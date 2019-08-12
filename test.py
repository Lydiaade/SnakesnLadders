import unittest,random

from main import SnakesLadders

class TestBlockSize(unittest.TestCase):
    def test_game_play(self):
        game = SnakesLadders()
        print("Should return: 'Player 1 is on square 38'")
        self.assertEqual(game.play(random.randint(1,7), random.randint(1,7)), "Player 1 is on square 38")
        print("Should return: 'Player 1 is on square 44'")
        self.assertEqual(game.play(random.randint(1,7), random.randint(1,7)), "Player 1 is on square 44")
        print("Should return: 'Player 2 is on square 31'")
        self.assertEqual(game.play(random.randint(1,7), random.randint(1,7)), "Player 2 is on square 31")
        print("Should return: 'Player 1 is on square 25'")
        self.assertEqual(game.play(random.randint(1,7), random.randint(1,7)), "Player 1 is on square 25")

if __name__ == '__main__':
    unittest.main()