import serial
import time

print("Start")
port="/dev/tty.HC-05-SPPDev"
bluetooth=serial.Serial(port, 9600, timeout = 1)

print("connected")
delay = 0.5;

nb = "1"
while nb != "q":
    # bluetooth.open()
    nb = input('WASD: ')
    if nb == "w":
        bluetooth.write(b'u')
        # bluetooth.write(str.encode()) # up
    if nb == "s":
        bluetooth.write(b'd') # down
    if nb == "a":
        bluetooth.write(b'l') # left
    if nb == "d":
        bluetooth.write(b'r') # right
    # print (str.encode())
    # bluetooth.flushInput()

# while True:
#     bluetooth.write(str.encode('u'))
#     print("up")
#     time.sleep(delay)
#     bluetooth.flushInput()
#
#     bluetooth.write(str.encode('d'))
#     print("down")
#     time.sleep(delay)
#     bluetooth.flushInput()
#
#     bluetooth.write(str.encode('l'))
#     print("left")
#     time.sleep(delay)
#     bluetooth.flushInput()
#
#     bluetooth.write(str.encode('r'))
#     print("right")
#     time.sleep(delay)
#     bluetooth.flushInput()
