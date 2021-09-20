import time
from .event import notfy_listeners

class Timer:

    def __init__(self, tic_interval):
        self.tic_interval = tic_interval

    def start_timer(self):
        while True:
            notfy_listeners("tic")
            print("tic")
            time.sleep(self.tic_interval)