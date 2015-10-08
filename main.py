import cv2
import sys
import RPi.GPIO as GPIO

# DEBUG MODE
DEBUG = True


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

cap = cv2.VideoCapture(0)

# Set resolution
cap.set(3, 200) # X
cap.set(4, 200) # Y

# Create the haar cascade
cascPath = 'res/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
#cascPath = 'res/frontalEyes35x16.xml'
#eyesCascade = cv2.CascadeClassifier(cascPath)
cascPath = 'res/haarcascade_eye.xml'
individualEyeCascade = cv2.CascadeClassifier(cascPath)

while(1):
	# Get newest frame
	_, frame = cap.read()

	# Generate grayscale image from grame
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.1,
    		minNeighbors=5,
    		minSize=(30, 30),
    		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	# Detect eyes in the image
	#eyes = eyesCascade.detectMultiScale(
    	#	gray,
    	#	scaleFactor=1.1,
    	#	minNeighbors=5,
    	#	minSize=(30, 10),
    	#	flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	#)

	# Detect individual eyes in the image
	iEyes = individualEyeCascade.detectMultiScale(
    		gray,
    		scaleFactor=1.1,
    		minNeighbors=5,
    		minSize=(10, 10),
    		flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
    		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	#for (x, y, w, h) in eyes:
    	#	cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

	for (x, y, w, h) in iEyes:
    		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# If a face is detected, turn on the LED
	if(len(faces) < 1):
		GPIO.output(11, GPIO.LOW)
	else:
		GPIO.output(11, GPIO.HIGH)

	# If DEBUG is true, show video on screen
	# Terminate with 'q' press
	if(DEBUG == True):	
		cv2.imshow("Faces found", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

GPIO.output(11, GPIO.LOW)