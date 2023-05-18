import unittest
import subprocess
import sys
from hw import TicTacGame
from io import StringIO, TextIOWrapper


class TestGame(unittest.TestCase):

    def setUp(self) -> TicTacGame:
        BOARD_X_win: dict = {'7': 'X', '8': ' ', '9': ' ',
                             '4': 'X', '5': ' ', '6': ' ',
                             '1': 'X', '2': ' ', '3': ' '}
        BOARD_O_win: dict = {'7': ' ', '8': ' ', '9': 'O',
                             '4': ' ', '5': 'O', '6': ' ',
                             '1': 'O', '2': ' ', '3': ' '}
        self.game_1 = TicTacGame()
        self.game_2 = TicTacGame()
        self.game_2.BOARD = BOARD_O_win
        self.game_1.BOARD = BOARD_X_win
        self.game = TicTacGame()
        self.result = []

        proc = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE)
        for line in TextIOWrapper(proc.stdout, encoding="utf-8"):
            self.result.append(line)
    
    def test_X_wins(self):
        self.assertTrue(self.game_1.check_winner(player='X'))

    def test_O_wins(self):
        self.assertTrue(self.game_2.check_winner(player='O'))

    def test_start_game(self):
        sys.stdin = StringIO('1\n2\n3\n5\n4\n6\n7\n8')
        self.game.start_game()
        self.assertIn(''.join(self.result), 'Победил игрок')


if __name__ == '__main__':
    unittest.main()