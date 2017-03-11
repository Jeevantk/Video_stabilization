import cv2
import sys

# I am writing this so as to help you guys to get started on the project. This can be used to capture a frame from a video.



cap=cv2.VideoCapture(sys.argv[1])

ret,frame=cap.read()
while(ret):
	cv2.imshow("video",frame)
	cv2.waitKey(10)
	ret,frame=cap.read()

cap.release()
cv2.destroyAllWindows()
