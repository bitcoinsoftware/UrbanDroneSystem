import socket, select, time, threading, cv2, serial, argparse, multiprocessing, numpy
import OpticalFlow
import LineFollower
import WifiPower
import HoughCircles

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
s.bind(('', args.port))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()

runServer = True

class DroneServer(threading.Thread):
    def __init__(self, (sock,address), videoIndex, videoPort):
        threading.Thread.__init__(self)
        self.socket = sock
        self.socket.settimeout(0.001)
        self.address= address
        print address
        self.flags={}
        self.flags['opticalFlow'], self.flags['followLine'], self.flags['printResults']= None, None, None
        self.flags['bluetoothLandingMode'], self.flags['followLineRunning'], self.flags['displayImage']=None, None, None
        self.flags['markerlanding']= None

        self.videoIndex = int(videoIndex)
        self.videoSock = socket.socket()
        #self.videoSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.videoSock.connect(('127.0.0.1', int(videoPort)))
        self.videoSock.connect((address[0], int(videoPort)))
        self.encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),70]

    def run(self):
        global runServer
        lock.acquire()
        clients.append(self)
        lock.release()
        print '%s:%s connected.' % self.address
        
        videocapture = cv2.VideoCapture(self.videoIndex)
        if videocapture.isOpened():
            rval, prevFrame = videocapture.read()
            h,w = prevFrame.shape[:2]
            ofPrevPreparedFrame = None
            of= OpticalFlow.OpticalFlow(h,w,1)
            
            lf= LineFollower.LineFollower(h,w,0.5)
            
            wp = WifiPower.WifiPower('wlan0')
            hc = HoughCircles.HoughCircles(h,w,0.7)
            availableCommands = ['EXIT', 'FOLLOWLINE', 'OPTICALFLOWSTABILISATION', 'BLUETOOTHLANDINGMODE', 
                                    'PRINTRESULTS','GRAPHICAL', 'MARKERLANDINGMODE', None]
            while True:
                rval, frame = videocapture.read()
                ready = select.select([self.socket], [], [], 0.0001)
                if ready[0]:
                    data = self.socket.recv(1024)
                else:
                    data=None
                if data=="EXIT":
                    break
                #if data=="STOPSERVER":
                #    runServer=None
                #    break
                elif data=="FOLLOWLINE":
                    if self.flags['followLine']==None:
                        self.flags['followLine']=True
                    else:
                        self.flags['followLine']=None
                elif data=="OPTICALFLOWSTABILISATION":
                    if self.flags['opticalFlow']==None:
                        self.flags['opticalFlow']=True
                    else:
                        self.flags['opticalFlow']=None
                elif data=="BLUETOOTHLANDINGMODE":
                    if self.flags['bluetoothLandingMode']==None:
                        self.flags['bluetoothLandingMode']=True
                    else:
                        self.flags['bluetoothLandingMode']=None  
                elif data=="PRINTRESULTS":
                    if self.flags['printResults']==None:
                        self.flags['printResults']=True
                    else:
                        self.flags['printResults']=None
                elif data=="GRAPHICAL":
                    if self.flags['displayImage']==None:
                        self.flags['displayImage']=True
                    else:
                        self.flags['displayImage']=None
                elif data=="MARKERLANDINGMODE":
                    if self.flags['markerlanding']==None:
                        self.flags['markerlanding']=True
                    else:
                        self.flags['markerlanding']=None

                if self.flags['followLine']==True:
                    # sending an argument to the line analysis process
                    lfResult = lf.process_frame(frame)
                    data = lf.getDirections(lfResult)
                    if self.flags['bluetoothLandingMode']==True:
                        if wp.isCloseToAP() and hc.findCircles(frame)!=None: #when wifi is strong , stop searching for the line and start looking for the platform
                            self.flags['followLine']=None
                elif self.flags['bluetoothLandingMode']==True and self.flags['followLine']==None: #start landing
                    circles = hc.findCircles(frame)
                    data = hc.getDirections(circles)
                elif self.flags['markerlanding']==True:
                    circles = hc.findCircles(frame)
                    data = hc.getDirections(circles)
                    
                if self.flags['opticalFlow']==True and data==None:
                    ofPreparedFrame = of.ofFramePrepare(frame.copy(), prevFrame)
                    if ofPrevPreparedFrame != None:
                        ofResults = of.countOF(ofPreparedFrame, ofPrevPreparedFrame)
                        if self.flags['printResults'] and ofResults:
                            self.socket.send("totOFx:{0},totOFy:{1},rotOF:{2}".format(ofResults[2], ofResults[3], ofResults[5]))
                            data = of.getDirections()
                    prevFrame, ofPrevPreparedFrame =frame, ofPreparedFrame
                
                if True:
                    result, imgencode = cv2.imencode('.jpg', frame, self.encode_param)
                    picture = numpy.array(imgencode)
                    stringData = picture.tostring()
                    self.videoSock.send( str(len(stringData)).ljust(16));
                    self.videoSock.send( stringData );
                
                if data not in availableCommands:
                    try:
                        ser.write(data)
                    except:
                        pass
                    print data
        print "CLOSED"
        self.socket.close()
        self.videoSock.close()
        print '%s:%s disconnected.' % self.address
        lock.acquire()
        clients.remove(self)
        lock.release()
        
if __name__ == '__main__':
    while runServer!=None: # wait for socket to connect
        # send socket to chatserver and start monitoring
        DroneServer(s.accept(), args.videosource, args.videoport).start()
