#Embedded file name: /home/noname/Dokumenty/AutonomousDrone/UrbanDroneSystem/DRONE/CLIENT/Connections.py
from PyQt4 import QtCore, QtGui
from functools import partial
from PS2Controller import *
from JSK420Joystick import *
import Client, VideoDisplay
import numpy, cv2
bPressedStyle = 'border: 2px inset'
bFreeStyle = 'default'
movementXYButtons = []
client = None

def connect(ui, param = None):
    global movementXYButtons
    movementXYButtons = [ui.pushButton_5, ui.pushButton_7, ui.pushButton_6,ui.pushButton_8]
    movementZYAWButtons = [ui.pushButton_3, ui.pushButton, ui.pushButton_4,ui.pushButton_2]
    leftHandButtons = [ui.spinBox_4, ui.spinBox_5, ui.spinBox_6, ui.spinBox_7,ui.spinBox_8,ui.spinBox_9]
    rightHandButtons = [ui.spinBox_10, ui.spinBox_11, ui.spinBox_12, ui.spinBox_13, ui.spinBox_14, ui.spinBox_15]
    audioButtons = [ui.pushButton_11, ui.pushButton_12, ui.pushButton_13, ui.pushButton_14, ui.pushButton_15, ui.pushButton_31]
    connectionButtons = [ui.pushButton_16, ui.pushButton_17, ui.pushButton_20]
    videoButtons = [ui.pushButton_9, ui.pushButton_10, ui.pushButton_30]

    ui.object = QtCore.QObject()

    #yaw, throttle, roll, pitch
    QtCore.QObject.connect(ui.object, QtCore.SIGNAL("move(int, int, int, int)"), partial(markButtonPress, ui))
    QtCore.QObject.connect(ui.object, QtCore.SIGNAL("move(int, int, int, int)"), partial(move, ui))
    QtCore.QObject.connect(ui.pushButton_5, QtCore.SIGNAL('clicked()'), partial(move, ui,  128, 128, 128, 255)) #'Forward'
    QtCore.QObject.connect(ui.pushButton_6, QtCore.SIGNAL('clicked()'), partial(move, ui,  128, 128, 128,   0)) #'Back'
    QtCore.QObject.connect(ui.pushButton_7, QtCore.SIGNAL('clicked()'), partial(move, ui,  128, 128,   0, 128)) #'Left'
    QtCore.QObject.connect(ui.pushButton_8, QtCore.SIGNAL('clicked()'), partial(move, ui,  128, 128, 255, 128)) #'Right'
    QtCore.QObject.connect(ui.pushButton,   QtCore.SIGNAL('clicked()'), partial(move, ui,    0, 128, 128, 128)) #'rotateLeft'
    QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL('clicked()'), partial(move, ui,  255, 128, 128, 128)) #'rotateRight'
    QtCore.QObject.connect(ui.pushButton_3, QtCore.SIGNAL('clicked()'), partial(move, ui,  128, 255, 128, 128)) # 'Up'
    QtCore.QObject.connect(ui.pushButton_4, QtCore.SIGNAL('clicked()'), partial(move, ui,  128,   0, 128, 128)) #'Down'

    #QtCore.QObject.connect(ui.object, QtCore.SIGNAL("inputDevicePressed()"), partial(move, 'allDirections', ui))

    QtCore.QObject.connect(ui.verticalSlider_2, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Left', ui))
    QtCore.QObject.connect(ui.verticalSlider_3, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Left', ui))
    QtCore.QObject.connect(ui.verticalSlider_4, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Left', ui))
    QtCore.QObject.connect(ui.horizontalSlider_2, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Left', ui))
    QtCore.QObject.connect(ui.horizontalSlider, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Left', ui))
    QtCore.QObject.connect(ui.verticalSlider_5, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Right', ui))
    QtCore.QObject.connect(ui.verticalSlider_6, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Right', ui))
    QtCore.QObject.connect(ui.verticalSlider_7, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Right', ui))
    QtCore.QObject.connect(ui.horizontalSlider_3, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Right', ui))
    QtCore.QObject.connect(ui.horizontalSlider_4, QtCore.SIGNAL('sliderReleased()'), partial(moveArm, 'Right', ui))
    QtCore.QObject.connect(ui.spinBox_5, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Left', '4', ui, leftHandButtons, ui.spinBox_5))
    QtCore.QObject.connect(ui.spinBox_6, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Left', '3', ui, leftHandButtons, ui.spinBox_6))
    QtCore.QObject.connect(ui.spinBox_7, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Left', '2', ui, leftHandButtons, ui.spinBox_7))
    QtCore.QObject.connect(ui.spinBox_8, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Left', '1', ui, leftHandButtons, ui.spinBox_8))
    QtCore.QObject.connect(ui.spinBox_9, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Left', '0', ui, leftHandButtons, ui.spinBox_9))
    QtCore.QObject.connect(ui.spinBox_4, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Left', '01234', ui, leftHandButtons, ui.spinBox_4))
    QtCore.QObject.connect(ui.spinBox_11, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Right', '0', ui, rightHandButtons, ui.spinBox_11))
    QtCore.QObject.connect(ui.spinBox_12, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Right', '1', ui, rightHandButtons, ui.spinBox_12))
    QtCore.QObject.connect(ui.spinBox_13, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Right', '2', ui, rightHandButtons, ui.spinBox_13))
    QtCore.QObject.connect(ui.spinBox_14, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Right', '3', ui, rightHandButtons, ui.spinBox_14))
    QtCore.QObject.connect(ui.spinBox_15, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Right', '4', ui, rightHandButtons, ui.spinBox_15))
    QtCore.QObject.connect(ui.spinBox_10, QtCore.SIGNAL('valueChanged(int)'), partial(moveFinger, 'Right', '01234', ui, rightHandButtons, ui.spinBox_10))
    ui.frame_8.setEnabled(False)
    ui.frame_5.setEnabled(False)
    QtCore.QObject.connect(ui.pushButton_15, QtCore.SIGNAL('clicked()'), partial(selectFile, ui))
    QtCore.QObject.connect(ui.pushButton_11, QtCore.SIGNAL('clicked()'), partial(playAudio, ui, audioButtons, ui.pushButton_11))
    QtCore.QObject.connect(ui.pushButton_14, QtCore.SIGNAL('clicked()'), partial(stopAudio, ui, audioButtons, ui.pushButton_14))
    QtCore.QObject.connect(ui.pushButton_12, QtCore.SIGNAL('clicked()'), partial(startRecordingAudio, ui, audioButtons, ui.pushButton_12))
    QtCore.QObject.connect(ui.pushButton_13, QtCore.SIGNAL('clicked()'), partial(stopRecordingAudio, ui, audioButtons, ui.pushButton_13))
    QtCore.QObject.connect(ui.pushButton_31, QtCore.SIGNAL('clicked()'), partial(saveAudio, ui, audioButtons, ui.pushButton_31))
    ui.groupBox_3.setEnabled(False)
    QtCore.QObject.connect(ui.pushButton_16, QtCore.SIGNAL('clicked()'), partial(connectServer, ui, param, connectionButtons, ui.pushButton_16))
    QtCore.QObject.connect(ui.pushButton_17, QtCore.SIGNAL('clicked()'), partial(disconnectServer, ui, connectionButtons, ui.pushButton_17))
    QtCore.QObject.connect(ui.pushButton_20, QtCore.SIGNAL('clicked()'), partial(stopServer, ui, videoButtons, ui.pushButton_20))
    QtCore.QObject.connect(ui.pushButton_18, QtCore.SIGNAL('clicked()'), partial(startStream, ui, videoButtons, ui.pushButton_18))
    QtCore.QObject.connect(ui.pushButton_19, QtCore.SIGNAL('clicked()'), partial(stopStream, ui, videoButtons, ui.pushButton_19))

    QtCore.QObject.connect(ui.object, QtCore.SIGNAL('displayImage(PyQt_PyObject, int)'), partial(displayImage, ui))
    QtCore.QObject.connect(ui.pushButton_9, QtCore.SIGNAL('clicked()'), partial(startRecordingVideo, ui, videoButtons, ui.pushButton_9))
    QtCore.QObject.connect(ui.pushButton_10, QtCore.SIGNAL('clicked()'), partial(stopRecordingVideo, ui, videoButtons, ui.pushButton_10))
    QtCore.QObject.connect(ui.verticalSlider_8, QtCore.SIGNAL('sliderReleased()'), partial(moveCamera, ui))
    QtCore.QObject.connect(ui.verticalSlider, QtCore.SIGNAL('sliderReleased()'), partial(moveCamera, ui))
    QtCore.QObject.connect(ui.verticalSlider_9, QtCore.SIGNAL('sliderReleased()'), partial(moveCamera, ui))
    QtCore.QObject.connect(ui.pushButton_30, QtCore.SIGNAL('clicked()'), partial(saveVideo, ui, videoButtons, ui.pushButton_30))

    ui.frame_6.setEnabled(False)
    ui.groupBox_4.setEnabled(False)
    ui.pushButton_17.setEnabled(False)
    ui.pushButton_20.setEnabled(False)
    QtCore.QObject.connect(ui.spinBox_3, QtCore.SIGNAL('valueChanged(int)'), partial(setCameraWidgets, ui))
    QtCore.QObject.connect(ui.pushButton_21, QtCore.SIGNAL('clicked()'), partial(applyInputDevice, ui))
    ui.inputDevice = InputDevice()

def applyInputDevice(ui):
    deviceName = str(ui.comboBox_2.currentText())
    if deviceName =='PS2 Pad':
        print deviceName
        ui.inputDevice= PS2Controller(0x0079, 0x0006, ui) #idVendor=0x0079, idProduct=0x0006
    else:
        print ">",deviceName,"<"
    ui.inputDevice.start()

def move(ui, yaw, throttle, roll, pitch):
    global client
    directionPID = ui.verticalSlider_10.value()
    altyawPID = ui.verticalSlider_11.value()
    client.request('move', {'argument':{'yaw':yaw*altyawPID, 'throttle':throttle*altyawPID, 'roll':roll*directionPID,
                                        'pitch':pitch*directionPID}}, waitForConfiramtion=False)

def markButtonPress(ui, yaw, throttle, roll, pitch):
    if roll > 128:
        ui.pushButton_8.setStyleSheet("border: 2px inset")
        ui.pushButton_7.setStyleSheet("default")
    elif roll<127:
        ui.pushButton_7.setStyleSheet("border: 2px inset")
        ui.pushButton_8.setStyleSheet("default")
    else:
        ui.pushButton_7.setStyleSheet("default")
        ui.pushButton_8.setStyleSheet("default")

    if pitch > 128:
        ui.pushButton_5.setStyleSheet("border: 2px inset")
        ui.pushButton_6.setStyleSheet("default")
    elif pitch < 127:
        ui.pushButton_6.setStyleSheet("border: 2px inset")
        ui.pushButton_5.setStyleSheet("default")
    else:
        ui.pushButton_5.setStyleSheet("default")
        ui.pushButton_6.setStyleSheet("default")

    if throttle > 128:
        ui.pushButton_3.setStyleSheet("border: 2px inset")
        ui.pushButton_4.setStyleSheet("default")
    elif throttle < 127:
        ui.pushButton_4.setStyleSheet("border: 2px inset")
        ui.pushButton_3.setStyleSheet("default")
    else:
        ui.pushButton_3.setStyleSheet("default")
        ui.pushButton_4.setStyleSheet("default")

    if yaw > 128:
        ui.pushButton_2.setStyleSheet("border: 2px inset")
        ui.pushButton.setStyleSheet("default")
    elif yaw < 127:
        ui.pushButton.setStyleSheet("border: 2px inset")
        ui.pushButton_2.setStyleSheet("default")
    else:
        ui.pushButton.setStyleSheet("default")
        ui.pushButton_2.setStyleSheet("default")

def displayImage(ui, qpixmap, cameraNumb):
    if cameraNumb==0:
        ui.label_14.setPixmap(qpixmap)
    elif cameraNumb==1:
        ui.label_15.setPixmap(qpixmap)

def moveArm(side, ui):
    if side == 'Left':
        alfa = ui.verticalSlider_2.value()
        beta = ui.verticalSlider_3.value()
        gamma = ui.verticalSlider_4.value()
        delta = ui.horizontalSlider_2.value()
    elif side == 'Right':
        alfa = ui.verticalSlider_5.value()
        beta = ui.verticalSlider_6.value()
        gamma = ui.verticalSlider_7.value()
        delta = ui.horizontalSlider_3.value()
    client.steer('moveArm', {'side': side,
     'alfa': alfa,
     'beta': beta,
     'gamma': gamma,
     'delta': delta})

def moveFinger(side, finger, ui, buttons, btn):
    if finger == '01234':
        if btn.isChecked():
            state = True
        else:
            state = False
        for bt in buttons:
            bt.setChecked(state)

        params = {'side': side,
         '0': state,
         '1': state,
         '2': state,
         '3': state,
         '4': state}
    else:
        state = btn.isChecked()
        params = {'side': side,
         finger: state}
    client.steer('moveFinger', params)

def selectFile(ui):
    pass

def playAudio(ui, buttons, btn):
    pass

def stopAudio(ui, buttons, btn):
    pass

def startRecordingAudio(ui, buttons, btn):
    pass

def stopRecordingAudio(ui, buttons, btn):
    pass

def saveAudio(ui, buttons, btn):
    pass

def connectServer(ui, param, buttons, btn):
    global client
    ui.videoDisplay = [None, None]
    host = str(ui.lineEdit.text())
    port = ui.spinBox.value()
    print host, port, param
    client = Client.Client(host, port, param)
    if client != None:
        ui.frame_8.setEnabled(True)
        ui.frame_5.setEnabled(True)
        ui.pushButton_17.setEnabled(True)
        ui.pushButton_20.setEnabled(True)
        ui.pushButton_16.setEnabled(False)
        if client.features['videoAvailable']:
            ui.frame_6.setEnabled(True)
            ui.groupBox_4.setEnabled(True)
            ui.spinBox_3.setMaximum(len(client.features['cameraParams']) - 1)
            ui.spinBox_3.setEnabled(True)
            ui.cameraParams = client.features['cameraParams']
            setCameraWidgets(ui)
        ui.comboBox.setCurrentIndex(0)
        for i in range(ui.comboBox.count()):
            if str(ui.comboBox.itemText(i)) == client.features['serverType']:
                ui.comboBox.setCurrentIndex(i)
                break

        setMovementWidgets(ui)
        if client.features['audioAvailable']:
            ui.groupBox_3.setEnabled(True)
            if not client.features['microphoneAvailable']:
                ui.frame_7.setEnabled(False)
            if not client.features['speakerAvailable']:
                ui.frame.setEnabled(False)
        for item in client.features['sensorList']:
            ui.listWidget.insertItem(0, str((item, client.features['sensorList'][item])))

def setMovementWidgets(ui):
    serverType = client.features['serverType']
    if serverType == 'manipulator':
        ui.frame_8.setEnabled(False)
    elif serverType == 'tank':
        ui.pushButton_3.setEnabled(False)
        ui.pushButton_4.setEnabled(False)
    elif serverType == 'car' or serverType == 'boat':
        ui.groupBox.setEnabled(False)
    if client.features['leftRoboticArmAvailable']:
        ui.frame_3.setEnable(True)
        if client.features['leftRoboticFingersAvailable']:
            ui.frame_9.setEnabled(True)
        else:
            ui.frame_9.setEnabled(False)
    else:
        ui.frame_3.setEnabled(False)
    if client.features['rightRoboticArmAvailable']:
        ui.frame_4.setEnabled(True)
        if client.features['rightRoboticFingersAvailable']:
            ui.frame_10.setEnabled(True)
        else:
            ui.frame_10.setEnabled(False)
    else:
        ui.frame_4.setEnable(False)

def setCameraWidgets(ui):
    print 'camera'
    i = ui.spinBox_3.value()
    if not ui.cameraParams[i]['xAxisAvailable']:
        ui.verticalSlider_8.setEnabled(False)
    else:
        ui.verticalSlider_8.setEnabled(True)
    if not ui.cameraParams[i]['yAxisAvailable']:
        ui.verticalSlider.setEnabled(False)
    else:
        ui.verticalSlider.setEnabled(True)
    if not ui.cameraParams[i]['zAxisAvailable']:
        ui.verticalSlider_9.setEnabled(False)
    else:
        ui.verticalSlider_9.setEnabled(True)

def disconnectServer(ui, buttons, btn):
    ui.inputDevice.stop()
    if ui.videoDisplay[0] != None:
        stopStream(ui, None, None, cameraIndex=0)
    if ui.videoDisplay[0] != None:
        stopStream(ui, None, None, cameraIndex=1)
    client.end()
    ui.frame_8.setEnabled(False)
    ui.frame_5.setEnabled(False)
    ui.pushButton_17.setEnabled(False)
    ui.pushButton_20.setEnabled(False)
    ui.pushButton_16.setEnabled(True)
    if client.features['videoAvailable']:
        ui.frame_6.setEnabled(False)
        ui.groupBox_4.setEnabled(False)
        ui.spinBox_3.setEnabled(False)
        ui.groupBox_3.setEnabled(False)

def startStream(ui, buttons, btn):
    cameraIndex = int(ui.spinBox_3.value())
    if client.request('startStream', {'argument':cameraIndex}):
        ui.videoDisplay[cameraIndex] = VideoDisplay.VideoDisplay(ui, cameraIndex)
        print 'zaczynam odbierac pakiety przychodzace na port', client.features['cameraParams'][cameraIndex]['videoPort']
        ui.videoDisplay[cameraIndex].startVideoConnection(client.features['cameraParams'][cameraIndex]['videoPort'])
        if client.request('connectVideo', {'argument':cameraIndex}):
            ui.videoDisplay[cameraIndex].start()
            print 'serwer video uruchomiony'

def stopStream(ui, buttons, btn, cameraIndex =-1):
    if cameraIndex==-1:
        cameraIndex = int(ui.spinBox_3.value())
    if client.request('stopStream', {'argument':cameraIndex}):
        ui.videoDisplay[cameraIndex].stopVideoConnection()
        ui.videoDisplay[cameraIndex] = None

def stopServer(ui, buttons, btn):
    client.request("stopServer")
    pass


def startRecordingVideo(ui, buttons, btn):
    pass


def stopRecordingVideo(ui, buttons, btn):
    pass


def moveCamera(ui):
    pass


def saveVideo(ui, buttons, btn):
    pass
