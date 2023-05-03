## Authors: Matthew Stenvold, Kyle Knotek
## Date: 4/29/23

import board
import player

def selectDifficulty():
    print("What difficulty would you like to choose?")
    message = "1. Easy (9x9, 10)| 2. Intermediate (14x14, 33)| "
    message += "3. Expert (20x20, 100): "
    difChoice = int(input(message))
    difficultyParameters = [0, 0, 0] #Different Difficult parameters
    if (difChoice == 1):
        difficultyParameters = [9, 9, 10]
    elif (difChoice == 2):
        difficultyParameters = [14, 14, 33]
    elif (difChoice == 3):
        difficultyParameters = [20, 20, 100]
    return difficultyParameters

def decideMove(): #Has the user decide a coordinate to move to
    moveCoors = [0, 0]
    moveCoors[0] = int(input("X Value for your move: ")) -1
    moveCoors[1] = int(input("Y Value for your move: ")) -1
    return moveCoors

def printBoard(inputBoard, filler): # Prints the board, unrevealed spaces are ' '
    seperator = "---"
    for k in range(1, inputBoard.width):
        seperator += "----"
    for j in range(0, inputBoard.width):
        for i in range(0, inputBoard.height):
            if (inputBoard.getSpot(i, j) >= 2):
                print(inputBoard.getSpot(i, j) - 2, end =" | ")
            else:
                print(filler, end =" | ")
        print("\n" + seperator)

def main():
    name = input("What is your name?: ")
    user = player.Player(name)
    parameters = selectDifficulty()
    # Make board with given parameters
    playingBoard = board.Board(parameters[0], parameters[1], parameters[2]) 
    startingPos = decideMove()

    playingBoard.createBoard(startingPos[0], startingPos[1])
    numSpacesCleared = 0

    stillPlaying = True
    while(stillPlaying):
        printBoard(playingBoard, ' ')
        pos = decideMove()
        result = playingBoard.makeMove(pos[0], pos[1])
        if (result == 1):
            stillPlaying = False
            print("Game Over")
            playingBoard.revealBoard()
        elif (result == -1):
            print("That is not a legal move")
        else:
            adjMines = str(playingBoard.spots[pos[0]][pos[1]]-2)
            print("The number of adjacent mines is " + adjMines)
            numSpacesCleared += 1
        if(playingBoard.checkWin()):
            print("Congrats, you've won")
            stillPlaying = False

    printBoard(playingBoard, '*')
    totalTime = user.getTotalTime()
    print(user.name + " got " + str(playingBoard.spotsRevealed) + " cleared in", end=" ")
    print(str(round(totalTime, 4)) + " seconds")

if __name__ == '__main__':
    main()

