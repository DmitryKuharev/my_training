from abc import ABCMeta, abstractmethod

STRIKE = 20
SPARE = 15
FOREIGN_STRIKE = 10


class State(metaclass=ABCMeta):
    def __init__(self, object_get_score):
        self.object_get_score = object_get_score

    @abstractmethod
    def take_score(self, char):
        pass


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


class ForeignClient(State):
    def take_score(self, result_for_calculation):
        count = 0
        list_result = list(result_for_calculation)
        last_symbol, penultimate_symbol = list_result[-1:], list_result[-2:-1]
        for symbol in list_result[:-2]:
            next_symbol, through_one_symbol = list_result[count + 1], list_result[count + 2]
            if symbol == 'X':
                self.object_get_score.total_score += FOREIGN_STRIKE
                if next_symbol == 'X':
                    self.object_get_score.total_score += FOREIGN_STRIKE
                    if through_one_symbol == 'X':
                        self.object_get_score.total_score += FOREIGN_STRIKE
                    elif through_one_symbol.isdigit():
                        self.object_get_score.total_score += int(through_one_symbol)
                elif through_one_symbol == '/':
                    self.object_get_score.total_score += FOREIGN_STRIKE
                elif next_symbol.isdigit() and through_one_symbol.isdigit():
                    self.object_get_score.total_score += int(next_symbol) + int(through_one_symbol)
                elif next_symbol.isdigit() and through_one_symbol == '-':
                    self.object_get_score.total_score += int(next_symbol)
                elif through_one_symbol.isdigit() and next_symbol == '-':
                    self.object_get_score.total_score += int(through_one_symbol)
            elif symbol == "/":
                if next_symbol.isdigit():
                    self.object_get_score.total_score += int(next_symbol)
            elif symbol.isdigit():
                if next_symbol == '/':
                    self.object_get_score.total_score += FOREIGN_STRIKE
                elif next_symbol.isdigit() or next_symbol == '-':
                    self.object_get_score.total_score += int(symbol)
                elif list_result[count - 1].isdigit() or list_result[count - 1] == '-':
                    self.object_get_score.total_score += int(symbol)
            count += 1
        if penultimate_symbol[0] == 'X':
            self.object_get_score.total_score += FOREIGN_STRIKE * 3
        elif last_symbol[0] == '/':
            self.object_get_score.total_score += FOREIGN_STRIKE
        elif penultimate_symbol[0].isdigit() and last_symbol[0].isdigit():
            self.object_get_score.total_score += int(last_symbol[0]) + int(penultimate_symbol[0])
        elif penultimate_symbol[0].isdigit() and last_symbol[0] == '-':
            self.object_get_score.total_score += int(penultimate_symbol[0])
        elif last_symbol[0].isdigit() and penultimate_symbol[0] == '-':
            self.object_get_score.total_score += int(last_symbol[0])


class BowlingScore:
    def __init__(self, version=True):
        self.symbol_state = SymbolState(self)
        self.digital_state = DigitalState(self)
        self.foreign_state = ForeignClient(self)
        self.total_score = 0
        self.buffer_symbol = ''
        self._state = self.symbol_state
        self.version = version

    def score(self, result_for_calculation):
        if self.version:
            for char in list(result_for_calculation):
                self._state.take_score(char)
        else:
            self.foreign_state.take_score(result_for_calculation)


class WrongFirstSymbol(Exception):
    def __str__(self):
        return "Неверный ввод! Результат не может начинатся символом '/'"


class InvalidNumberOfCharacters(Exception):
    pass


class InvalidNumberOfScore(Exception):
    pass


class SimpleCheckResult:
    def __init__(self, result):
        self.result = result

    def check_result(self):
        if list(self.result)[0] == '/':
            raise WrongFirstSymbol()
        buffer = self.result.replace('X', '')
        while '/' in buffer:
            index = buffer.find('/')
            buffer = buffer[:index - 1] + buffer[index + 1:]
        if int(len(buffer)) % 2 != 0:
            raise InvalidNumberOfCharacters(f"Неверный ввод! Неверное количество символов {self.result}")
        if any(char in '.,:;!@#$%^&*()_+=| \\' for char in buffer):
            raise InvalidNumberOfScore(f'Строка {self.result} не может содержать спецсимволов')
        list_buffer = list(buffer)
        for char in list_buffer:
            if char.isalpha():
                raise InvalidNumberOfScore(f'{char} - данная буква не дожна быть в результате')
        while list_buffer:
            first_char, second_char = list_buffer.pop(0), list_buffer.pop(0)
            if first_char.isdigit() and second_char.isdigit():
                if int(first_char) + int(second_char) > 10:
                    raise InvalidNumberOfScore(f'За два броска результат не может быть больше 10 очков, проверьте'
                                               f' строку {self.result} верно ли записана данная пара чисел:'
                                               f' {first_char} и {second_char}')


# '285-7/4/3/277-2---'
# 'X4/34'
game_result = "X--XX347/21"

def get_score(game_result, calculation_method=True):
    # try:
    check = SimpleCheckResult(game_result)
    check.check_result()
    result = BowlingScore(version=calculation_method)
    result.score(game_result)
    return result.total_score
    # except Exception as ex:
    #     print(ex)


print(get_score(game_result, calculation_method=False))