import subprocess as sub
import movements as mv
import curses as crs
from time import sleep

def main(stdscr):
    stdscr.nodelay(True)
    return stdscr.getch()

def key_press():
    key = crs.wrapper(main)
    w = 119
    a = 97
    s = 115
    d = 100
    if key == -1:
        mv.stop()
    elif key == w:
        mv.fwd()
    elif key == a:
        mv.left()
    elif key == s:
        mv.bwd()
    elif key == d:
        mv.right()
    else:
        pass

try:
    sub.call("/home/pi/downloads/RPi_Cam_Web_Interface/./start.sh")
    while True:
        key_press()
        sleep(0.020)
        
except KeyboardInterrupt:
    sub.call("/home/pi/downloads/RPi_Cam_Web_Interface/./stop.sh")
    mv.cleanup()
    crs.endwin()
