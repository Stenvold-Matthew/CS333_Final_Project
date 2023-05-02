import time

class Player:

    def __init__(self, name):
        self.name = name
        self.startTime = time.time()

    def getTotalTime(self):
        endTime = time.time()
        return endTime - self.startTime