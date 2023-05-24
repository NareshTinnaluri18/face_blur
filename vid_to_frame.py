import cv2
import os
vid="images/"
i=1
count=1
##print filelist
cap = cv2.VideoCapture('BIAL_BAY26_2020-03-19T15-18-01-460.avi')
while True:
	ret, img =cap.read()
	
	if i % 30 == 0:
		#img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
		cv2.imwrite(vid+'avi'+str(count)+'.jpg',img)
		count= count+1
	i=i+1
	if i ==4000000 :
		break


