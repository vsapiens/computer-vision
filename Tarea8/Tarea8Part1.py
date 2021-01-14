import numpy as np
import cv2
import matplotlib.pylab as plt

cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	color = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	#Take Picture
	if cv2.waitKey(1) & 0xFF == ord('c'):
		cv2.imwrite('photo.png',frame)
		break
	# Display the resulting frame
	cv2.imshow('frame',color)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
#Read the photo
selfie = cv2.imread('photo.png',0)
meme = cv2.imread('meme.png',0)
# Get the photo measuerements
height, width = selfie.shape
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(selfie,'Erick Gonzalez',(width-250,25), font,1,(0,102,204),2,cv2.LINE_AA)
cv2.putText(selfie,'A01039859',(width-200,75), font, 1,(0,102,204),2,cv2.LINE_AA)
meme = cv2.resize(meme, (selfie.shape[1], int(meme.shape[0] * selfie.shape[1] / meme.shape[1])), interpolation=cv2.INTER_CUBIC)
img = cv2.vconcat([selfie,meme])
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
cv2.imwrite('concatenated.png',img)
plt.show()