import serial;
import time;

data = serial.Serial('/dev/ttys002', 38400);

while True:
    indata = data.readline().strip();
    print indata;
    time.sleep(1);
