#!/usr/bin/env python
# PS2 Buzz! Controller library
import usb.core
import usb.util
import threading, time
from PyQt4 import QtCore
from InputDevice import InputDevice

class PS2Controller(InputDevice, threading.Thread):
    def __init__ (self, id_vendor, id_product, ui ):
        threading.Thread.__init__(self)
        # ID 054c:1000 Sony Corp. Wireless Buzz! Receiver
        self.device = usb.core.find(idVendor=id_vendor, idProduct=id_product)
        self.interface = 0
        self.bits = 0
        if self.device is None:
            raise ValueError('Device not found')

        if self.device.is_kernel_driver_active(self.interface) is True:
            self.kerneldriver = True
            self.device.detach_kernel_driver(self.interface)
        else:
            self.kerneldriver = False

        self.device.set_configuration()
        usb.util.claim_interface(self.device, self.interface)
        cfg = self.device.get_active_configuration()
        self.endpoint = cfg[(0,0)][0]

        self.runAnalysis = True
        self.ui = ui
        print "zainicjowany"

    def readcontroller(self, timeout = None):
        # Reads the controller
        # Returns the result of Parsecontroller (the changed bit) or raw
        cfg = self.device.get_active_configuration()
        self.endpoint = cfg[(0,0)][0]
        data = self.device.read(self.endpoint.bEndpointAddress, self.endpoint.wMaxPacketSize, timeout=timeout)
        return data

    def translateToMovements(self, data = [0,0,0,0,0,0,0,0]):
        """
        element 0 - yaw
        element 1 - throttle odwrocony (gora minimum)
        element 3 - roll
        element 4 - pitch odwrocony ( gora minimum)

        element 5 odpowiada za przyciski krzyzowe
        0 - lewy pad, strzalka do przodu
        2 - lewy pad, strzalka w prawo
        4 - lewy pad, strzalka do tylu
        6 - lewy pad, strzalka w lewo
        15- bez przyciskow
        31- prawy pad przycisk do przodu
        47- prawy pad przycisk w prawo
        79- prawy pad przycisk w dol
        143-prawy pad przycisk w lewo

        element 6 odpowiada za przyciski z przodu pada, select/start, wciskanie joystickow
        0  - brak wcisniec
        1  - lewy 1
        2  - prawy 1
        4  - lewy 2
        8  - prawy 2
        16 - select
        32 - start
        64 - lewy joystick wcisniecie
        128- prawy joystick wcisniecie
        """
        yaw, throttle = data[0], 255 - data[1]
        roll, pitch   = data[3], 255 - data[4]
        return yaw, throttle, roll, pitch

    def run(self):
        while self.runAnalysis:
            yaw, throttle, roll, pitch = self.translateToMovements(self.readcontroller(timeout=500))
            self.ui.object.emit(QtCore.SIGNAL("move(int, int, int, int)"), yaw, throttle, roll, pitch)
            time.sleep(0.1)