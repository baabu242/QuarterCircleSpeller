from threading import Thread
from speller import Speller
import pandas as pd
from pylsl import resolve_stream, StreamInlet
import sys
import os
import argparse

def main():
    global opt, root
    t2 = Thread(target = lsl_receive_eeg)
    t3 = Thread(target = lsl_receive_marker)
    name = Speller(opt.name, root)
    if opt.record:
        t2.start()
        t3.start()
        name.train(opt.record, False, opt.append, opt.n)
    else:
        name.train(opt.record, False, opt.append, opt.n)
    print("Data Recording and preprocessing done")
    name.predict()

def lsl_receive_eeg():
    global isMarker, df_eeg, opt, root
    i = 0
    stream = resolve_stream('type', 'EEG')
    inlet = StreamInlet(stream[0])

    eeg_file = open(root + "recordings\\" + opt.name + "_eeg.csv", 'w')
    eeg_file.write(",".join(list(map(str, ["time_stamp"] + ["channel_" + str(i) for i in range(1,9)] ))) + '\n')

    while isMarker:
        sample, time_stamp = inlet.pull_sample()
        eeg_file.write(",".join(list(map(str, [time_stamp] + sample))) + '\n')
        # df_eeg.loc[i] = [time_stamp] + sample
        i+=1
    sample, time_stamp = inlet.pull_chunk(timeout = 5.0, max_samples = 5000)
    for j in range(len(time_stamp)):
        # df_eeg.loc[i+j] = [time_stamp[j]] + sample[j]
        eeg_file.write(",".join(list(map(str, [time_stamp[j]] + sample[j]))) + '\n')
    eeg_file.close()

def lsl_receive_marker():
    global isMarker, df_marker, opt, root
    max_n = 2*(2*opt.n + (2*opt.n)//10 + 1)
    stream = resolve_stream('type', 'Markers')
    inlet = StreamInlet(stream[0])
    i = 0
    while True:
        sample, time_stamp = inlet.pull_sample()
        df_marker.loc[i] = [time_stamp] + sample
        i += 1
        if i == max_n:
            print("Markers recorded")
            isMarker = False
            break
    df_marker.to_csv(root + "recordings\\" + opt.name + "_markers.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='test', help='Name of the User')
    parser.add_argument('--n', type=int, default=25, help='No. of trials per class')
    parser.add_argument('--record', type=bool, default=True, help='Record new data or not')
    parser.add_argument('--append', type=bool, default=False, help='Append the recorded data to an existing one or not')
    opt = parser.parse_args()

    root = os.getcwd() + "\\"
    isMarker = True
    df_eeg = pd.DataFrame(columns = ["time_stamp"] + ["channel_" + str(i) for i in range(1,9)])
    df_marker = pd.DataFrame(columns = ["time_stamp", "Marker"])
    main()


