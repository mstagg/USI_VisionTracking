# Import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

X_RESOLUTION = 100
Y_RESOLUTION = 100

# Initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (X_RESOLUTION, Y_RESOLUTION)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size = (X_RESOLUTION, Y_RESOLUTION))

# Allow camera to warmup
time.sleep(0.1)

avgBool = False
avgPixelVal = 0

#Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# Grab the raw NumPy array representing the image, then illustrate the timestamp
	# and occupied/unoccupied text
	image = frame.array
	image.setflags(write=True)

	if(not avgBool):
		# Find average pixel value in frame
		for x in range(0, X_RESOLUTION):
			for y in range(0, Y_RESOLUTION):
				avgPixelVal = (avgPixelVal + sum(image[x][y])) / 2
		avgBool = True
	else:
		# Assign pixel as black or white based on avg pixel value
		for x in range(0, X_RESOLUTION):
			for y in range(0, Y_RESOLUTION):
				if(sum(image[x][y]) > avgPixelVal):
					image[x][y] = [0, 0, 0]
				else:
					image[x][y] = [255, 255, 255]

		# Show the frame
		cv2.imshow("Test_Frame", image)
		key = cv2.waitKey(1) & 0xFF

		# If the 'q' key was pressed, break from the loop
		if(key == ord('q')):
			break

	# Clear the stream so it is ready to receive the next frame
	rawCapture.truncate(0)