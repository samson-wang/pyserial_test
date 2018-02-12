import serial
ser = serial.Serial('/dev/tty.usbserial')

s = ser.read(100)

print s
