import RPi.GPIO as io
import time

io.setmode(io.BCM)
io.setwarnings(False)

# Trigger pins
t1 = 22
t2 = 23
t3 = 24
t4 = 25
t5 = 26
# Echo pins
e1 = 16
e2 = 17
e3 = 18
e4 = 19
e5 = 20

all_triggers = [t1, t2, t3, t4, t5]
all_echoes = [e1, e2, e3, e4, e5]

io.setup(all_triggers,io.OUT)
io.setup(all_echoes,io.IN)

def get_distance(trigger, echo):
    # Activate trigger.
    io.output(trigger, 1)
    time.sleep(0.00001)
    io.output(trigger, 0)

    start_time = time.time()
    stop_time = time.time()

    # Save start time.
    while io.input(echo) == 0:
        start_time = time.time()

    # Save arrival time.
    while io.input(echo) == 1:
        stop_time = time.time()

    # Convert time to centimeters.
    distance = ((stop_time - start_time) * 34300) / 2
    return round(distance, 2)

    io.cleanup()

def dist_1():
    return get_distance(t1, e1)

def dist_2():
    return get_distance(t2, e2)

def dist_3():
    return get_distance(t3, e3)

def dist_4():
    return get_distance(t4, e4)

def dist_5():
    return get_distance(t5, e5)
