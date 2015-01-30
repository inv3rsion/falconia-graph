import os;
import pty;
import serial;
import time;
import random;

ser = serial.Serial('/dev/ttys003', 9600);

while True:
    ser.write("%s,%s," % (60+random.randint(-20, 20), 75+random.randint(-15, 15)));
#    ser.write("%s,%s," % (5, 10));
    time.sleep(1.2);
    r, g, b = (30+random.randint(-20, 20), 80+random.randint(-20, 20), 130+random.randint(-20, 20));
#    r, g, b = (50, 80, 130);
    ser.write("%s,%s,%s\n" % (r, g, b));
    time.sleep(0.8);
