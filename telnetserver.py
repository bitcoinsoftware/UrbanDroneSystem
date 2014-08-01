#avconv -r 25 -s 160x128 -f video4linux2 -i /dev/video0 http://127.0.0.1:8090/feed1.ffm
#ffserver -d -f ffserver.conf

import socket, threading, cv2, serial

HOST = ''
PORT = 51234
SERIAL = "/dev/ttyACM99"

try:
    ser = serial.Serial(SERIAL, 9600, timeout=1)
except:
    print("Could not open serial "+SERIAL);
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(4)
clients = [] #list of clients connected
lock = threading.Lock()


class chatServer(threading.Thread):
    def __init__(self, (socket,address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address= address

    def run(self):
        lock.acquire()
        clients.append(self)
        lock.release()
        print '%s:%s connected.' % self.address
        while True:
            data = self.socket.recv(1024)
            print data
            if not data:
                break
            for c in clients:
                c.socket.send(data)
                try:
                    ser.write(data)
                except:
                    print("Could not write to serial ")
                print data
        self.socket.close()
        print '%s:%s disconnected.' % self.address
        lock.acquire()
        clients.remove(self)
        lock.release()

while True: # wait for socket to connect
    # send socket to chatserver and start monitoring
    chatServer(s.accept()).start()
