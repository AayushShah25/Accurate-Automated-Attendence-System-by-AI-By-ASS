
import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

black = np.zeros((600,600,3))
cv2.putText(black,'1', (200,400), cv2.FONT_HERSHEY_SIMPLEX, 10, (255,0,255), 15)


k = 3
while True:

	black = np.zeros((600,600,3))
	cv2.putText(black,str(k), (200,400), cv2.FONT_HERSHEY_SIMPLEX, 10, (255,0,255), 15)

	
	
	cv2.imshow("SET",black)

	k-=1

	
	cv2.waitKey(1000)

	if k == 0:
		black = np.zeros((600,600,3))
		cv2.putText(black,"SMILE", (60,350), cv2.FONT_HERSHEY_SIMPLEX, 5, (255,0,255), 15)
		cv2.imshow("SET",black)
		cv2.waitKey(1000)
		
		break