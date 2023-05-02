Project Documentation

Project Description

	For this project, I have decided to implement the game Minesweeper using Python in VScode. I’m currently undecided on how I want the user to input their moves, as ideally, I would have them use the mouse to choose where to make moves. However, I have never created a program like that, so I might end up having the user just enter which move to make into the terminal. 

Regardless the main part of the program remains the same. To begin, the user will select what difficulty they would like to play on. This will alter how big the playing area is and how many mines there are, with both increasing as difficulty increases. I may also implement a feature that allows the user to make their own difficulty by selecting both of those values manually. From there, the user will be allowed to make one move and then it will generate the starting board from the difficulty parameters. 

The board will be stored as a 2D array of integers where 0 represents a safe spot, 1 represents a mine, and 2 represents a revealed safe spot (optional depending on how I implement the program). To generate the board, it will randomly place mines across the playing area until the predetermined number of mines is reached. A mine can be placed anywhere in the playing field as long as it doesn’t overlap with an existing mine and is not adjacent to the starting position, which is why it is done after the initial move. This is to ensure the first move made isn’t a mine.

At this point, the user will be allowed to make moves by deciding which spot they would like to uncover. If I do create the program to work using the mouse, the user will also be able to mark a spot as a mine using the right mouse button. When uncovering a spot, assuming it is not a mine, it will check to see how many mines are adjacent to it. It will then make this information available to the player. 

If the spot is a mine, then it will give the player a game over and uncover the rest of the field. From here, the user may choose to change the difficulty or retry, which will replay the game without having to choose the difficulty. I may choose to implement a scoring system, which will be a mixture of time elapsed and safe spaces uncovered. If so, I might also implement a leaderboard.

Test Plan

	Regardless of how I implement the project, my testing plan will remain mostly the same. When writing the source code, I will prioritize modularity and avoid I/O elements. The former will involve writing functions such as checkValid(x, y), which will return a bool value on whether or not the move is valid. These functions can be used multiple times throughout the program and are easy to test, making them ideal for this sort of project. I will avoid I/O elements as those are difficult to test and should be implemented at the very end, not built into the base of the program. I will be measuring my test coverage by running coverage.py, which can give you an extensive breakdown of which parts of the code are being tested and the percent coverage of each file. I will now go over 5 different integration tests I plan to include.

Using the checkValid function I described earlier, I will check whether a given move is valid in various game states. A valid move is any move that is within the confines of the board and is not an uncovered spot. The position checked will be received from the player class.

A test of the checkAdjacent function. Given a board and a spot to check, it will return how many mines are adjacent to that spot (including diagonals). The test will compare the returned result to the intended value. The position checked will be received from the player class.

If I decide to use mouse integration, then I will have a test that checks that the checkValid function correctly works with the player class when it uses the convertPosition function. The convertPosition function would convert the x and y values of the mouse to workable integers that can be used in the array. So if the mouse is outside of the visual representation of the board, checkValid should not work.

A test of the makeMove function. This function will intake an x and y value, and return whether or not the spot checked is a mine or not (with false being a mine and true being safe). If it is safe, it will run the checkAdjacent function and reveal that value to the player. If that value is 0, it will also run the makeMove function on all of the adjacent spots. The test will only check whether or not it gives the appropriate result of whether or not it is on a mine. The position checked will be received from the player class.

A test of whether the board generated correctly. This test will create a board (or various different boards) and then reiterate over it to return the total number of mines and safe spots. It will then check to make sure that the board contains the correct number of mines and safe spots. It will also check to make sure that there are no adjacent mines to starting position, which is received from the player class.


Source Code and Automated Testing

	For this project, I intend to use GitHub as my technology of choice for centralizing code. This is because it is the technology I am most familiar with and I understand its capabilities the most. Additionally, it is compatible with the technologies I’ll use for other parts of the project as well as being industry standard. I may choose to create multiple branches to help better organize my workflow, especially if I decide to add massive features like the mouse integration which could potentially break my program if integrated incorrectly.

	As for the code testing automation, I will again be using Github in a similar manner as we did for activity 8. I choose the technology for similar reasons as I did for code management, because I am familiar with it and understanding how to do this will be useful for me later in my career. By configuring and integrating a YAML file into my project within the .github/workflows directory, it will automatically run my testing files after committing the code. This will make accessing this information incredibly easy, as it is in the same location as the source code. If possible, I may also choose to configure the YAML file to run coverage.py as well to automate that part of testing as well. 

Build and Deployment Automation

	For automating the build and deployment of finished software, I will probably be using the software application Jenkins (https://www.jenkins.io/), although this is subject to change as I am not familiar with these technologies. However, from my research, this application is free, relatively easy to use, highly customizable, in addition to being one of the leading open-source automation tools used. Not only that but it can be integrated with my other technologies, mainly GitHub, which makes it ideal for this project. An explanation of how to do that can be found here: blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project. My plan for the automation basically just involves following this guide step by step, such that it will build and deploy on every commit. If I feel that is excessive, I may opt to have a separate branch on GitHub which will be used solely for finished software so as to not run this process over every minuscule change.

	
