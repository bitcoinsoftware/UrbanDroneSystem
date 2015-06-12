import telnetlib, sys, os, ast, threading, socket, numpy, cv2, select

class Client:

    def __init__(self, ip, port,param):
        self.ip, self.port = ip, port
        print ip, port
        print param
        self.stub, data = False, None
        if param == "--stub":
            self.stub = True
        if not self.stub:
            print "probuje sie polaczyc przez ", (ip, port)
            self.tn=telnetlib.Telnet(ip, port)
            data = self.request('connect')
            #TODO dodac wyjatek jak sie nie uda polaczyc z serwerem
        else:
            response = "{'serverType':'tank', 'videoAvailable':True," \
                       " 'cameraParams':[{'xAxisAvailable':True, 'yAxisAvailable':True, 'zAxisAvailable':False}" \
                       ",{'xAxisAvailable':False, 'yAxisAvailable':False, 'zAxisAvailable':False}],  'videoPort':696969, " \
                       "'audioAvailable':True, 'microphoneAvailable':True, 'speakerAvailable':True, 'leftRoboticArmAvailable':False, " \
                       "'leftRoboticFingersAvailable':False, 'rightRoboticArmAvailable':True, 'rightRoboticFingersAvailable':True, " \
                       "'sensorList':{'temperature':30, 'methan':0.1}}"
        if data is not None:
            self.features=data


    def request(self, methodName, args ={'argument':None}, waitForConfiramtion = True):
        msgDict = {'request':methodName}
        msgDict.update(args)
        self.tn.write(str(msgDict))
        data = None
        if waitForConfiramtion:
            while not data:
                data = self.tn.read_until("\n",timeout=1)
            print ">",data,"<"
            data = ast.literal_eval(data)
        return data

    def end(self):
        self.request('disconnect')
        self.tn.close()

    """
    def steering(self):
        running = True
        while running:
            length = self.recvall(self.videoConn,16)
            if length == None:
                break
            stringData = self.recvall(self.videoConn, int(length))
            data = numpy.fromstring(stringData, dtype='uint8')
            decimg=cv2.imdecode(data,cv2.CV_LOAD_IMAGE_UNCHANGED)
            cv2.imshow('frame',decimg)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def steer(self,action, params):
        if self.stub:
            pass
        else:
            #params=''.join([str(x) for x in params])
            #TODO
            self.tn.write(params)
        print "Client order: ", {'action':action, 'params':params}

    """