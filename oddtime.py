from datetime import datetime 
import time 
import random

odds = [1,3,5,7,9,11,13,15,17,18,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
for i in range(5):
    now_minute = datetime.today().minute
    if now_minute in odds:
        print("emmm,odd")
        WaitTime = random.randint(1,60)
        print(WaitTime)
        time.sleep(WaitTime)
    else:
        print("it's ok")
        WaitTime = random.randint(1,60)
        print(WaitTime)
        time.sleep(WaitTime)