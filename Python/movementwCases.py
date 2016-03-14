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

cam = cv2.VideoCapture(0)   # on jamie's comp use cam = cv2.VideoCapture(1)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

height, width = t.shape

thresh = 80
timethresh = 0.0  # time between images in milliseconds
partitionNum = 20   # number of partitions

partitionLength = width/partitionNum

path = '/dev/cu.usbmodem1411'   # on jamie's comp use path = '/dev/cu.usbmodemfa141'

ser=serial.Serial(path,9600,timeout=0)
time.sleep(2)


while True:
    
    img = diffImg(t_minus, t, t_plus)

    nz = np.transpose(np.nonzero(img>thresh))
    a = 0
    b = 0
    c = 0
    d = 0
    avg=0
    if nz.size>0:   # if there is movement
        a,b = nz[0] # block out the resulting shape
        c,d = nz[-1]
        avg = (b+d)/2 # find center of the movement on y axis
        
		if avg<1*partitionLength:
			ser.write('a')
		elif avg<2*partitionLength:
			ser.write('b')
		elif avg<3*partitionLength:
			ser.write('c')
		elif avg<4*partitionLength:
			ser.write('d')
		elif avg<5*partitionLength:
			ser.write('e')
		elif avg<6*partitionLength:
			ser.write('f')
		elif avg<7*partitionLength:
			ser.write('g')
		elif avg<8*partitionLength:
			ser.write('h')
		elif avg<9*partitionLength:
			ser.write('i')
		elif avg<10*partitionLength:
			ser.write('j')
		elif avg<11*partitionLength:
			ser.write('k')
		elif avg<12*partitionLength:
			ser.write('l')
		elif avg<13*partitionLength:
			ser.write('m')
		elif avg<14*partitionLength:
			ser.write('n')
		elif avg<15*partitionLength:
			ser.write('o')
		elif avg<16*partitionLength:
			ser.write('p')
		elif avg<17*partitionLength:
			ser.write('q')
		elif avg<18*partitionLength:
			ser.write('r')
		elif avg<19*partitionLength:
			ser.write('s')
		elif avg<=width:
			ser.write('t')

    time.sleep(timethresh / 1000.0) # wait for stepper to move

    # Read next image
    t_minus = t
    t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
    
    key = cv2.waitKey(10)
    if key == 27:
       ser.close()
       break

print "Goodbye"



