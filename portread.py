import serial;
import time;
import os;

data = serial.Serial('/dev/ttys002', 9600);

while True:
    indata = data.readline().strip();
    print indata;
