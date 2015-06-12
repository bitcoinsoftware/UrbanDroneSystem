import argparse, DroneClient
from gui import *
from Connections import *

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    if len(sys.argv)> 1:
        connect(ui, sys.argv[1])
    else:
        connect(ui)
    MainWindow.show()
    sys.exit(app.exec_())
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--host", type=str, help="server host ip address")
    parser.add_argument("-p", "--port", type=int, help="port number")
    parser.add_argument("--videoport", type=int, help="video port number")
    args = parser.parse_args()
    a = DroneClient.DroneClient(args.host, args.port, args.videoport)
    a.steering()
    """
