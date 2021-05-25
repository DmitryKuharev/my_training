from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def take_score(self):
        pass


class SymbolState(State):

    def take_score(self):
        pass


class DigitalState(State):
    def take_score(self):
        pass


class BowlingScore:
    def __init__(self):
        self.symbol_state = SymbolState(self)
        self.digital_state = DigitalState(self)
        self.total_score = 0
        self.buffer_symbol = 0


def get_score(game_result):
    score = 0
    score += game_result.count('X') * 20
    buffer = game_result.replace("X", '')
    while '/' in buffer:
        index = buffer.find('/')
        buffer = buffer[:index - 1] + buffer[index + 1:]
        score += 15
    for i in list(buffer):
        if i == '-':
            continue
        else:
            score += int(i)
    return score


print(get_score("X4/3--44/-"))