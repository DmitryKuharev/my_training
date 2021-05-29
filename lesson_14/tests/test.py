import unittest
from lesson_14.bowling import BowlingScore


class SimpleBowlingCount:
    score = 0

    def get_score(self, game_result):
        self.score += game_result.count('X') * 20
        buffer = game_result.replace("X", '')
        while '/' in buffer:
            index = buffer.find('/')
            buffer = buffer[:index - 1] + buffer[index + 1:]
            self.score += 15
        for i in list(buffer):
            if i == '-':
                continue
            else:
                self.score += int(i)
        return self.score


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.result = BowlingScore()
        self.tes = SimpleBowlingCount()

    def test_simple(self):
        self.result.score('X4/3--45/-')
        self.assertEqual(self.result.total_score, self.tes.get_score('X4/3--45/-'))

    def test_first(self):
        self.result.score('XXX')
        self.assertEqual(self.result.total_score, self.tes.get_score('XXX'))

    def test_second(self):
        self.result.score('37281955647346--82')
        self.assertEqual(self.result.total_score, self.tes.get_score('37281955647346--82'))



