import unittest
from lesson_14.bowling import BowlingScore, SimpleCheckResult, WrongFirstSymbol, InvalidNumberOfCharacters, \
    InvalidNumberOfScore


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


class BowlingForeignClientTest(unittest.TestCase):

    def setUp(self):
        self.result = BowlingScore(version=False)

    def test_simple(self):
        self.result.score("X4/34")
        self.assertEqual(self.result.total_score, 40)

    def test_first(self):
        self.result.score("XXX347/21")
        self.assertEqual(self.result.total_score, 92)

    def test_second(self):
        self.result.score('--7/X5-6/XXX4/')
        self.assertEqual(self.result.total_score, 144)


class CheckResultTest(unittest.TestCase):

    def test_FirstSymbol(self):
        with self.assertRaises(WrongFirstSymbol):
            check = SimpleCheckResult("/123")
            check.check_result()

    def test_NumberOfCharacters(self):
        with self.assertRaises(InvalidNumberOfCharacters):
            check = SimpleCheckResult("12345")
            check.check_result()

    def test_NumberOfScore(self):
        errors_list = ["123$", "123f", "123499"]
        for error in errors_list:
            with self.assertRaises(InvalidNumberOfScore):
                check = SimpleCheckResult(error)
                check.check_result()
