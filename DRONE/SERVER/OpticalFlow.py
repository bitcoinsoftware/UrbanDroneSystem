""" OpticalFlow.py  - counts optical linear flow and rotational flow """
import numpy, cv2
class OpticalFlow:
    def __init__(self, h, w, s=1, mACoeff=0.95):
        self.scale = s
        self.h, self.w, = int(h*s), int(w*s)
        self.mACoeff = mACoeff
        self.totalOFx = 0
        self.totalOFy = 0
        self.totalRotationalFlow = 0
        self.ofCoeficientMat = self._countOFCoefMat()
        

    def ofFramePrepare(self, frame, prevFrame):
        frame = cv2.absdiff(frame, prevFrame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        frame = cv2.resize(frame, (self.w, self.h))
        return frame

    def countOF(self, img, prevImg, step=16):
        prevPts= cv2.goodFeaturesToTrack(prevImg, 40, 0.9, 5, useHarrisDetector=True)
        if prevPts!=None:
            nextPts, st, err = cv2.calcOpticalFlowPyrLK(prevImg, img, prevPts, None)
            deltaXY = (nextPts-prevPts).reshape(-1, 2)
            avOFx, avOFy= numpy.round(numpy.mean(deltaXY, 0))
            ofMomentum, prevPtsLen =0, len(prevPts)
            for i in range(prevPtsLen):
                ofMomentum +=deltaXY[i][1]/self.ofCoeficientMat[int(prevPts[0][0][1])][int(prevPts[0][0][0])]
            ofMomentum = round(ofMomentum/prevPtsLen)
            self.totalOFx = round(self.totalOFx*self.mACoeff - avOFx*(1-self.mACoeff), 4)
            self.totalOFy = round(self.totalOFy*self.mACoeff + avOFy*(1-self.mACoeff), 4)
            self.totalRotationalFlow = round(self.totalRotationalFlow*self.mACoeff + ofMomentum*(1-self.mACoeff), 4)
            
            return (avOFx, avOFy, self.totalOFx, self.totalOFy,ofMomentum,self.totalRotationalFlow)
        return None

    def _countOFCoefMat(self):
        coefMat = numpy.zeros((self.h, self.w))
        for x in range(self.w):
            for y in range(self.h):
                coefMat[y][x] = x - self.w/2
                if coefMat[y][x]==0:
                    coefMat[y][x]=1
        return coefMat
    #TO DO 
    def getDirections(self):
        return [5,5,5,5,1]
