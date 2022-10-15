import unittest

from main import SnakesLadders

class TestBlockSize(unittest.TestCase):
    def test_game_play(self):
        game = SnakesLadders()
        print("Should return: 'Player 1 is on square 38'")
        result = game.play(1, 1)
        self.assertIn("Player 1", result)
        self.assertIn("is on square 38", result)

        print("Should return: 'Player 1 is on square 44'")
        result = game.play(1, 5)
        self.assertIn("Player 1", result)
        self.assertIn("is on square 44", result)

        print("Should return: 'Player 2 is on square 31'")
        result = game.play(6, 2)
        print(f'This is the result: {result}')
        self.assertIn("Player 2", result)
        self.assertIn("is on square 31", result)

        print("Should return: 'Player 1 is on square 25'")
        result = game.play(1, 1)
        self.assertIn("Player 1", result)
        self.assertIn("is on square 25", result)

if __name__ == '__main__':
    unittest.main()