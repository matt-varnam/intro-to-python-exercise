#!/usr/bin/python2.7
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

#"8" here is specific to Papuch thermometer device
print ser.read(size=8)
ser.close()
