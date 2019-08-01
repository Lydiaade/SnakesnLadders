import unittest

from main import SnakesLadders

class TestBlockSize(unittest.TestCase):
    def test_game_play(self):
        game = SnakesLadders()
        print("Should return: 'Player 1 is on square 38'")
        self.assertEquals(game.play(1, 1), "Player 1 is on square 38")
        print("Should return: 'Player 1 is on square 44'")
        self.assertEquals(game.play(1, 5), "Player 1 is on square 44")
        print("Should return: 'Player 2 is on square 31'")
        self.assertEquals(game.play(6, 2), "Player 2 is on square 31")
        print("Should return: 'Player 1 is on square 25'")
        self.assertEquals(game.play(1, 1), "Player 1 is on square 25")

if __name__ == '__main__':
    unittest.main()