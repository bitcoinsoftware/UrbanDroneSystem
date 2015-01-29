__author__ = 'user'
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyCentralWidget(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)

    def event(self, event):
        if (event.type()==QEvent.KeyPress):
            key = event.key()
            if   key==65:
                self.emit(SIGNAL("a"))
            elif key==83:
                self.emit(SIGNAL("s"))
            elif key==68:
                self.emit(SIGNAL("d"))
            elif key==87:
                self.emit(SIGNAL("w"))

            elif key==73:
                self.emit(SIGNAL("i"))
            elif key==74:
                self.emit(SIGNAL("j"))
            elif key==75:
                self.emit(SIGNAL("k"))
            elif key==76:
                self.emit(SIGNAL("l"))
            #a65,s83,d68,w87,   i73,j74,k75,l76
            return True

        return QWidget.event(self, event)