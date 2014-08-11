import telnetlib, sys, os, pygame, socket, numpy, cv2

class DroneClient:

    def __init__(self, ip, port, videoPort):
        self.ip, self.port = ip, port
        print ip, port
        self.tn=telnetlib.Telnet(ip, port)
        self.neutral=[5,5,5,5,0]
        self.speed=1
        
        self.videoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.videoSocket.bind(('127.0.0.1', videoPort))
        self.videoSocket.listen(True)
        self.videoConn, self.videoAddr = self.videoSocket.accept()

    def steer(self, params):
        params=''.join([str(x) for x in params]) 
        self.tn.write(params)
        
    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    def steering(self):
        pygame.init()
        clock = pygame.time.Clock()
        W, H = 640, 480
        screen = pygame.display.set_mode((W, H))
        image=pygame.image.load("videoIcon.png")
        screen.blit(image,(0,0)) # "show image" on the screen
        pygame.display.update()
        
        running = True
        result=self.neutral[:]
        while running:
            #image = self.getVideoData()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYUP:
                    result=self.neutral[:]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        result="EXIT"
                    # takeoff / land
                    elif event.key == pygame.K_RETURN:
                        result[4]=1
                    elif event.key == pygame.K_SPACE:
                        result[4]=0
                    # emergency
                    elif event.key == pygame.K_BACKSPACE:
                        print("TODO Emergency Reset")
                    # forward / backward
                    elif event.key == pygame.K_w:
                        result[1]=self.neutral[1]+self.speed
                    elif event.key == pygame.K_s:
                        result[1]=self.neutral[1]-self.speed
                    # left / right
                    elif event.key == pygame.K_a:
                        result[2]=self.neutral[2]-self.speed
                    elif event.key == pygame.K_d:
                        result[2]=self.neutral[2]+self.speed
                    # up / down
                    elif event.key == pygame.K_UP:
                        result[3] =self.neutral[3]+self.speed
                    elif event.key == pygame.K_DOWN:
                        result[3] =self.neutral[3]-self.speed
                    # turn left / turn right
                    elif event.key == pygame.K_LEFT:
                        result[0] =self.neutral[0]-self.speed
                    elif event.key == pygame.K_RIGHT:
                        result[0] =self.neutral[0]+self.speed
                    
                    # speed
                    elif event.key == pygame.K_1:
                        self.speed = 1
                    elif event.key == pygame.K_2:
                        self.speed = 2
                    elif event.key == pygame.K_3:
                        self.speed = 3
                    elif event.key == pygame.K_4:
                        self.speed = 4
                        
                    #optical processes:
                    elif event.key ==pygame.K_f:
                        result="FOLLOWLINE"
                    elif event.key ==pygame.K_o:
                        result="OPTICALFLOWSTABILISATION"
                    elif event.key ==pygame.K_b:
                        result="BLUETOOTHLANDINGMODE"
                    elif event.key ==pygame.K_p:
                        result="PRINTRESULTS"
                    elif event.key ==pygame.K_g:
                        result="GRAPHICAL"
                        
                    self.steer(result)
            
            
            length = self.recvall(self.videoConn,16)
            if length == None:
                break
            stringData = self.recvall(self.videoConn, int(length))
            data = numpy.fromstring(stringData, dtype='uint8')
            decimg=cv2.imdecode(data,1)
            frame2=cv2.cvtColor(decimg,cv2.COLOR_BGR2RGB)
            frame2=numpy.rot90(frame2)
            surface=pygame.surfarray.make_surface(frame2)
            

            screen.blit(surface,(0,0))
            pygame.display.update()
            serverResponse = self.tn.read_eager()
            if(serverResponse):
                print serverResponse
            pygame.display.flip()
            clock.tick(50)
            pygame.display.set_caption("FPS: %.2f" % clock.get_fps())
