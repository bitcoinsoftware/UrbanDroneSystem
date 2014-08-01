import telnetlib, sys, os, pygame

class TelnetClient:

    def __init__(self, ip, port):
        self.ip, self.port = ip, port
        self.tn=telnetlib.Telnet(ip, port)
        self.neutral=[5,5,5,5,0]
        self.speed=1

    def steer(self, params):
        params=''.join([str(x) for x in params]) 
        self.tn.write(params)

    def steering(self):
        pygame.init()
        clock = pygame.time.Clock()
        W, H = 320, 240
        screen = pygame.display.set_mode((W, H))
        running = True
        result=self.neutral[:]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYUP:
                    result=self.neutral[:]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
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
                        
                    self.steer(result)
                    
            pygame.display.flip()
            clock.tick(50)
            pygame.display.set_caption("FPS: %.2f" % clock.get_fps())


a = TelnetClient("192.168.2.102", 51234)
a.steering()
