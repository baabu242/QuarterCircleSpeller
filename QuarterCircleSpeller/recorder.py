from helper.MI_Stimuli_egi import MI
import sys
from PyQt5.QtWidgets import QApplication
import pandas as pd
import numpy as np
from scipy import signal
import time
from tqdm import tqdm
from bisect import bisect_left

class Record:
    #records one session approximately 30 minutes
    def __init__(self, name, n, root, frequency = 250):
        self.name = name
        self.root = root
        self.channels = ["channel_" + str(i) for i in range(1,9)]
        self.sf = frequency
        self.n_trials = n
        self.scale_factor = 4500000 / (8 * (2 ** 23 - 1))
        self.record()
        time.sleep(5)
        self.filtered_data = self.preprocess()
        self.batches, self.labels = self.epoching()
        self.feature_matrix = self.feature_extraction()

    def record(self):
        app = QApplication(sys.argv)
        demo = MI(self.n_trials)
        demo.show()
        ret = app.exec_()

    def preprocess(self):
        def notch_filter(val, data, fs=100):
            notch_freq_Hz = np.array([float(val)])
            for freq_Hz in np.nditer(notch_freq_Hz):
                bp_stop_Hz = freq_Hz + 3.0 * np.array([-1, 1])
                b, a = signal.butter(3, bp_stop_Hz / (fs / 2.0), 'bandstop')
                fin = data = signal.lfilter(b, a, data)
            return fin

        def bandpass(start, stop, data, fs=100):
            bp_Hz = np.array([start, stop])
            b, a = signal.butter(5, bp_Hz / (fs / 2.0), btype='bandpass')
            return signal.lfilter(b, a, data, axis=0)

        #opens the xdf file do something returns un-epoched data as pandas df with labels

        # copying EEG data from xdf into a DataFrame
        eeg_df = None
        print("Opening the EEG CSV file........ (might take some time)")
        while True:
            try:
                eeg_df = pd.read_csv(self.root + "recordings\\" + self.name + "_eeg.csv")
                print("Opened")
                break
            except:
                time.sleep(5)
                continue
        # scaling the values
        eeg_df[self.channels] = eeg_df[self.channels] * self.scale_factor
        # filtering
        # print('filtering the data...')
        # for channel in self.channels:
        #     eeg_df[channel] = notch_filter(50, np.array(eeg_df[channel]), fs=self.sf)
        #     eeg_df[channel] = bandpass(7, 80, np.array(eeg_df[channel]), fs=self.sf)
        # print('Data filtered!')
        #eeg_df['time_stamp'] = eeg_df['time_stamp'].apply(lambda x: int(x))

        # copying Marker data from xdf into a DataFrame
        marker_df = pd.read_csv(self.root + "recordings\\" + self.name + "_markers.csv", index_col = 0)
        marker_df = marker_df[(marker_df["Marker"] == "left") | (marker_df["Marker"] == "right")]
        #print(marker_df)
        eeg_time_stamps_arr = eeg_df['time_stamp'].to_numpy()
        final = pd.DataFrame()
        for i in range(len(marker_df)):
            kk = bisect_left(eeg_time_stamps_arr, marker_df.iloc[i]["time_stamp"])
            temp = eeg_df[kk:kk+1500].copy()
            for channel in self.channels:
                temp[channel] = notch_filter(50, np.array(temp[channel]), fs=self.sf)
                temp[channel] = bandpass(7, 80, np.array(temp[channel]), fs=self.sf)
            arr = ["start-" + str(i)] + [marker_df.iloc[i]["Marker"]]*1498 + ["end-" + str(i)]
            temp["Marker"] = arr
            final = pd.concat([final, temp])
        return final.reset_index().drop("index", axis = 1)

    def epoching(self, window_size = 500, skip = 100):
        batches, labels = list(), list()
        start_index, end_index = 0, window_size
        while True:
            batch = np.array(self.filtered_data[self.channels][start_index:end_index])
            label = self.filtered_data["Marker"][start_index+1]
            batches.append(batch.T)
            labels.append(label)
            if end_index == len(self.filtered_data):
                break
            elif end_index%1500 == 0:
                start_index = end_index
                end_index = start_index + window_size
            else:
                start_index += skip
                end_index += skip
        return batches, labels

    def feature_extraction(self):
        def get_features(data):
            from scipy import stats
            def mean(data):
                return np.mean(data, axis=-1)

            def std(data):
                return np.std(data, axis=-1)

            def skewness(data):
                return stats.skew(data, axis=-1)

            def kurtosis(data):
                return stats.kurtosis(data, axis=-1)

            def bandpowers(data) :
                # for band power
                alpha_band = [8, 12]
                beta_band = [12, 30]
                alpha_band_powers = []
                beta_band_powers = []

                def bandpower(data, sf, band, window_sec=None, relative=False):
                    # copied from https://raphaelvallat.com/bandpower.html
                    """Compute the average power of the signal x in a specific frequency band.

                    Parameters
                    ----------
                    data : 1d-array
                        Input signal in the time-domain.
                    sf : float
                        Sampling frequency of the data.
                    band : list
                        Lower and upper frequencies of the band of interest.
                    window_sec : float
                        Length of each window in seconds.
                        If None, window_sec = (1 / min(band)) * 2
                    relative : boolean
                        If True, return the relative power (= divided by the total power of the signal).
                        If False (default), return the absolute power.

                    Return
                    ------
                    bp : float
                        Absolute or relative band power.
                    """
                    from scipy.signal import welch
                    from scipy.integrate import simps
                    band = np.asarray(band)
                    low, high = band

                    # Define window length
                    if window_sec is not None:
                        nperseg = window_sec * sf
                    else:
                        nperseg = (2 / low) * sf

                    # Compute the modified periodogram (Welch)
                    freqs, psd = welch(data, sf, nperseg=nperseg)

                    # Frequency resolution
                    freq_res = freqs[1] - freqs[0]

                    # Find closest indices of band in frequency vector
                    idx_band = np.logical_and(freqs >= low, freqs <= high)

                    # Integral approximation of the spectrum using Simpson's rule.
                    bp = simps(psd[idx_band], dx=freq_res)

                    if relative:
                        bp /= simps(psd, dx=freq_res)
                    return bp

                for channel in range(len(self.channels)):
                    alpha_band_powers.append(bandpower(data=data[channel], sf=self.sf, band=alpha_band,
                                                       window_sec=2,
                                                       relative=False))
                    beta_band_powers.append(bandpower(data=data[channel], sf=self.sf, band=beta_band,
                                                      window_sec=2,
                                                      relative=False))
                alpha_band_powers = np.array(alpha_band_powers)
                beta_band_powers = np.array(beta_band_powers)

                return {'alpha_band_power' : alpha_band_powers, 'beta_band_power' : beta_band_powers}

            def wavelet_features(data):
                from pywt import dwt
                cA_values = []
                cD_values = []
                cA_mean = []
                cA_std = []
                cA_Energy = []
                cD_mean = []
                cD_std = []
                cD_Energy = []
                Entropy_D = []
                Entropy_A = []

                for i in range(len(data)):
                    cA, cD = dwt(data[i, :], 'coif1')
                    cA_values.append(cA)
                    cD_values.append(cD)  # calculating the coefficients of wavelet transform.
                for x in range(len(data)):
                    cA_Energy.append(abs(np.sum(np.square(cA_values[x]))))
                    # features.append(abs(np.sum(np.square(cA_values[x]))))

                for x in range(len(data)):
                    cD_Energy.append(abs(np.sum(np.square(cD_values[x]))))
                    # features.append(abs(np.sum(np.square(cD_values[x]))))

                cA_Energy = np.array(cA_Energy)
                cD_Energy = np.array(cD_Energy)

                features = {'cA_Energy': cA_Energy, 'cD_Energy': cD_Energy}

                return features

            features_dict = {
                'mean': mean(data),
                'std': std(data),
                'skewness' : skewness(data),
                'kurtosis' : kurtosis(data),
            }
            features_dict.update(wavelet_features(data))
            features_dict.update(bandpowers(data))

            return np.concatenate((features_dict['mean'],features_dict['std'],features_dict['skewness'],
                                   features_dict['kurtosis'],features_dict['cA_Energy'],features_dict['cD_Energy'],
                                   features_dict['alpha_band_power'], features_dict['beta_band_power']), axis=-1)

        print("Extracting Features...")
        features = []
        feature_names = ['mean', 'std', 'skewness', 'kurtosis', 'cA_Energy', 'cD_Energy', 'alpha_band_power', 'beta_band_power']
        for data in tqdm(self.batches):
            features.append(get_features(data))
        features=np.array(features)
        # features.shape
        feature_df_cols = []
        for feature_name in feature_names:
            for j in range(len(self.channels)):
                feature_df_cols.append('{}_{}'.format(feature_name, j+1))
        feature_df = pd.DataFrame(features, columns=feature_df_cols)
        print("Done!")
        feature_df["labels"] = self.labels
        return feature_df