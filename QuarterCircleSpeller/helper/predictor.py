import numpy as np
from scipy import signal

def get_features(data, frequency = 250):
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
        channels = ["channel_" + str(i) for i in range(1,9)]
        for channel in range(len(channels)):
            alpha_band_powers.append(bandpower(data=data[channel], sf=frequency, band=alpha_band,
                                               window_sec=2,
                                               relative=False))
            beta_band_powers.append(bandpower(data=data[channel], sf=frequency, band=beta_band,
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


def preprocess(datA, frequency = 250):
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
    
    data = datA.copy()
    scale_factor = 4500000 / (8 * (2 ** 23 - 1))
    channels = ["channel_" + str(i) for i in range(1,9)]
    data[channels] = data[channels] * scale_factor
    
    for channel in channels:
        data[channel] = notch_filter(50, np.array(data[channel]), fs=frequency)
        data[channel] = bandpass(7, 80, np.array(data[channel]), fs=frequency)

    start, end = 0,500
    final = []
    for j in range(11):
        temp_data = data[start:end]
        start += 100
        end += 100
        final.append(get_features(np.array(temp_data).T))   
    
    return final