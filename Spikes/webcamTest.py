# Raspberry Pi Webcam Test
# Detects the color red and creates a 
# video feed of only things that are red.
# Uses external USB webcam.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Set resolution to 640x480
cap.set(3, 640)
cap.set(4, 480)


while(1):
	# Get newest frame
	_, frame = cap.read()

	# Convert frame into HSV format
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Create upper and lower bound to define what
	# exactly is 'red'. Values are arbitray and 
	# results will vary based on these values.
	lower_red = np.array([50, 50, 120])
	upper_red = np.array([175, 165, 255])

	# Create a binary color mask of red pixels
	mask = cv2.inRange(hsv, lower_red, upper_red)

	# Logical AND the frame and the mask. Video will
	# only show frame pixels that share a position
	# with white mask pixels.
	res = cv2.bitwise_and(frame, frame, mask = mask)

	# Update all three displays to illustrate the 
	# process.
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	# Terminate on 'q' press
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()