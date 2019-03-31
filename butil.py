import serial
import time
print("Start")
port="/dev/tty.HC-05-DevB"
bluetooth=serial.Serial(port, 9600)
print("connected")
delay = 0.5;
bluetooth.flushInput()
while True:
    bluetooth.write(str.encode('u'))
    print("up")
    time.sleep(delay)
    bluetooth.flushInput()
    bluetooth.write(str.encode('d'))
    print("down")
    time.sleep(delay)
    bluetooth.flushInput()
    bluetooth.write(str.encode('l'))
    print("left")
    time.sleep(delay)
    bluetooth.flushInput()
    bluetooth.write(str.encode('r'))
    print("right")
    time.sleep(delay)
    bluetooth.flushInput()
