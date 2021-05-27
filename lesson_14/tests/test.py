import unittest
from lesson_14.bowling import BowlingScore


class SimpleBowlingCount:
    def __init__(self, game_result):
        self.game_result = game_result
        self.score = 0

    def get_score(self):
        self.score += self.game_result.count('X') * 20
        buffer = self.game_result.replace("X", '')
        while '/' in buffer:
            index = buffer.find('/')
            buffer = buffer[:index - 1] + buffer[index + 1:]
            self.score += 15
        for i in list(buffer):
            if i == '-':
                continue
            else:
                self.score += int(i)


class BowlingTest(unittest.TestCase):
    def test_check(self):
        result = BowlingScore()
        result.score('X4/3--45/-')
        tes = SimpleBowlingCount('X4/3--45/-')
        tes.get_score()
        self.assertEqual(result.total_score, tes.score)

