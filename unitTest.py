import unittest
import board
import time
import player

class TestBoardObjectForSucessfulCreation(unittest.TestCase):
    def test_createBoard(self):
        object = board.Board(9, 9, 10)
        object.createBoard(0, 0)
        numMines = 0
        numSafe = 0
        for i in range(0,9):
            for j in range(0, 9):
                if (object.spots[i][j] == 1):
                    numMines += 1
                else:
                    numSafe += 1
        self.assertEqual(numMines, 10)
        self.assertEqual(numSafe, 81-10)

    def test_checkValid(self):
        object = board.Board(9, 9, 10)
        self.assertFalse(object.checkValid(-1, 3))
        self.assertFalse(object.checkValid(3, -1))
        self.assertFalse(object.checkValid(123, 3))
        self.assertFalse(object.checkValid(3, 123))
        self.assertTrue(object.checkValid(3, 3))

    def test_checkAdj(self):
        object = board.Board(9, 9, 10)
        object.spots[0][0] = 1
        self.assertEqual(object.checkAdjacent(1, 1), 1)
        object.spots[0][1] = 1
        self.assertEqual(object.checkAdjacent(1, 1), 2)

    def test_makeMove(self):
        object = board.Board(3, 3, 5)
        object.spots[2][1] = 1
        self.assertEqual(object.makeMove(2, 1), 1) #is mine
        self.assertEqual(object.makeMove(2, 0), 3) #1 adjacent mine
        self.assertEqual(object.makeMove(0, 0), 2) #no adjacent mine

    def test_revealBoard(self):
        object = board.Board(3, 3, 5)
        object.revealBoard
        for i in range(3):
            for j in range(3):
                self.assertNotEqual(object.spots[i][j], 0)

class TestPlayerObjectForSucessfulCreation(unittest.TestCase):
    def test_playerInit(self):
        object = player.Player("test")
        self.assertEqual(object.name, "test")

    def test_Time(self):
        object = player.Player("test")
        time.sleep(.001)
        totalTime = object.getTotalTime()
        self.assertTrue(totalTime > 0)

if __name__ == '__main__':
    unittest.main()
