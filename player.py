import time

class Player:

    def __init__(self, name):
        self.name = name
        self.startTime = time.time()

    def getTotalTime(self):
        endTime = time.time()
        return endTime - self.startTime
    
    def getPositions(self, x, y):
        positions = [x, y]  #If I had more time this would convert 
                            #mouse positions to coordinates
        return positions