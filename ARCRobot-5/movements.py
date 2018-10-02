from time import sleep
import RPi.GPIO as io
import checks as chk

io.setmode(io.BCM)
io.setwarnings(False)
# Left
io.setup(2, io.OUT)
io.setup(3, io.OUT)
# Right
io.setup(4, io.OUT)
io.setup(5, io.OUT)

all = [2, 3, 4, 5]


def l_fwd():
    io.output(2, 0)
    io.output(3, 1)


def r_fwd():
    io.output(4, 0)
    io.output(5, 1)


def l_bwd():
    io.output(2, 1)
    io.output(3, 0)


def r_bwd():
    io.output(4, 1)
    io.output(5, 0)


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
    if chk.turn_count():
        when_stuck()

    else:
        pick_a_side()


def path_clear():
        print("Front is clear.")
        fwd()
        sleep(0.5)


def when_stuck():
    print("Seemingly stuck.")
    if chk.sides == 'left':
        left_45()
        stop()
        sleep(0.2)

    else:
        right_45()
        stop()
        sleep(0.2)


def pick_a_side():
    stop()
    sleep(0.5)

    # Code below does not operate correctly. Good format for other things(condensed)
    # directions = {"back": turn_180(), "left": left_15(), "right": right_15()}
    # # Calls chk.sides(), using returned value to pick a turn from the dictionary.
    # directions[chk.sides()]

    side = chk.sides()

    if side == "back":
        turn_180()

    elif side == "left":
        left_15()

    elif side == "right":
        right_15()

    else:
        bwd()
        sleep(0.2)
