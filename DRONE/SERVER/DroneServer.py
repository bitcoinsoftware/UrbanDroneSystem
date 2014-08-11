import socket, threading, cv2, serial, multiprocessing

class DroneServer(threading.Thread):
    def __init__(self, (socket,address), videoSource):
        threading.Thread.__init__(self)
        self.clients = [] #list of clients connected
        self.lock = threading.Lock()
        self.socket = socket
        self.address= address
        self.videoSource=videoSource
        self.videoProcessor =None
        self.followLine = None
        self.opticalFlow= None
        self.bluetoothLandingMode = None

    def run(self):
        self.lock.acquire()
        self.clients.append(self)
        self.lock.release()
        print '%s:%s connected.' % self.address
        self.vc = cv2.VideoCapture(self.videoSource)
        
        if self.vc.isOpened(): # try to get the first frame
            self.rval, self.frame = self.vc.read()
            self.h,self.w = self.frame.shape[:2]
        
        while True:
            data = self.socket.recv(1024)
            
            if data=="VIDEO":
                self.videocapture = cv2.VideoCapture(self.videoSource)
                print videocapture.isOpened()
                """
                if self.videoProcessor==None:
                    self.videoProcess = multiprocessing.Process(target=self.startVideoProcessor)
                    self.videoProcess.start()
                else:
                    self.videoProcessor.turnOff()
                    self.videoProcessor=None
                    """
            elif  self.videoProcessor!=None:
                if data=="FOLLOWLINE":
                    if self.followLine==None:
                        self.videoProcessor.turnLineFollowerOn(scale=1)
                    else:
                        self.videoProcessor.flags["l"]=0
                if data=="OPTICALFLOWSTABILISATION":
                    if self.opticalFlow==None:
                        self.videoProcessor.turnOpticalFlowOn(scale=1)
                    else:
                        self.videoProcessor.flags["o"]=0
                if data=="BLUETOOTHLANDINGMODE":
                    if self.bluetoothLandingMode==None:
                        self.bluetoothLandingMode="WLACZAM BLUETOOTH LANDING"
                    else:
                        self.bluetoothLandingMode="WYLACZAM BLUETOOTH LANDING"
            print data
            
            if not data:
                break
            for c in self.clients:
                c.socket.send(data)
                try:
                    ser.write(data)
                except:
                    print("Could not write to serial ")
                print data
        self.socket.close()
        print '%s:%s disconnected.' % self.address
        self.lock.acquire()
        self.clients.remove(self)
        self.lock.release()
        
    def startVideoProcessor(self):
        self.videoProcessor=VideoProcessor.VideoProcessor(self.videoSource)
        self.videoProcessor.run()
        
