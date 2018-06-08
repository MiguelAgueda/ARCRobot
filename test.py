import movements as mv
import sensors as sen
import time

try:
    while True:
        a = sen.dist_1()
        print(a)
        time.sleep(0.1)

except KeyboardInterrupt:
    mv.cleanup()
