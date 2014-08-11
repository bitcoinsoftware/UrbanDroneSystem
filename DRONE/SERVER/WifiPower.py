import subprocess
import time
import argparse
import multiprocessing

class WifiPower():
    def __init__(self, interfaceName):
        self.interfaceName = interfaceName

    def scan(self):
        cmd = subprocess.Popen('/sbin/iwconfig %s' % self.interfaceName, shell=True,
                                  stdout=subprocess.PIPE)
        keystr, keystr2, keystr3= 'Signal level=', 'dBm', 'Not-Associated'

        for line in cmd.stdout:
            if keystr in line:
                line= line[line.find(keystr) + len(keystr):]
                line= line[:line.find(keystr2)]
                return int(line.lstrip(' '))
            elif 'Not-Associated' in line:
                return -9999

    def isCloseToAP(self):
        signalPow = self.scan()
        if abs(signalPow)<=3:  # is signal is stronger than -2 dBm
            return True
        else:
            return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
    parser.add_argument(dest='interface', nargs='?', default='wlan0',
                       help='wlan interface (default: wlan0)')
    args = parser.parse_args()
    wp = WifiPower(args.interface)
    print wp.scan()
    print wp.isCloseToAP()

    '''
    scanProcess = multiprocessing.Process(target=wp.scan)
    scanProcess.start()
    scanProcess.join()
    scanProcess.terminate()'''
