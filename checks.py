from time import sleep
import movements as mv
import sensors as sen
import checks as chk
from settings import Settings

stg = Settings()

def sides():
    if sen.dist_1() + sen.dist_5() < stg.safe_front_dist:
        print("Sides Checked - Going back.")
        return "back"
#        mv.stop()
#        mv.turn_180()
#        stg.turn_count = 0

    elif sen.dist_1() > sen.dist_5():
        print("Sides Checked - Left.")
        return "left"
#        mv.left_15()
#        stg.turn_count += 1

    elif sen.dist_1() < sen.dist_5():
        print("Sides Checked - Right.")
        return "right"
#        mv.right_15()
#        stg.turn_count += 1

    else:
        print("Error checking sides.")
        return "error"
#        mv.stop()
#        mv.bwd()
#        sleep(0.2)

def front_3():
    dist_2 = True
    dist_3 = True
    dist_4 = True
    front_clear = True

    sleep(0.1)

    if sen.dist_2() < stg.safe_diagonal_dist:
        dist_2 = False

    sleep(0.1)

    if sen.dist_3() < stg.safe_front_dist:
        dist_3 = False

    sleep(0.1)
    
    if sen.dist_4() < stg.safe_diagonal_dist:
        dist_4 = False

    if dist_2 and dist_3 and dist_4:
        front_clear = True
        stg.turn_count = 0

    else:
        front_clear = False

    return front_clear

def turn_count():
    if stg.turn_count > 10:
        stg.turn_count = 0
        return True

    elif stg.turn_count <= 10:
        return False

    else:
        print("Something wrong occurring in turn_count()")
