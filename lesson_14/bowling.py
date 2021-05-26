from abc import ABCMeta, abstractmethod

STRIKE = 20
SPARE = 15


class State(metaclass=ABCMeta):
    def __init__(self, object_get_score):
        self.object_get_score = object_get_score

    @abstractmethod
    def take_score(self, char):
        pass


# res = "X4/3--44/-"


class SymbolState(State):
    def take_score(self, char):
        if char == 'X':
            self.object_get_score.total_score += STRIKE
        elif char.isdigit():
            self.object_get_score.buffer_symbol = char
            self.object_get_score._state = self.object_get_score.digital_state
        elif self.object_get_score.buffer_symbol == '-':
            self.object_get_score.buffer_symbol = char
        elif char == '/' and self.object_get_score.buffer_symbol.isdigit():
            self.object_get_score.total_score += SPARE
            self.object_get_score.total_score -= int(self.object_get_score.buffer_symbol)


class DigitalState(State):
    def take_score(self, char):
        if self.object_get_score.buffer_symbol.isdigit():
            if char == '/':
                self.object_get_score.total_score += SPARE
                self.object_get_score.buffer_symbol = char
                self.object_get_score._state = self.object_get_score.symbol_state
            elif char == '-':
                self.object_get_score.total_score += int(self.object_get_score.buffer_symbol)
                self.object_get_score._state = self.object_get_score.symbol_state
                self.object_get_score.buffer_symbol = char
            else:
                self.object_get_score.total_score += int(self.object_get_score.buffer_symbol)
                self.object_get_score.buffer_symbol = char
                self.object_get_score._state = self.object_get_score.symbol_state
                if char.isdigit():
                    self.object_get_score.total_score += int(char)



class BowlingScore:
    def __init__(self):
        self.symbol_state = SymbolState(self)
        self.digital_state = DigitalState(self)
        self.total_score = 0
        self.buffer_symbol = ''
        self._state = self.symbol_state

    def score(self, result_for_calculation):
        for char in list(result_for_calculation):
            self._state.take_score(char)


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

#     "X4/3--45/--",
#     "X4/3--45/--"
res = "285-7/4/3/277-2---"
#"6---15--142/336/24X"
# "3/15--8117--3628X1/"
# "8-X3-4-41-10----7-X"
# "285-7/4/3/277-2---"
# print(get_score(res))

result = BowlingScore()
result.score(res)
print(result.total_score)
print(get_score(res))

