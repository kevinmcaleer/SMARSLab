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

DELAY = 2

if CONNECTED:
    while True:
        print("up")
        BLUETOOTH.write(b'u')
        print(BLUETOOTH.readline())
        time.sleep(DELAY)

        print("down")
        BLUETOOTH.write(b'd')
        print(BLUETOOTH.readline())
        time.sleep(DELAY)

        print("left")
        BLUETOOTH.write(b'l')
        print(BLUETOOTH.readline())
        time.sleep(DELAY)

        print("right")
        BLUETOOTH.write(b'r')
        print(BLUETOOTH.readline())
        time.sleep(DELAY)
    time.sleep(DELAY)
