__author__ = 'loziuk'


import sys , argparse
from socket import socket, AF_INET, SOCK_DGRAM

class Communication:
    def __init__(self, ip, port=1111, packetSize=1024):
        self.ip, self.port, self.packetSize  = ip, port, packetSize
        self.mySocket = socket( AF_INET, SOCK_DGRAM)
        self.mySocket.connect((self.ip, self.port))

    def interpretData(self, data):
        pass

    def sendData(self, data):
        self.mySocket.sendto(data, (self.ip,self.port))

    def receiveData(self):
        return con.mySocket.recvfrom(self.packetSize)
"""
while True:
        self.mySocket.sendto('cool',(SERVER_IP,PORT_NUMBER))
sys.exit()
"""
if __name__ == "__main__":
    con = Communication()
    while 1:
        (data,addr) = con.receiveData();
        print "START"+data+"STOP";
        con.interpretData(data)

