from lib.event_test import Test
from lib.timer import Timer
from os import system
import time
import multiprocessing

timer = Timer(1)
test = Test()
    
def longer_timer():
    while True:
        time.sleep(1.5)
        print("1.5 sec")

p1 = multiprocessing.Process(target=timer.start_timer)
p2 = multiprocessing.Process(target=longer_timer)

if __name__ == "__main__":
    p1.start()
    p2.start()
    p1.join()
    p2.join()
