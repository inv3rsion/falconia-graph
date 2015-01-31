import os;
import pty;
import serial;
import time;
import random;

ser = serial.Serial('/dev/ttys002', 9600);
#ser = serial.Serial('/dev/ttyACM0', 9600);

while True:
    ser.write("%s,%s,%s," % ("OK", 27+random.randint(-20, 20), +random.randint(-5, 5)));
#    ser.write("%s,%s," % (5, 10));
    time.sleep(1.2);
    r, g, b = (230+random.randint(-10, 10), 110+random.randint(-10, 10), 75+random.randint(-10, 10));
#    r, g, b = (50, 80, 130);
    ser.write("%s,%s,%s\n" % (r, g, b));
    time.sleep(0.8);
