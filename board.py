import random


class Board:

    def __init__(self, width, height, numMines):
        self.spots = [[0 for i in range(width)] for j in range(height)]
        self.numMines = numMines
        self.height = height
        self.width = width

    def getSpot(self, x, y):
        return self.spots[x][y]

    def createBoard(self, startingX, startingY):
        minesPlaced = 0
        while (minesPlaced < self.numMines):
        #for i in range(0, 10):
            randX = random.randrange(0, self.width-1)
            randY = random.randrange(0, self.height-1)
            notAdjacentX = (randX - startingX) > 1 or (randX - startingX) < -1
            notAdjacentY = (randY - startingY) > 1 or (randY - startingY) < -1
            notAdjacent = notAdjacentX or notAdjacentY
            if (self.spots[randX][randY] == 0) and notAdjacent:
                self.spots[randX][randY] = 1
                minesPlaced += 1
        self.makeMove(startingX, startingY)

    def checkValid(self, x, y):
        validX = (x >= 0) and (x < self.width)
        validY = (y >= 0) and (y < self.height)
        #notPlayed = self.spots[x][y] == 0
        return validX and validY #and notPlayed
    
    def checkAdjacent(self, x, y):
        numAdjacent = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if(self.checkValid(i, j)):
                    if (self.spots[i][j] == 1):
                        numAdjacent += 1
        return numAdjacent
    
    def makeMove(self, x, y):
        if self.checkValid(x, y):
            value = self.getSpot(x, y)
            if (value == 0):
                value = self.checkAdjacent(x, y) + 2
                self.spots[x][y] = value
                if (value == 2):
                    for i in range(x-1, x+1):
                        for j in range(y-1, y+1):
                            self.makeMove(i, j)
            return value
        else:
            return -1
        
    def revealBoard(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                if (self.getSpot(i, j) == 0):
                    self.makeMove(i, j)