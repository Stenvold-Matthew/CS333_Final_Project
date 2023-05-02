self.assertEqual(object.makeMove(2, 1), 1) #is mine
        self.assertEqual(object.makeMove(2, 0), 3) #1 adjacent mine
        self.assertEqual(object.makeMove(0, 0), 2) #no adjacent mine