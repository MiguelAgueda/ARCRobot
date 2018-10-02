from time import sleep
import movements as mv
import sensors as sen
import checks as chk
from settings import Settings

stg = Settings()

def front():
   if sen.front_dist() > stg.safe_front_dist:
       return True
   else:
       return False
