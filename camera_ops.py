#!/usr/bin/python3

import cv2
import random
import numpy as np

#img=cv2.imread('pc.jpeg',1)

#for starting the camera
cap=cv2.VideoCapture(0)


while cap.isOpened() :
	print("camera is working")
	status,frame=cap.read()
	print(frame.shape)	
	cv2.rectangle(frame,(100,100),(200,200),(0,255,0),2)
	cv2.rectangle(frame,(300,100),(400,200),(0,255,0),2)
	cv2.rectangle(frame,(100,300),(200,400),(0,255,0),2)
	cv2.rectangle(frame,(300,300),(400,400),(0,255,0),2)
	frame_new = frame[100:200,300:400,:]
	cv2.imshow("cropped",frame_new)
#	status,frame1=cap1.read()
	
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,"Hey smarty",(100,100),font,3,(255,0,0))
	cv2.imshow("Camera123",frame)
	
	x=random.random()
	y=str(x)[2:6]
	cv2.imwrite('adhoc' + y + '.jpg',frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()	
	
