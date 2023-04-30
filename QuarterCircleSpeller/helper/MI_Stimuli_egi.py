from PyQt5.QtWidgets import QWidget #, QPushButton, QLabel
from PyQt5.QtCore import QTimer
import winsound
from helper.expUI import Ui_Form
import time
from pylsl import StreamInfo, StreamOutlet
# _TEST = True
from PyQt5.QtWidgets import QApplication
import sys

class MI(QWidget):
    def __init__(self, n):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.Welcomelabel.setVisible(True)
        self.ui.Instructionslabel.setVisible(False)
        self.ui.Flabel.setVisible(False)
        self.ui.Rlabel.setVisible(False)
        self.ui.Llabel.setVisible(False)
        self.ui.Blabel.setVisible(False)
        self.ui.Slabel.setVisible(False)

        self.info = StreamInfo(name='MotorImag-Markers', type='Markers', channel_count=1,
                  nominal_srate=0, channel_format='string',
                  source_id='t8u43t98u')
        self.outlet = StreamOutlet(self.info)
        self.trials_per_class = n
        self.pause_every = 10
        self.start_time = time.time()
        self.perform_time = 6000 #ms display
        self.fixation_period = 2000 #ms 
        self.rest_period = 1000 #ms
        self.pause_duration = 8000 #ms

        self.Ftimer = QTimer(self)
        self.Ttimer = QTimer(self)
        self.Btimer = QTimer(self)
        self.Rtimer = QTimer(self)

        # self.marker_list = [1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        self.marker_list = self.make_marker_list()
        print("Marker List : ", self.marker_list)
        self.i = 0
        self.marker = -1

    def make_marker_list(self):
        sub_list = [1 for i in range(self.trials_per_class)] + [2 for i in range(self.trials_per_class)]
        from random import shuffle
        shuffle(sub_list)
        main_list = []
        for i in range(1,len(sub_list)+1) :
            main_list.append(sub_list[i-1])
            if i%self.pause_every == 0:
                main_list.append(0)
        return main_list

    def keyPressEvent(self, e):
        print(e.key())
        if e.key() == 16777220: #press enter to call start function
            self.start()
        if e.key() == 16777236: #press right-arrow to show right cue
            self.showRight()
        if e.key() == 16777234: #press left-arrow to show left cue
            self.showLeft()
        if e.key() == 32:
            winsound.Beep(500, 200)
            self.preTrialForward()
            
    def preTrialForward(self):
        if self.ui.Welcomelabel.isVisible():
            self.ui.Welcomelabel.setVisible(False)
            self.ui.Instructionslabel.setVisible(True)

        elif self.ui.Instructionslabel.isVisible():
            self.ui.Instructionslabel.setVisible(False)
            self.ui.Slabel.setVisible(True)

    def showRight(self):
        # print('Right')
        self.ui.Llabel.setVisible(False)
        self.ui.Rlabel.setVisible(True)

    def showLeft(self):
        # print('left')
        self.ui.Rlabel.setVisible(False)
        self.ui.Llabel.setVisible(True)

    def start(self):
        #egi_connect(1)
        self.start_time = time.time()
        self.ui.Slabel.setVisible(False)
        self.outlet.push_sample(['start'])
        self.BlackScreen()

    def BlackScreen(self):
        print('I am Black Screen at : ', round(time.time()-self.start_time, 1))
        self.ui.Blabel.setVisible(True)
        self.ui.Flabel.setVisible(False)
        self.ui.Rlabel.setVisible(False)
        self.ui.Llabel.setVisible(False)
        self.ui.Slabel.setVisible(False)
        self.Btimer.singleShot(self.pause_duration, self.Fixation) #pause_duration = 8s
        winsound.Beep(500, 1000)

    def Fixation(self):
        print('I am Fixation at : ', round(time.time()-self.start_time, 1))
        self.outlet.push_sample(['Fixation'])
        self.ui.Rlabel.setVisible(False)
        self.ui.Llabel.setVisible(False)
        self.ui.Flabel.setVisible(True)
        self.Ftimer.singleShot(self.fixation_period, self.Trial) #wait_time (partial) = 2s

    def Rest(self):
        print('I am Rest Screen at : ', round(time.time()-self.start_time, 1))
        self.ui.Blabel.setVisible(True)
        self.ui.Flabel.setVisible(False)
        self.ui.Rlabel.setVisible(False)
        self.ui.Llabel.setVisible(False)
        self.ui.Slabel.setVisible(False)
        self.Rtimer.singleShot(self.rest_period, self.Fixation) #wait_time (partial) = 1s

    def Trial(self):
        if self.i>=len(self.marker_list):
            self.close()
            return


        self.marker = self.marker_list[self.i]
        print('I am marker ', self.marker, 'at : ', round(time.time()-self.start_time, 1))
        
        self.i = self.i + 1

        if self.marker == 1:
            self.showLeft()
            self.outlet.push_sample(['left'])
        elif self.marker == 2:
            self.showRight()
            self.outlet.push_sample(['right'])
        else :
            self.outlet.push_sample(['Pause'])
            self.BlackScreen()
            return

        self.Ttimer.singleShot(self.perform_time, self.Rest) #perform_time = 6s