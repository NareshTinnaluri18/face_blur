import cv2
import os
# dir_="/home/siddharth/Downloads/bahadurgharh_march28/poster/"
dir_ ="images/"
#vid="/home/siddharth/Downloads/BPCL_person/output/"
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter(vid+"still.avi",fourcc, 50, (1280,720), True)
i,j=0,0
#print filelist
cap = cv2.VideoCapture("BIAL_BAY26_2020-03-19T15-18-01-460.mp4")
while True:
   ret, img =cap.read()
   if ret == True and i % 100 == 0:
      cv2.imwrite(dir_+"avi{}.jpg".format(str(j)),img)
      j=j+1
   i=i+1
cap.release()
out.release()
cv2.destroyAllWindows()