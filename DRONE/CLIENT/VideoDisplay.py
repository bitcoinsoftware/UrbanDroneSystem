import cv2, threading, socket, numpy
from PyQt4.QtGui import QImage, QPixmap
from PyQt4 import QtCore

__author__ = 'noname'
class VideoDisplay(threading.Thread):
    def __init__(self, ui, cameraIndex):
        threading.Thread.__init__(self)
        self.ui = ui
        self.allowRun = False
        self.cameraIndex = cameraIndex

    def run(self):
        self.allowRun = True
        self.videoConn, self.videoAddr = self.videoSocket.accept()
        while self.allowRun:
            length = self.recvall(self.videoConn,16)
            if length != None:
                stringData = self.recvall(self.videoConn, int(length))
                data = numpy.fromstring(stringData, dtype='uint8')
                decimg=cv2.imdecode(data,cv2.CV_LOAD_IMAGE_UNCHANGED)
                cvRGBImg = cv2.cvtColor(decimg, cv2.cv.CV_BGR2RGB)
                qimg = QImage(cvRGBImg.data,cvRGBImg.shape[1], cvRGBImg.shape[0], QImage.Format_RGB888)
                self.ui.object.emit(QtCore.SIGNAL("displayImage(PyQt_PyObject, int)"), QPixmap.fromImage(qimg), self.cameraIndex)

        self.videoSocket.close()
        self.videoConn.close()

    def startVideoConnection(self, videoPort):
        self.videoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.videoSocket.bind(('', videoPort))
        self.videoSocket.listen(True)

    def stopVideoConnection(self):
        self.allowRun= False

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf