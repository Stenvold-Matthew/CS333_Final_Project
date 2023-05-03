import random


class Board:

    def __init__(self, width, height, numMines):
        #Creates a 2d array of integers for the playing board
        self.spots = [[0 for i in range(width)] for j in range(height)] #
        self.numMines = numMines
        self.height = height
        self.width = width
        self.spotsRevealed = 0
        self.gameOver = False

    def getSpot(self, x, y):
        return self.spots[x][y]

    def createBoard(self, startingX, startingY):
        minesPlaced = 0
        while (minesPlaced < self.numMines):
        # While there are less mines then desired, randomize a location
            randX = random.randrange(0, self.width-1)
            randY = random.randrange(0, self.height-1)
            notAdjacentX = (randX - startingX) > 1 or (randX - startingX) < -1
            notAdjacentY = (randY - startingY) > 1 or (randY - startingY) < -1
            notAdjacent = notAdjacentX or notAdjacentY
            # If the spot is not adjacent to the starting location and is not already a mine
            if (self.spots[randX][randY] == 0) and notAdjacent:
                self.spots[randX][randY] = 1
                minesPlaced += 1
        # Make a move at the starting postion to unveal area
        self.makeMove(startingX, startingY)

    def checkValid(self, x, y):
        # Check that the spot is within the playing area
        validX = (x >= 0) and (x < self.width)
        validY = (y >= 0) and (y < self.height)
        return validX and validY 
    
    def checkAdjacent(self, x, y):
        numAdjacent = 0
        #Reiterate over the adjacent spots to see how many mines there are
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if(self.checkValid(i, j)):
                    if (self.spots[i][j] == 1):
                        numAdjacent += 1
        return numAdjacent
    
    def makeMove(self, x, y):
        if self.checkValid(x, y):
            # Increase the score if the game is not over
            if not self.gameOver and self.spots[x][y] == 0:
                self.spotsRevealed += 1
            value = self.getSpot(x, y)
            # If the spot is not a mine and unplayed
            if (value == 0):
                value = self.checkAdjacent(x, y) + 2
                self.spots[x][y] = value
                # Change the value of the spot to reflect how many mines are adjacent
                if (value == 2):
                    # If no adjacent, play all adjacent moves
                    for i in range(x-1, x+2):
                        for j in range(y-1, y+2):
                            self.makeMove(i, j)
            return value
        else:
            # If an ilegal move, return -1
            return -1
        
    def revealBoard(self):
        # Set gameover to true and play all remaining moves
        self.gameOver = True
        for i in range(0, self.width):
            for j in range(0, self.height):
                if (self.getSpot(i, j) == 0):
                    self.makeMove(i, j)

    def checkWin(self): #If the board is fully cleared, return true
        totalNumberOfSafeSpots = self.width * self.height
        totalNumberOfSafeSpots -= self.numMines

        if(self.spotsRevealed == totalNumberOfSafeSpots):
            return True
        else:
            return False