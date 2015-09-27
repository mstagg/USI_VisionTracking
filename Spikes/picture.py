# Import packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# Init camera and grab reference to raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# Allow camera to prep
time.sleep(0.1)

# Grab image from camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# Display image
cv2.imshow("image", image)
cv2.waitKey(0)
