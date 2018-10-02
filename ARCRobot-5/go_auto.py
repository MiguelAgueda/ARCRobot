import movements as mv
import checks as chk
# from settings import Settings
# from learning import Collision
#
# stg = Settings()
# col = Collision()


def autonomous():
    while True:
        chk.for_collision()
        if chk.front_3():
            mv.path_clear()

        else:
            mv.path_not_clear()


try:
    autonomous()
except KeyboardInterrupt:
    print("\nProgram Terminated")
    mv.cleanup()
