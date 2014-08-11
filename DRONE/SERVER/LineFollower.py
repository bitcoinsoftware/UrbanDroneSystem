""" LineFollower.py - detect a line in the image and follow it """
import cv2, sys, math, time,  numpy as np

class LineFollower:

    def __init__(self, h,w,s):
        self.originalW = w
        self.h, self.w, self.scale = int(h*s), int(w*s), s
        self.movingAvLen=18
        self.certaintyThreshold = 130
        self.iterationUp, self.iterationDown = 0, 0
        self.upLineMiddle=None
        self.downLineMiddle=None
        self.downLineMeanX, self.upLineMeanX = None, None
        self.downLineMeanDevX, self.upLineMeanDevX = None, None
        self.stdDevOfLines=1
        self.upLineMiddleHistory =np.array([[0,0]]) #to trzeba przekazac
        self.downLineMiddleHistory =np.array([[0,0]]) #to trzeba przekazac

    def updateLineMiddle(self, upLineMiddle, downLineMiddle):
        #count moving averange
        if upLineMiddle!=None:
            self.upLineMiddleHistory= np.append(self.upLineMiddleHistory, [np.array(upLineMiddle)],axis=0)
            if self.iterationUp<self.movingAvLen:
                self.upLineMiddle= tuple(np.average(self.upLineMiddleHistory, axis=0).astype(int))
                self.iterationUp+=1
            else:
                self.upLineMiddle= tuple(np.average(self.upLineMiddleHistory, axis=0).astype(int))
                self.upLineMiddleHistory= np.delete(self.upLineMiddleHistory,0,0)
                self.upLineMeanX = np.mean(self.upLineMiddleHistory, axis=0)[0]
                self.upLineMeanDevX = np.std(self.upLineMiddleHistory, axis=0)[0]

        if downLineMiddle!=None:
            self.downLineMiddleHistory= np.append(self.downLineMiddleHistory, [np.array(downLineMiddle)], axis=0)
            if self.iterationDown<self.movingAvLen:
                self.downLineMiddle= tuple(np.average(self.downLineMiddleHistory, axis=0).astype(int))
                self.iterationDown+=1
            else:
                self.downLineMiddle= tuple(np.average(self.downLineMiddleHistory, axis=0).astype(int))
                self.downLineMiddleHistory= np.delete(self.downLineMiddleHistory,0,0)
                self.downLineMeanX = np.mean(self.downLineMiddleHistory, axis=0)[0]
                self.downLineMeanDevX = np.std(self.downLineMiddleHistory, axis=0)[0]

    def process_frame(self,frame):
        if self.scale !=1:
            frame= cv2.resize(frame, (self.w, self.h))
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        gray = cv2.GaussianBlur(gray,(3,3),3)
        avc = np.mean(gray)
        avc2= avc*1.7
        if avc2<255:
            avc=avc2
        ret2, gray=cv2.threshold(gray,avc2,255,cv2.THRESH_BINARY)
        gray = cv2.Canny(gray,150,200,apertureSize = 5)
        
        linesUP = cv2.HoughLinesP(gray[:self.h/2][:],4,np.pi/45,self.certaintyThreshold, minLineLength = self.h/10, maxLineGap = self.h/48)
        
        upperLineMiddle=None
        if linesUP!=None:
            if self.upLineMeanDevX!=None:
                linesUP = np.array([[e for e in linesUP[0] if abs((e[0]+e[2])/2-self.upLineMeanX)<3 * self.upLineMeanDevX]])
            if len(linesUP[0]):
                x1,y1,x2, y2 = np.median(linesUP,axis=1).astype(int)[0]
                upperLineMiddle = (int((x1+x2)/2) ,int((y1+y2)/2))
                self.updateLineMiddle(upperLineMiddle, None)

        linesDOWN = cv2.HoughLinesP(gray[self.h/2:][:],4,np.pi/45,self.certaintyThreshold, minLineLength = self.h/10, maxLineGap = self.h/48)

        lowerLineMiddle=None
        if linesDOWN != None:
            if self.downLineMeanDevX!=None:
                linesDOWN = np.array([[e for e in linesDOWN[0] if abs((e[0]+e[2])/2-self.downLineMeanX)<3 * self.downLineMeanDevX]])
            if len(linesDOWN[0]) :
                x1,y1,x2,y2 = np.median(linesDOWN, axis=1).astype(int)[0]
                lowerLineMiddle = (int((x1+x2)/2) ,int((y1+y2)/2+self.h/2))
                self.updateLineMiddle(None, lowerLineMiddle)

        if self.upLineMiddle and self.downLineMiddle:
            line = [self.upLineMiddle, self.downLineMiddle]
        else:
            line = None
        return [upperLineMiddle, lowerLineMiddle], line

    def getDirections(self, (points, line)):
        if line and points[0] and points[1]:
            commands=[5,6,5,5,1]
        else:
            commands=[5,5,5,5,1]
        
        if points[0] and points[1]:
            middlePoint = [(points[0][0]+points[1][0])/2, (points[0][1]+points[1][1])/2]
            if middlePoint[0]> self.originalW/2+self.originalW/20: # go left
                commands[2]=4
            elif middlePoint[0]< self.originalW/2-self.originalW/20: #go right
                commands[2]=6
        if line:
            if line[0][0]-line[1][0] >self.originalW/20 : # turn right
                commands[0]=6
            elif line[0][0]-line[1][0] < -self.originalW/20: #turn left
                commands[0]=4
        return commands

if __name__ == '__main__':
    print "USAGE: python LineFollower.py filmUrl.mp4 SCALE"
    #try:
    if 1:
        if len(sys.argv[1])==1:
            source = int(sys.argv[1])
        else:
            source=sys.argv[1]
        vidFile = cv2.VideoCapture(source)
        ret, frame = vidFile.read()
        h,w = frame.shape[:2]
        scale = float(sys.argv[2])
        lf = LineFollower(h,w,scale)
        while ret:
            lf.process_frame(frame)
            ret, frame = vidFile.read()
            print ret
            cv2.imshow("preview", frame)
            key = cv2.waitKey(1)
            if key == 27: # exit on ESC
                break
        vc.release()
        cv2.destroyWindow("preview")
    #except:
    #    print "problem opening input stream"
    #    sys.exit(1)
    if not vidFile.isOpened():
        print "capture stream not open"
        sys.exit(1)
    """
    nFrames = int(vidFile.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    print "frame number: %s" %nFrames
    fps = vidFile.get(cv2.cv.CV_CAP_PROP_FPS)
    print "FPS value: %s" %fps
    lf= LineFollower()
    lf.proccess_film(vidFile)
    """
