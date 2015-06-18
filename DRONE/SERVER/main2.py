import socket, select, threading, cv2, serial, argparse,  numpy, ast
import ConfigFile

SERIAL = "/dev/ttyACM99"

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--videosource", type=str, help="proccess a video source")
    parser.add_argument("--videoport", type=int, help="video transmition port")
    parser.add_argument("-g", "--graphical", help="display video", action="store_true")
    parser.add_argument("-p", "--port", type=int, help="port number")
    args = parser.parse_args()

try:
    ser = serial.Serial(SERIAL, 9600, timeout=1)
except:
    print("Could not open serial "+SERIAL);
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', ConfigFile.config['port']))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()

runServer = True

class CameraThread(threading.Thread):
    def __init__(self, (address, videoPort) , cameraIndex):
        threading.Thread.__init__(self)
        self.videoSock = socket.socket()
        self.videoSock.connect((address, videoPort))
        self.videocapture = cv2.VideoCapture(cameraIndex)
        self.loopRun = True

    def run(self):
        self.encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),70]
        while self.loopRun:
            if self.videocapture!=None: # sending image to client
                rval, frame = self.videocapture.read()
                result, imgencode = cv2.imencode('.jpg', frame, self.encode_param)
                picture = numpy.array(imgencode)
                stringData = picture.tostring()
                if self.videoSock!=None:
                    self.videoSock.send( str(len(stringData)).ljust(16))
                    self.videoSock.send( stringData )
        self.videoSock.close()
        self.videocapture.release()
        self.videoSock, self.videocapture = None, None
        self.confirmationSocket.send('True')

    def stopStream(self, confirmationSocket):
        self.confirmationSocket = confirmationSocket
        self.loopRun = False

class DroneServer(threading.Thread):
    def __init__(self, (sock,address)):
        threading.Thread.__init__(self)
        self.socket = sock
        self.socket.settimeout(0.001)
        self.address= address

    def run(self):
        global runServer
        lock.acquire()
        clients.append(self)
        lock.release()
        print '%s:%s connected.' % self.address
        #streamRequested = False
        streamRequested = [False, False]  # 2 cameras
        #cameraThread = None
        cameraThreads = [None, None]
        while runServer:
            ready = select.select([self.socket], [], [], 0.0001)
            if ready[0]:
                recData = self.socket.recv(1024).lstrip()
                if recData: #check if data has some non white spaces
                    jsonData = ast.literal_eval(recData)
                    print "RECEIVED: ", jsonData
                    request = jsonData['request']
                    requestArgument = jsonData['argument']
                    if request=='connect':
                        self.socket.send(str(ConfigFile.config))
                    if request=='startStream' or request=='connectVideo' or request=='stopStream':
                        cameraNumber = requestArgument

                        if (request=='startStream' and streamRequested[cameraNumber]==False) or (request=='connectVideo' and streamRequested[cameraNumber]==True):
                            self.socket.send(str(ConfigFile.config['videoAvailable']))
                            streamRequested[cameraNumber] = True
                            if ConfigFile.config['videoAvailable']:
                                if request=='connectVideo':
                                    cameraThreads[cameraNumber]= CameraThread((self.address[0], ConfigFile.config['cameraParams'][cameraNumber]['videoPort']) , ConfigFile.config['cameraParams'][cameraNumber]['cameraIndex'])
                                    cameraThreads[cameraNumber].start()
                                    #cameraThread = CameraThread((self.address[0], ConfigFile.config['cameraParams'][cameraNumber]['videoPort']) , ConfigFile.config['cameraParams'][cameraNumber]['cameraIndex'])
                                    #cameraThread.start()
                                    ConfigFile.config['cameraParams'][cameraNumber]['taken'] = True
                        elif request=='stopStream' and streamRequested[cameraNumber] == True: #stop video stream
                            streamRequested[cameraNumber] = False
                            cameraThreads[cameraNumber].stopStream(self.socket)
                            #cameraThread.stopStream(self.socket)

                    elif request=='move':
                        #self.socket.send('True')
                        pass

                    elif request=='disconnect': #disconnect telnet client
                        self.socket.send('True')
                        print '%s:%s disconnected.' % self.address

                    elif request=='stopServer':
                        for cameraNumber in range(len(cameraThreads)):
                            if streamRequested[cameraNumber] == True:
                                cameraThreads[cameraNumber].stopStream(self.socket)
                                streamRequested[cameraNumber] = False
                        runServer = False

        lock.acquire()
        clients.remove(self)
        lock.release()
        
if __name__ == '__main__':
    while runServer: # wait for socket to connect
        # send socket to chatserver and start monitoring
        DroneServer(s.accept()).start()