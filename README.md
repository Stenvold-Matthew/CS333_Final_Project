How to Run Automated Testing/Building:

All of the fully up-to-date code can be found on the "Final-Release" branch. Both the testing and the buuilding are done automatically when there is a push to the repository. The test results can be found on the github page under the actions workflow tab, as can the results for the build. The build is hosted on PyPi, under the tag ___. I will update it to work in the morning.

Project Description

For this project, I have decided to implement the game Minesweeper using Python in VScode. I’m currently undecided on how I want the user to input their moves, as ideally, I would have them use the mouse to choose where to make moves. However, I have never created a program like that, so I might end up having the user just enter which move to make into the terminal. 

Regardless the main part of the program remains the same. To begin, the user will select what difficulty they would like to play on. This will alter how big the playing area is and how many mines there are, with both increasing as difficulty increases. I may also implement a feature that allows the user to make their own difficulty by selecting both of those values manually. From there, the user will be allowed to make one move and then it will generate the starting board from the difficulty parameters. 

The board will be stored as a 2D array of integers where 0 represents a safe spot, 1 represents a mine, and 2 represents a revealed safe spot (optional depending on how I implement the program). To generate the board, it will randomly place mines across the playing area until the predetermined number of mines is reached. A mine can be placed anywhere in the playing field as long as it doesn’t overlap with an existing mine and is not adjacent to the starting position, which is why it is done after the initial move. This is to ensure the first move made isn’t a mine.

At this point, the user will be allowed to make moves by deciding which spot they would like to uncover. If I do create the program to work using the mouse, the user will also be able to mark a spot as a mine using the right mouse button. When uncovering a spot, assuming it is not a mine, it will check to see how many mines are adjacent to it. It will then make this information available to the player. 

If the spot is a mine, then it will give the player a game over and uncover the rest of the field. From here, the user may choose to change the difficulty or retry, which will replay the game without having to choose the difficulty. I may choose to implement a scoring system, which will be a mixture of time elapsed and safe spaces uncovered. If so, I might also implement a leaderboard.
