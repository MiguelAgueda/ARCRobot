import movements as mv
import checks as chk
# from settings import Settings
# from learning import Collision
#
# stg = Settings()
# col = Collision()


def autonomous():
    while True:
        if chk.front():
            mv.path_clear()

        elif not chk.front():
            mv.path_not_clear()

        else:
            print("Error in autonomous()")


try:
    autonomous()
except KeyboardInterrupt:
    print("\nProgram Terminated")
    mv.cleanup()
