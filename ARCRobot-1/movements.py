from time import sleep
import RPi.GPIO as io
import checks as chk
from settings import Settings


stg = Settings()
in1 = stg.in1
in2 = stg.in2
in3 = stg.in3
in4 = stg.in4


io.setmode(io.BCM)
io.setwarnings(False)
# Left
io.setup(stg.all_h_bridge_pins, io.OUT)


def l_fwd():
    io.output(in1, 0)
    io.output(in2, 1)


def r_fwd():
    io.output(in3, 0)
    io.output(in4, 1)


def l_bwd():
    io.output(in1, 1)
    io.output(in2, 0)


def r_bwd():
    io.output(in3, 1)
    io.output(in4, 0)


def stop():
    io.output(stg.all_h_bridge_pins, 0)


def fwd():
    l_fwd()
    r_fwd()


def bwd():
    l_bwd()
    r_bwd()


def right():
    l_fwd()
    r_bwd()


def left():
    l_bwd()
    r_fwd()


def right_15():
    right()
    sleep(0.1)


def left_15():
    left()
    sleep(0.1)


def right_45():
    right()
    sleep(.3)


def left_45():
    left()
    sleep(.3)


def right_90():
    right()
    sleep(0.7)


def left_90():
    left()
    sleep(0.7)


def turn_180():
    right()
    sleep(1.25)


def cleanup():
    io.cleanup()
    io.setmode(io.BCM)


def path_not_clear():
    print("Front is not clear")
    # stop()
    left()
    sleep(0.75)


def path_clear():
        print("Front is clear.")
        fwd()
        sleep(0.5)
