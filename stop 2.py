import serial
import time
print("Start")
port="/dev/tty.HC-05-DevB"
bluetooth=serial.Serial(port, 9600)
print("connected")
bluetooth.flushInput()

bluetooth.write(str.encode('s'))
print("stop!")
