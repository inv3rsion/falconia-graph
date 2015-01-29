import serial;
import random;
import time;
import pty;
import os;

master, slave = pty.openpty();
s_name = os.ttyname(slave);
print s_name;

arduino = serial.Serial(s_name, 38400);
while True:
    r = 20;
    g = 100;
    b = 255;
    arduino.write("%s,%s,%s" % (r, g, b));
    time.sleep(1);
