from time import sleep
import RPi.GPIO as io
import checks as chk
from settings import Settings
import sensors as sen

stg = Settings()
io.setmode(io.BCM)
io.setwarnings(False)

io.setup(2,io.OUT)
io.setup(3,io.OUT)
io.setup(4,io.OUT)
io.setup(5,io.OUT)

all = [2, 3, 4, 5]

def l_fwd():
    io.output(2,0)
    io.output(3,1)

def r_fwd():
    io.output(4,0)
    io.output(5,1)

def l_bwd():
    io.output(2,1)
    io.output(3,0)

def r_bwd():
    io.output(4,1)
    io.output(5,0)

def stop():
    io.output(all, 0)

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
    sleep(0.001)

def left_15():
    left()
    sleep(0.001)

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
    stop()
    print("Stopped")
    sleep(0.1)
    if chk.turn_count():
        print("chk.turn_count()")
        when_stuck()

    else:
        print("path_not_clear: not turn_count()")
        chk.sides()

def path_clear():
    while True:
        if chk.front_3():
            print("Front is clear.")
            fwd()
    
        else:
            pick_a_side()

def when_stuck():
    print("Seemingly stuck. Assessing surroundings.")
    if sen.dist_3() > stg.safe_front_dist:
        print("Best option: Forward.")
        fwd()
        sleep(0.1)

    else:
        print("\nContinuing.\n")
        stg.turn_count = 0

def pick_a_side():
    side = chk.sides()

    if side == "back":
        stop()
        turn_180()

    elif side == "left":
        left_15()

    elif side == "right":
        right_15()

    else:
        stop()
        bwd()
        sleep(0.2)

