import os
import time
import sys
import pandas as pd
from recorder import Record
from helper.predictor import preprocess
import numpy as np
from threading import Thread
from MyWindow import MyWindow
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets, QtGui, QtCore
from pylsl import resolve_stream, StreamInlet, StreamInfo, StreamOutlet
import pickle
from random import randint
import lazypredict.Supervised as lp
from sklearn.model_selection import train_test_split


os.environ['KMP_DUPLICATE_LIB_OK']='True'

class Speller:

    def __init__(self, name, root):
        self.root = root
        self.name = name
        self.model = None
        self.data = None 
        self.info = StreamInfo(name='Left-Right-Predictions', type='Predictions', channel_count=1,
                  nominal_srate=0, channel_format='int32', source_id = 't8u43t98v')
        self.outlet = StreamOutlet(self.info)
        self.features = None
        
    def appendData(self, df2):
        try:
            df1 = pd.read_csv(self.root + "recordings\\" + self.name + ".csv", index_col = 0)
            return pd.concat([df1,df2])
        except:
            return df2
        
    def fit(self):
        def func(x):
            if x == "right":
                return 1
            else:
                return 0
            
        self.data["labels"] = self.data["labels"].apply(func)

        X = self.data.drop("labels", axis = 1)
        y = self.data["labels"]
        self.features = X.columns

        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

        clf = lp.LazyClassifier()
        models, predictions = clf.fit(X_train, X_test, y_train, y_test)

        print(models)

        self.model = clf.models[models.index[0]]

    def train(self, record = False, from_pretrained = False, append = True, n = 5):
        if record:
            temp = Record(self.name, n, self.root)
            if append:
                self.data = self.appendData(temp.feature_matrix)
                self.data = self.data.reset_index().drop("index", axis = 1)
            else:
                self.data = temp.feature_matrix
            self.data.to_csv(self.root + "recordings\\" + self.name + ".csv")
            print("Done")
        else:
            try:
                self.data = pd.read_csv(self.root + "recordings\\" + self.name + ".csv", index_col = 0)
            except Exception as e:
                print(e)
                
        self.fit()

    def capture_eeg_signal(self):
        stream = resolve_stream('type', 'EEG')
        inlet = StreamInlet(stream[0])
        ss, tt = inlet.pull_chunk(max_samples = 10000)

        i = 0
        eeg_test_file = open(self.root + "recordings\\" + self.name + "_test_eeg.csv", 'w')
        while True:
            print(f"value of i = {i}\n")
            sample, time_stamp = inlet.pull_chunk(timeout = 100, max_samples = 1500)
            left_count, right_count = 0,0
            data = pd.DataFrame(sample, columns = ["channel_" + str(i) for i in range(1,9)])
            predictions = preprocess(data)
            for prediction in predictions:
                eeg_test_file.write(",".join(list(map(str, list(prediction)))) + '\n')
                prediction = prediction.reshape((1,64))
                prediction = pd.DataFrame(prediction, columns = self.features)
                val = self.make_prediction(prediction)
                if val[0] == 0:
                    left_count += 1
                else:
                    right_count += 1 
            i += 1
            if i == 1:
                continue
            if left_count >= right_count:
                self.outlet.push_sample([0])
            else:
                self.outlet.push_sample([1])
            if i == 100:
                break

    def control_application(self):
        app = QtWidgets.QApplication([])
        application = MyWindow()
        application.show()
        time.sleep(2)
        timer = QTimer()
        timer.timeout.connect(application.updateWindow)
        timer.start(1)
        sys.exit(app.exec())

    def predict(self):
        #capture eeg data
        #then pass a dataframe of dimension 500*8 with appropriate columns name
        t1 = Thread(target = self.capture_eeg_signal)
        t2 = Thread(target = self.control_application)

        t2.start()
        t1.start()
        

    def make_prediction(self, x):
        return self.model.predict(x)