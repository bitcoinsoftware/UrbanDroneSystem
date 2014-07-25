__author__ = 'loziuk'


import sys , argparse, time
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, help="ip address")
    parser.add_argument("-p", '--port', help="port number (default 1111)", nargs='?', const=1111, type=int)
    parser.add_argument("-s", '--packetsize', help="packet size (default 1024 B)", nargs='?', const=1024, type=int)
    args = parser.parse_args()
    con = Communication(args['ip'], args['port'], args['packetsize'])

    while 1:
        (data,addr) = con.receiveData()
        print "START"+data+"STOP"
        con.interpretData(data)


