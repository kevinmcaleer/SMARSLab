""" SMARS Bluetooth test utility """
import time
import serial

CONNECTED = False
print("Start")
try:
    PORT = "/dev/tty.HC-05-SPPDev-1"
    BLUETOOTH = serial.Serial(PORT, 9600, timeout = 1)
    print("connected")
    CONNECTED = True
except:
    print("Error connecting to Bluetooth port: " + PORT)

DELAY = 0.5

if CONNECTED:
    NB = "1"
    while NB != "q":
        # BLUETOOTH.open()
        NB = ""
        NB = input('WASD: ')
        if NB == "w":
            BLUETOOTH.write(b'u') # up
        if NB == "s":
            BLUETOOTH.write(b'd') # down
        if NB == "a":
            BLUETOOTH.write(b'l') # left
        if NB == "d":
            BLUETOOTH.write(b'r') # right
        # print (str.encode())
        # BLUETOOTH.flushInput()
        note = BLUETOOTH.readline()
        print(note.decode('utf-8'))
        print(str(chr(note)))
        time.sleep(DELAY)
    # while True:
    #     BLUETOOTH.write(str.encode('u'))
    #     print("up")
        # time.sleep(DELAY)
    #     BLUETOOTH.flushInput()
    #
    #     BLUETOOTH.write(str.encode('d'))
    #     print("down")
        # time.sleep(DELAY)
    #     BLUETOOTH.flushInput()
    #
    #     BLUETOOTH.write(str.encode('l'))
    #     print("left")
        # time.sleep(DELAY)
    #     BLUETOOTH.flushInput()
    #
    #     BLUETOOTH.write(str.encode('r'))
    #     print("right")
        # time.sleep(DELAY)
    #     BLUETOOTH.flushInput()
