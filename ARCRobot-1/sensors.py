import RPi.GPIO as io
import settings as stg
import time


io.setmode(io.BCM)
io.setwarnings(False)
# Trig pin
io.setup(stg.Settings().trig, io.OUT)
# Echo pin
io.setup(stg.Settings().echo, io.IN)


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

def front_dist():
    return get_distance(stg.Settings().trig, stg.Settings().echo)
