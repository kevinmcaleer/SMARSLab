import io
import picamera
import cv2
import numpy
import time
from trilobot import *

SHOW_TIME = 3
CLEAR_TIME = 0.5

tbot = Trilobot()

def green_light():
    tbot.fill_underlighting(0,0,0)
    # time.sleep(CLEAR_TIME)
    tbot.set_underlight(LIGHT_FRONT_LEFT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_LEFT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_REAR_LEFT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_FRONT_RIGHT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_RIGHT, 0,255,0, show=False)
    tbot.set_underlight(LIGHT_REAR_RIGHT, 0,255,0, show=False)
    tbot.show_underlighting()

def blue_light():
    tbot.fill_underlighting(0,0,0)
    # time.sleep(CLEAR_TIME)
    tbot.set_underlight(LIGHT_FRONT_LEFT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_LEFT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_REAR_LEFT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_FRONT_RIGHT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_MIDDLE_RIGHT, 0,0,255, show=False)
    tbot.set_underlight(LIGHT_REAR_RIGHT, 0,0,255, show=False)
    tbot.show_underlighting()
    # time.sleep(SHO)



def detect_faces():
    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
        camera.resolution = (320, 240)
        camera.capture(stream, format='jpeg')

    buff = numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8)

    image = cv2.imdecode(buff, 1)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # print("detecting faces")
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    print("Found " + str(len(faces)) + " face(s)")
    if len(faces) > 0:
        green_light()
    else:
        blue_light()

    # write file
    # for (x,y,w,h) in faces:
    #     cv2.rectangle(image, (x,y), (x+w,y+h),(255,255,0),4)

    # cv2.imwrite('result.jpg', image)

while True or KeyboardInterrupt:
    detect_faces()
