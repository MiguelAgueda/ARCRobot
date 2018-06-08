from time import sleep
import movements as mv
import sensors as sen
import checks as chk
from settings import Settings

stg = Settings()

def front_3():
    dist_2 = sen.dist_2()
    dist_3 = sen.dist_3()
    dist_4 = sen.dist_4()
    dist_2_clear = True
    dist_3_clear = True
    dist_4_clear = True
    front_clear = True

    if dist_2 < stg.safe_diagonal_dist:
        dist_2_clear = False

    if dist_3 < stg.safe_front_dist:
        dist_3_clear = False
    
    if dist_4 < stg.safe_diagonal_dist:
        dist_4_clear = False

    if dist_2_clear and dist_3_clear and dist_4_clear:
        front_clear = True

    else:
        front_clear = False

    return front_clear

def sides():
    print("Checking sides.")
    dist_1 = sen.dist_1()
    dist_5 = sen.dist_5()

    if dist_1 + dist_5 < stg.safe_front_dist:
        print("Sides Checked - Going back.")
        stg.turn_count += 1
        return "back"

    elif dist_1 > dist_5:
        print("Sides Checked - Left.")
        stg.turn_count += 1
        return "left"

    elif dist_1 < dist_5:
        print("Sides Checked - Right.")
        stg.turn_count += 1
        return "right"

    else:
        print("Error checking sides.")
        return "error"

def turn_count():
    if stg.turn_count <= 10:
        return False

    else:
        stg.turn_count = 0
        return True
