# Import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

X_RESOLUTION = 400
Y_RESOLUTION = 400

# Init camera and grab reference to raw camera capture
camera = PiCamera()
camera.resolution = (X_RESOLUTION, Y_RESOLUTION)
rawCapture = PiRGBArray(camera, size = (X_RESOLUTION, Y_RESOLUTION))

# Allow camera to prep
time.sleep(0.1)

# Grab image from camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
image.setflags(write=True)

avgPixelVal = 0
for x in range(0, X_RESOLUTION):
	for y in range(0, Y_RESOLUTION):
		avgPixelVal = (avgPixelVal + sum(image[x][y])) / 2

for x in range(0, X_RESOLUTION):
	for y in range(0, Y_RESOLUTION):
		if(sum(image[x][y]) > avgPixelVal):
			image[x][y] = [0, 0, 0]
		else:
			image[x][y] = [255, 255, 255]

# Display image
cv2.imshow("image", image)
cv2.waitKey(0)
