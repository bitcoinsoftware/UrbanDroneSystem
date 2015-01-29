__author__ = 'user'
from PyQt4 import QtCore, QtGui

#class Connections(Functions):
class Connections():
    def connect(self):
        #movment XY
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('w'),self.pushButton_5, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL('clicked()'), self.pressW)
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('a'),self.pushButton_7, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL('clicked()'), self.pressA)
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('s'),self.pushButton_6, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL('clicked()'), self.pressS)
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('d'),self.pushButton_8, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL('clicked()'), self.pressD)
        #movment Z YAW
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('i'),self.pushButton_3, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.pressI)
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('j'),self.pushButton, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.pressJ)
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('k'),self.pushButton_4, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL('clicked()'), self.pressK)
        QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('l'),self.pushButton_2, QtCore.SIGNAL('clicked()'))
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.pressL)

        #camera
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL('clicked()'), self.startRecordingVideo)
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL('clicked()'), self.stopRecordingVideo)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL('sliderReleased()'), self.moveCamera)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL('sliderReleased()'), self.moveCamera)
        #audio
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL('clicked()'), self.playAudio)
        QtCore.QObject.connect(self.pushButton_14, QtCore.SIGNAL('clicked()'), self.stopAudio)
        QtCore.QObject.connect(self.pushButton_12, QtCore.SIGNAL('clicked()'), self.startRecordingAudio)
        QtCore.QObject.connect(self.pushButton_13, QtCore.SIGNAL('clicked()'), self.stopRecordingAudio)
        QtCore.QObject.connect(self.pushButton_15, QtCore.SIGNAL('clicked()'), self.selectFile)


        #QtCore.QObject.connect(self.centralwidget,QtCore.SIGNAL('w'),self.presW)
    #camera
    def startRecordingVideo(self):
        self.pressButton("StartRecordingVideo")

    def stopRecordingVideo(self):
        self.pressButton("StopRecordingVideo")

    def selectFile(self):
        self.pressButton("SelectFile")

    def moveCamera(self):
        pass
        #self.pressButton("MoveCamera")

    def playAudio(self):
        self.pressButton("PlayAudio")

    def stopAudio(self):
        self.pressButton("StopAudio")

    def startRecordingAudio(self):
        self.pressButton("StartRecordingAudio")

    def stopRecordingAudio(self):
        self.pressButton("StopRecordingAudio")

    def pressButton(self, signal):
        if signal=="StartRecordingVideo":
            self.pushButton_9.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_9.setStyleSheet("default")
        if signal=="StopRecordingVideo":
            self.pushButton_10.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_10.setStyleSheet("default")
        if signal=="PlayAudio":
            self.pushButton_11.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_11.setStyleSheet("default")
        if signal=="StopAudio":
            self.pushButton_14.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_14.setStyleSheet("default")

        if signal=="StartRecordingAudio":
            self.pushButton_12.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_12.setStyleSheet("default")
        if signal=="StopRecordingAudio":
            self.pushButton_13.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_13.setStyleSheet("default")
        if signal=="SelectFile":
            self.pushButton_15.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_15.setStyleSheet("default")


        if signal=="w":
            self.pushButton_5.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_5.setStyleSheet("default")
        if signal=="a":
            self.pushButton_7.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_7.setStyleSheet("default")
        if signal=="s":
            self.pushButton_6.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_6.setStyleSheet("default")
        if signal=="d":
            self.pushButton_8.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_8.setStyleSheet("default")


        if signal=="i":
            self.pushButton_3.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_3.setStyleSheet("default")
        if signal=="j":
            self.pushButton.setStyleSheet("border: 2px inset")
        else:
            self.pushButton.setStyleSheet("default")
        if signal=="k":
            self.pushButton_4.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_4.setStyleSheet("default")
        if signal=="l":
            self.pushButton_2.setStyleSheet("border: 2px inset")
        else:
            self.pushButton_2.setStyleSheet("default")



    def pressW(self):
        self.pressButton("w")
    def pressA(self):
        self.pressButton("a")
    def pressS(self):
        self.pressButton("s")
    def pressD(self):
        self.pressButton("d")

    def pressI(self):
        self.pressButton("i")
    def pressJ(self):
        self.pressButton("j")
    def pressK(self):
        self.pressButton("k")
    def pressL(self):
        self.pressButton("l")
    #w self.pushButton_5
    #a self.pushButton_7
    #s self.pushButton_6
    #d self.pushButton_8

    #i self.pushButton_3
    #j self.pushButton
    #k self.pushButton_4
    #l self.pushButton_2
