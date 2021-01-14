import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ix,iy = -1,-1
hsvColor = np.uint8([[[1,144,113]]])

def mouseBound(event,x,y,flags,param):
	global hsvColor
	if event == cv2.EVENT_MOUSEMOVE:
		ix,iy = x,y
		cv2.circle(frame,(x,y),50,(255,0,0),-1)
		print(frame[ix,iy])
		color = np.uint8([[frame[ix,iy]]])
		hsvColor = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
		print(hsvColor)
		hsvColor
while(1):
	# Take each frame
	_, frame = cap.read()
	cv2.setMouseCallback('frame',mouseBound)
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of selected color in HSV
	lower_bound = np.array([hsvColor[0][0][0]-50,hsvColor[0][0][1]-30,hsvColor[0][0][2]-30])
	upper_bound = np.array([hsvColor[0][0][0]+50,hsvColor[0][0][1]+30,hsvColor[0][0][2]+30])

	# Threshold the HSV image to get only selected colors
	mask = cv2.inRange(hsv, lower_bound, upper_bound)
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()