## Authors: Matthew Stenvold, Kyle Knotek
## Date: 4/29/23

import board

def selectDifficulty():
    print("What difficulty would you like to choose?")
    difChoice = int(input("1. Easy (9x9, 10)| 2. Intermediate (16x16, 40)| 3. Expert (24x24, 99): "))
    difficultyParameters = [0, 0, 0]
    if (difChoice == 1):
        difficultyParameters = [9, 9, 10]
    elif (difChoice == 2):
        difficultyParameters = [16, 16, 40]
    elif (difChoice == 3):
        difficultyParameters = [24, 24, 99]
    return difficultyParameters

def decideMove():
    moveCoors = [0, 0]
    moveCoors[0] = int(input("X Value for your move: "))
    moveCoors[1] = int(input("Y Value for your move: "))
    return moveCoors

def printBoard(inputBoard):
    for i in range(0, inputBoard.width):
        for j in range(0, inputBoard.height):
            if not ((inputBoard.spots[i][j] == 0) or inputBoard.spots[i][j] == 1):
                print(inputBoard.spots[i][j] - 0, end ="|")
            else:
                print(" ", end ="|")
        print("\n------------------------------------------------------------")

parameters = selectDifficulty()
playingBoard = board.Board(parameters[0], parameters[1], parameters[2])
startingPos = decideMove()

playingBoard.createBoard(startingPos[0], startingPos[1])
printBoard(playingBoard)

stillPlaying = True
while(stillPlaying):
    pos = decideMove()
    result = playingBoard.makeMove(pos[0], pos[1])
    if (result == 1):
        stillPlaying = False
        print("Game Over")
        playingBoard.revealBoard()
    else:
        adjMines = str(playingBoard.spots[pos[0], pos[1]]-2)
        print("The number of adjacent mines is " + adjMines)



