import serial
ser = serial.Serial('/dev/tty.usbserial')

print ser.name
ser.write(b'hello')
ser.close()
