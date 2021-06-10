import io
import picamera
import cv2
import numpy

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture(stream, format='jpeg')

buff = numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8)

image = cv2.imdecode(buff, 1)

face_cascade = cv2.CascadeClassifier('/home/pi/Documents/opencv_stuff/haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("detecting faces")
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

print("Found {}" + str(len(faces)) + " face(s)")

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h),(255,255,0),4)

cv2.imwrite('result.jpg', image)

