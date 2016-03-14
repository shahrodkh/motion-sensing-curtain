# source: http://www.steinm.com/blog/motion-detection-webcam-python-opencv-differential-images/

import cv2
import numpy as np
import serial
import time

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    dif = cv2.bitwise_and(d1, d2)
    return np.fliplr(dif)

cam = cv2.VideoCapture(0)  

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

thresh = 80


ser=serial.Serial('/dev/cu.usbmodem1411',9600,timeout=0)
time.sleep(2)


while True:
    
    img = diffImg(t_minus, t, t_plus)

    nz = np.transpose(np.nonzero(img>thresh))
    a = 0
    b = 0
    c = 0
    d = 0
    avg=0
    if nz.size>0:
        a,b = nz[0]
        c,d = nz[-1]
        avg = (b+d)/2
        if 0<=avg and avg<=1280:
            ser.write(str(int(avg))+" ") 

    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    

    key = cv2.waitKey(10)
    if key == 27:
       ser.close()
       break

print "Goodbye"



