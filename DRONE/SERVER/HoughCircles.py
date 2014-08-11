import cv2
import numpy as np

class HoughCircles:

    def __init__(self, height, width, scale):
        self.h, self.w, self.scale= height*scale, width*scale, scale

    def findCircles(self, frame):
        if self.scale!=1:
            frame = cv2.resize(frame, (int(w*self.scale), int(h*self.scale)))
        frame = cv2.medianBlur(frame,5)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(frame,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=5,maxRadius=35)
        return circles

    def getDirections(self, circles):
        command=[5,5,5,5,1]
        if circles!=None:
            circles=circles[0] #unpack
            xSum, ySum, l =0, 0, len(circles)
            for circle in circles:
                xSum+=circle[0]
                ySum+=circle[1]
            x, y = xSum/l,ySum/l

            if x < self.w/2+ self.w/20: #go right
                command[2]=6
            elif x>self.w/2+ self.w/20: #go left
                command[2]=4
                
            if y < self.h/2+ self.h/20: #go front
                command[1]=6
            elif y>self.h/2+ self.h/20: #go back
                command[1]=4
                
            if command[0] ==None and command[1]==None: # go down
                command[0]=4
            return command
            
        return None

if __name__ == '__main__':
    import sys
    print "USAGE: python HoughCircles.py filmUrl.mp4 scale"
    if len(sys.argv[1])==1:
        source = int(sys.argv[1])
    else:
        source=sys.argv[1]
    vidFile = cv2.VideoCapture(source)
    ret, frame = vidFile.read()
    h,w = frame.shape[:2]
    cd = HoughCircles(h,w,scale=float(sys.argv[2]))
    while ret:
        ret, frame = vidFile.read()
        circles = cd.findCircles(frame)
        print cd.getDirections(circles)
        print circles
        if circles != None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                cv2.circle(frame,(i[0],i[1]),i[2],(255,255,255),1) # draw the outer circle
                cv2.circle(frame,(i[0],i[1]),2,(128,128,255),3) # draw the center of the circle
        cv2.imshow("preview", frame)
        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
            break
    vc.release()
    cv2.destroyWindow("preview")

    if not vidFile.isOpened():
        print "capture stream not open"
        sys.exit(1)
