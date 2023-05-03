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

    def convMouseCoors(self, mouseX, mouseY, xSpots, ySpots):
        area = 600#playable area is 600x600
        xgrid = area / xSpots
        ygrid = area / ySpots

        xpos = mouseX // xgrid
        ypos = mouseY // ygrid

        return [xpos, ypos]