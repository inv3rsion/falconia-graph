import serial;
import time;
import os;

#data = serial.Serial('/dev/ttys008', 9600);
data = serial.Serial('/dev/ttyACM1', 9600);

while True:
    indata = data.readline().strip();
    print indata;
