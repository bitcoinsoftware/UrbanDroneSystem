# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Jun 10 20:12:43 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1375, 779)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame_6 = QtGui.QFrame(self.centralwidget)
        self.frame_6.setEnabled(True)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1280, 480))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.label_14 = QtGui.QLabel(self.frame_6)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8("videoIcon.png")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(640, 0, 640, 480))
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setPixmap(QtGui.QPixmap(_fromUtf8("videoIcon.png")))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 560, 231, 61))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.listWidget = QtGui.QListWidget(self.groupBox_5)
        self.listWidget.setGeometry(QtCore.QRect(0, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.groupBox_7 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(0, 480, 231, 81))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.frame_2 = QtGui.QFrame(self.groupBox_7)
        self.frame_2.setGeometry(QtCore.QRect(0, 20, 231, 61))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit = QtGui.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(60, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.spinBox = QtGui.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(60, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(99999)
        self.spinBox.setProperty("value", 12345)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.pushButton_16 = QtGui.QPushButton(self.frame_2)
        self.pushButton_16.setGeometry(QtCore.QRect(150, 0, 81, 21))
        self.pushButton_16.setObjectName(_fromUtf8("pushButton_16"))
        self.pushButton_17 = QtGui.QPushButton(self.frame_2)
        self.pushButton_17.setGeometry(QtCore.QRect(150, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName(_fromUtf8("pushButton_17"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 40, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_20 = QtGui.QPushButton(self.frame_2)
        self.pushButton_20.setGeometry(QtCore.QRect(150, 41, 81, 20))
        self.pushButton_20.setObjectName(_fromUtf8("pushButton_20"))
        self.frame_5 = QtGui.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(635, 480, 731, 251))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.frame_4 = QtGui.QFrame(self.frame_5)
        self.frame_4.setGeometry(QtCore.QRect(370, 0, 361, 251))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_13 = QtGui.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(180, 0, 176, 241))
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("roboticArm.jpg")))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalSlider_5 = QtGui.QSlider(self.frame_4)
        self.verticalSlider_5.setGeometry(QtCore.QRect(230, 125, 31, 76))
        self.verticalSlider_5.setMaximum(180)
        self.verticalSlider_5.setProperty("value", 90)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName(_fromUtf8("verticalSlider_5"))
        self.verticalSlider_6 = QtGui.QSlider(self.frame_4)
        self.verticalSlider_6.setGeometry(QtCore.QRect(200, 20, 29, 81))
        self.verticalSlider_6.setMaximum(180)
        self.verticalSlider_6.setProperty("value", 90)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName(_fromUtf8("verticalSlider_6"))
        self.verticalSlider_7 = QtGui.QSlider(self.frame_4)
        self.verticalSlider_7.setGeometry(QtCore.QRect(290, 10, 21, 81))
        self.verticalSlider_7.setMaximum(180)
        self.verticalSlider_7.setProperty("value", 90)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName(_fromUtf8("verticalSlider_7"))
        self.horizontalSlider_3 = QtGui.QSlider(self.frame_4)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(280, 100, 71, 21))
        self.horizontalSlider_3.setMaximum(180)
        self.horizontalSlider_3.setProperty("value", 90)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.horizontalSlider_4 = QtGui.QSlider(self.frame_4)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(210, 210, 141, 31))
        self.horizontalSlider_4.setMaximum(359)
        self.horizontalSlider_4.setProperty("value", 180)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName(_fromUtf8("horizontalSlider_4"))
        self.frame_10 = QtGui.QFrame(self.frame_4)
        self.frame_10.setGeometry(QtCore.QRect(0, -10, 181, 261))
        self.frame_10.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_10.setObjectName(_fromUtf8("frame_10"))
        self.label_11 = QtGui.QLabel(self.frame_10)
        self.label_11.setGeometry(QtCore.QRect(0, 10, 171, 251))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("rightHand.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.frame_11 = QtGui.QFrame(self.frame_10)
        self.frame_11.setGeometry(QtCore.QRect(0, 0, 181, 146))
        self.frame_11.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_11.setObjectName(_fromUtf8("frame_11"))
        self.spinBox_11 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_11.setGeometry(QtCore.QRect(130, 90, 46, 26))
        self.spinBox_11.setProperty("value", 99)
        self.spinBox_11.setObjectName(_fromUtf8("spinBox_11"))
        self.spinBox_12 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_12.setGeometry(QtCore.QRect(125, 51, 46, 26))
        self.spinBox_12.setProperty("value", 99)
        self.spinBox_12.setObjectName(_fromUtf8("spinBox_12"))
        self.spinBox_13 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_13.setGeometry(QtCore.QRect(100, 16, 46, 21))
        self.spinBox_13.setProperty("value", 99)
        self.spinBox_13.setObjectName(_fromUtf8("spinBox_13"))
        self.spinBox_14 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_14.setGeometry(QtCore.QRect(30, 30, 46, 27))
        self.spinBox_14.setProperty("value", 99)
        self.spinBox_14.setObjectName(_fromUtf8("spinBox_14"))
        self.spinBox_15 = QtGui.QSpinBox(self.frame_11)
        self.spinBox_15.setGeometry(QtCore.QRect(5, 85, 46, 27))
        self.spinBox_15.setProperty("value", 99)
        self.spinBox_15.setObjectName(_fromUtf8("spinBox_15"))
        self.spinBox_10 = QtGui.QSpinBox(self.frame_10)
        self.spinBox_10.setGeometry(QtCore.QRect(50, 165, 56, 27))
        self.spinBox_10.setProperty("value", 99)
        self.spinBox_10.setObjectName(_fromUtf8("spinBox_10"))
        self.frame_3 = QtGui.QFrame(self.frame_5)
        self.frame_3.setGeometry(QtCore.QRect(5, 0, 361, 251))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_12 = QtGui.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(180, 0, 176, 241))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8("roboticArm.jpg")))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalSlider_2 = QtGui.QSlider(self.frame_3)
        self.verticalSlider_2.setGeometry(QtCore.QRect(235, 130, 29, 81))
        self.verticalSlider_2.setMaximum(180)
        self.verticalSlider_2.setProperty("value", 90)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName(_fromUtf8("verticalSlider_2"))
        self.verticalSlider_3 = QtGui.QSlider(self.frame_3)
        self.verticalSlider_3.setGeometry(QtCore.QRect(210, 20, 31, 81))
        self.verticalSlider_3.setMaximum(180)
        self.verticalSlider_3.setProperty("value", 90)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName(_fromUtf8("verticalSlider_3"))
        self.verticalSlider_4 = QtGui.QSlider(self.frame_3)
        self.verticalSlider_4.setGeometry(QtCore.QRect(305, 5, 31, 81))
        self.verticalSlider_4.setMaximum(180)
        self.verticalSlider_4.setProperty("value", 90)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName(_fromUtf8("verticalSlider_4"))
        self.horizontalSlider_2 = QtGui.QSlider(self.frame_3)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(280, 110, 71, 31))
        self.horizontalSlider_2.setMaximum(180)
        self.horizontalSlider_2.setProperty("value", 90)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalSlider = QtGui.QSlider(self.frame_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(215, 210, 121, 29))
        self.horizontalSlider.setMaximum(359)
        self.horizontalSlider.setProperty("value", 180)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.frame_9 = QtGui.QFrame(self.frame_3)
        self.frame_9.setGeometry(QtCore.QRect(0, 0, 181, 251))
        self.frame_9.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_9.setObjectName(_fromUtf8("frame_9"))
        self.label_10 = QtGui.QLabel(self.frame_9)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 171, 251))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet(_fromUtf8(""))
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8("leftHand.png")))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.frame_12 = QtGui.QFrame(self.frame_9)
        self.frame_12.setGeometry(QtCore.QRect(0, 0, 196, 141))
        self.frame_12.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_12.setObjectName(_fromUtf8("frame_12"))
        self.spinBox_5 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_5.setGeometry(QtCore.QRect(5, 90, 46, 27))
        self.spinBox_5.setProperty("value", 99)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.spinBox_6 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_6.setGeometry(QtCore.QRect(10, 40, 46, 27))
        self.spinBox_6.setProperty("value", 99)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.spinBox_7 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_7.setGeometry(QtCore.QRect(45, 5, 46, 26))
        self.spinBox_7.setProperty("value", 99)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.spinBox_8 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_8.setGeometry(QtCore.QRect(95, 20, 46, 27))
        self.spinBox_8.setProperty("value", 99)
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.spinBox_9 = QtGui.QSpinBox(self.frame_12)
        self.spinBox_9.setGeometry(QtCore.QRect(130, 70, 46, 27))
        self.spinBox_9.setProperty("value", 99)
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))
        self.spinBox_4 = QtGui.QSpinBox(self.frame_9)
        self.spinBox_4.setGeometry(QtCore.QRect(80, 160, 60, 27))
        self.spinBox_4.setProperty("value", 99)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1280, 0, 86, 481))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalSlider = QtGui.QSlider(self.groupBox_4)
        self.verticalSlider.setGeometry(QtCore.QRect(40, 200, 31, 136))
        self.verticalSlider.setMaximum(180)
        self.verticalSlider.setProperty("value", 90)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.verticalSlider.setTickInterval(25)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.pushButton_9 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(0, 115, 86, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 140, 86, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(0, 331, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(0, 160, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_30 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_30.setGeometry(QtCore.QRect(0, 180, 86, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName(_fromUtf8("pushButton_30"))
        self.verticalSlider_8 = QtGui.QSlider(self.groupBox_4)
        self.verticalSlider_8.setGeometry(QtCore.QRect(10, 200, 21, 136))
        self.verticalSlider_8.setMaximum(180)
        self.verticalSlider_8.setProperty("value", 90)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName(_fromUtf8("verticalSlider_8"))
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_3.setGeometry(QtCore.QRect(45, 15, 41, 21))
        self.spinBox_3.setMaximum(1)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(5, 20, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalSlider_9 = QtGui.QSlider(self.groupBox_4)
        self.verticalSlider_9.setGeometry(QtCore.QRect(30, 355, 31, 111))
        self.verticalSlider_9.setMaximum(360)
        self.verticalSlider_9.setProperty("value", 180)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName(_fromUtf8("verticalSlider_9"))
        self.label_4 = QtGui.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(40, 331, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_18 = QtGui.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(30, 460, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pushButton_18 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_18.setGeometry(QtCore.QRect(0, 40, 83, 24))
        self.pushButton_18.setObjectName(_fromUtf8("pushButton_18"))
        self.pushButton_19 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_19.setGeometry(QtCore.QRect(0, 70, 83, 24))
        self.pushButton_19.setObjectName(_fromUtf8("pushButton_19"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setGeometry(QtCore.QRect(235, 485, 401, 141))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 30, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 151, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame = QtGui.QFrame(self.groupBox_3)
        self.frame.setGeometry(QtCore.QRect(0, 110, 391, 26))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.radioButton_4 = QtGui.QRadioButton(self.frame)
        self.radioButton_4.setGeometry(QtCore.QRect(160, 1, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(65, 0, 91, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton_11 = QtGui.QPushButton(self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 0, 51, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.pushButton_14 = QtGui.QPushButton(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(280, 0, 51, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.checkBox_3 = QtGui.QCheckBox(self.frame)
        self.checkBox_3.setGeometry(QtCore.QRect(5, 5, 56, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.pushButton_15 = QtGui.QPushButton(self.frame)
        self.pushButton_15.setGeometry(QtCore.QRect(340, 0, 51, 26))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.frame_7 = QtGui.QFrame(self.groupBox_3)
        self.frame_7.setGeometry(QtCore.QRect(0, 70, 391, 41))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.pushButton_13 = QtGui.QPushButton(self.frame_7)
        self.pushButton_13.setGeometry(QtCore.QRect(175, 0, 86, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.pushButton_12 = QtGui.QPushButton(self.frame_7)
        self.pushButton_12.setGeometry(QtCore.QRect(85, 0, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.pushButton_31 = QtGui.QPushButton(self.frame_7)
        self.pushButton_31.setGeometry(QtCore.QRect(270, 0, 86, 21))
        self.pushButton_31.setObjectName(_fromUtf8("pushButton_31"))
        self.label_5 = QtGui.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(5, 25, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBox = QtGui.QCheckBox(self.frame_7)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(5, 5, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.frame_8 = QtGui.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(0, 640, 631, 91))
        self.frame_8.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_8.setObjectName(_fromUtf8("frame_8"))
        self.comboBox_2 = QtGui.QComboBox(self.frame_8)
        self.comboBox_2.setGeometry(QtCore.QRect(0, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.setItemText(10, _fromUtf8(""))
        self.comboBox = QtGui.QComboBox(self.frame_8)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(0, 10, 141, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(self.frame_8)
        self.groupBox.setGeometry(QtCore.QRect(150, 0, 231, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 20, 66, 31))
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 50, 61, 31))
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(0, 50, 66, 31))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(135, 50, 61, 31))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalSlider_11 = QtGui.QSlider(self.groupBox)
        self.verticalSlider_11.setGeometry(QtCore.QRect(200, 10, 21, 71))
        self.verticalSlider_11.setProperty("value", 50)
        self.verticalSlider_11.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_11.setObjectName(_fromUtf8("verticalSlider_11"))
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(170, 20, 31, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.pushButton_21 = QtGui.QPushButton(self.frame_8)
        self.pushButton_21.setGeometry(QtCore.QRect(30, 63, 83, 21))
        self.pushButton_21.setObjectName(_fromUtf8("pushButton_21"))
        self.groupBox_6 = QtGui.QGroupBox(self.frame_8)
        self.groupBox_6.setGeometry(QtCore.QRect(390, 0, 231, 91))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalSlider_10 = QtGui.QSlider(self.groupBox_6)
        self.verticalSlider_10.setGeometry(QtCore.QRect(200, 10, 21, 71))
        self.verticalSlider_10.setProperty("value", 50)
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName(_fromUtf8("verticalSlider_10"))
        self.label_19 = QtGui.QLabel(self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(160, 20, 31, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 20, 66, 31))
        self.pushButton_5.setCheckable(False)
        self.pushButton_5.setChecked(False)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_8 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 50, 66, 31))
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_7 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 50, 66, 31))
        self.pushButton_7.setCheckable(False)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_6.setGeometry(QtCore.QRect(65, 50, 66, 31))
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1375, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuRobot_type = QtGui.QMenu(self.menuSettings)
        self.menuRobot_type.setObjectName(_fromUtf8("menuRobot_type"))
        self.menuAudio = QtGui.QMenu(self.menuSettings)
        self.menuAudio.setObjectName(_fromUtf8("menuAudio"))
        self.menuAdd_robotic_hand = QtGui.QMenu(self.menuSettings)
        self.menuAdd_robotic_hand.setObjectName(_fromUtf8("menuAdd_robotic_hand"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuadcopter = QtGui.QAction(MainWindow)
        self.actionQuadcopter.setObjectName(_fromUtf8("actionQuadcopter"))
        self.actionTank = QtGui.QAction(MainWindow)
        self.actionTank.setObjectName(_fromUtf8("actionTank"))
        self.actionCar = QtGui.QAction(MainWindow)
        self.actionCar.setObjectName(_fromUtf8("actionCar"))
        self.actionBoat = QtGui.QAction(MainWindow)
        self.actionBoat.setObjectName(_fromUtf8("actionBoat"))
        self.actionWorkspace = QtGui.QAction(MainWindow)
        self.actionWorkspace.setObjectName(_fromUtf8("actionWorkspace"))
        self.actionLanguage = QtGui.QAction(MainWindow)
        self.actionLanguage.setObjectName(_fromUtf8("actionLanguage"))
        self.actionLoop_settings = QtGui.QAction(MainWindow)
        self.actionLoop_settings.setObjectName(_fromUtf8("actionLoop_settings"))
        self.actionVolume = QtGui.QAction(MainWindow)
        self.actionVolume.setObjectName(_fromUtf8("actionVolume"))
        self.actionRight = QtGui.QAction(MainWindow)
        self.actionRight.setObjectName(_fromUtf8("actionRight"))
        self.actionLeft = QtGui.QAction(MainWindow)
        self.actionLeft.setObjectName(_fromUtf8("actionLeft"))
        self.actionTurn_Server_Off = QtGui.QAction(MainWindow)
        self.actionTurn_Server_Off.setObjectName(_fromUtf8("actionTurn_Server_Off"))
        self.menuRobot_type.addAction(self.actionQuadcopter)
        self.menuRobot_type.addAction(self.actionTank)
        self.menuRobot_type.addAction(self.actionCar)
        self.menuRobot_type.addAction(self.actionBoat)
        self.menuAudio.addSeparator()
        self.menuAudio.addAction(self.actionLoop_settings)
        self.menuAudio.addAction(self.actionVolume)
        self.menuAdd_robotic_hand.addAction(self.actionRight)
        self.menuAdd_robotic_hand.addAction(self.actionLeft)
        self.menuSettings.addAction(self.menuRobot_type.menuAction())
        self.menuSettings.addAction(self.actionWorkspace)
        self.menuSettings.addAction(self.actionLanguage)
        self.menuSettings.addAction(self.menuAudio.menuAction())
        self.menuSettings.addAction(self.menuAdd_robotic_hand.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "RoboClient", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Sensors", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Robot", None))
        self.label_7.setText(_translate("MainWindow", "Host ip:", None))
        self.lineEdit.setText(_translate("MainWindow", "127.0.0.1", None))
        self.label_8.setText(_translate("MainWindow", "Port:", None))
        self.pushButton_16.setText(_translate("MainWindow", "Connect", None))
        self.pushButton_17.setText(_translate("MainWindow", "Disconnect", None))
        self.label_6.setText(_translate("MainWindow", "Password:", None))
        self.pushButton_20.setText(_translate("MainWindow", "Server Off", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Camera ", None))
        self.pushButton_9.setText(_translate("MainWindow", "Start recording", None))
        self.pushButton_10.setText(_translate("MainWindow", "Stop recording", None))
        self.label_3.setText(_translate("MainWindow", " X angle", None))
        self.label.setText(_translate("MainWindow", "0 [s]", None))
        self.pushButton_30.setText(_translate("MainWindow", "Save", None))
        self.label_17.setText(_translate("MainWindow", "Index", None))
        self.label_4.setText(_translate("MainWindow", " Y angle", None))
        self.label_18.setText(_translate("MainWindow", "Z angle", None))
        self.pushButton_18.setText(_translate("MainWindow", "Stream ON", None))
        self.pushButton_19.setText(_translate("MainWindow", "Stream OFF", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Audio", None))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Test audo message", None))
        self.label_2.setText(_translate("MainWindow", "Language: en", None))
        self.radioButton_4.setText(_translate("MainWindow", "File", None))
        self.radioButton_2.setText(_translate("MainWindow", "Microphone", None))
        self.pushButton_11.setText(_translate("MainWindow", "Play", None))
        self.pushButton_14.setText(_translate("MainWindow", "Stop", None))
        self.checkBox_3.setText(_translate("MainWindow", "Loop", None))
        self.pushButton_15.setText(_translate("MainWindow", "...", None))
        self.pushButton_13.setText(_translate("MainWindow", "Stop recording", None))
        self.pushButton_12.setText(_translate("MainWindow", "Start recording", None))
        self.pushButton_31.setText(_translate("MainWindow", "Save", None))
        self.label_5.setText(_translate("MainWindow", "0 [s]", None))
        self.checkBox.setText(_translate("MainWindow", "Listen", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Keyboard", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "None", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "PS2 Pad", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "JSK420 Joystick", None))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Kinect + PS2 Pad", None))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Kinect + Joystick", None))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Kinect + Keyboard", None))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Camera + PS2 Pad", None))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Camera + Joystick", None))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Camera + Keyboard", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "other", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "manipulator", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "UAV", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "tank", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "car", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "boat", None))
        self.groupBox.setTitle(_translate("MainWindow", "Throttle, Yaw", None))
        self.pushButton_3.setText(_translate("MainWindow", "i", None))
        self.pushButton_4.setText(_translate("MainWindow", "k", None))
        self.pushButton.setText(_translate("MainWindow", "j", None))
        self.pushButton_2.setText(_translate("MainWindow", "l", None))
        self.label_20.setText(_translate("MainWindow", " PID", None))
        self.pushButton_21.setText(_translate("MainWindow", "Apply", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Pich, Roll", None))
        self.label_19.setText(_translate("MainWindow", " PID", None))
        self.pushButton_5.setText(_translate("MainWindow", "w", None))
        self.pushButton_8.setText(_translate("MainWindow", "d", None))
        self.pushButton_7.setText(_translate("MainWindow", "a", None))
        self.pushButton_6.setText(_translate("MainWindow", "s", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuRobot_type.setTitle(_translate("MainWindow", "Robot type", None))
        self.menuAudio.setTitle(_translate("MainWindow", "Audio", None))
        self.menuAdd_robotic_hand.setTitle(_translate("MainWindow", "Add robotic hand", None))
        self.actionQuadcopter.setText(_translate("MainWindow", "UAV", None))
        self.actionTank.setText(_translate("MainWindow", "tank", None))
        self.actionCar.setText(_translate("MainWindow", "car", None))
        self.actionBoat.setText(_translate("MainWindow", "boat", None))
        self.actionWorkspace.setText(_translate("MainWindow", "Workspace", None))
        self.actionLanguage.setText(_translate("MainWindow", "Language", None))
        self.actionLoop_settings.setText(_translate("MainWindow", "Loop settings", None))
        self.actionVolume.setText(_translate("MainWindow", "Volume", None))
        self.actionRight.setText(_translate("MainWindow", "Right", None))
        self.actionLeft.setText(_translate("MainWindow", "Left", None))
        self.actionTurn_Server_Off.setText(_translate("MainWindow", "Turn Server Off", None))

