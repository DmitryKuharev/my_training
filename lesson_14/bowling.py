exmple = 'X4/344/'


def get_score(game_result):
    score = 0
    score += game_result.count('X') * 20
    buffer = game_result.replace("X", '')
    while '/' in buffer:
        index = buffer.find('/')
        buffer = buffer[:index - 1] + buffer[index + 1:]
        score += 15
    for i in list(buffer):
        score += int(i)
    return score


print(get_score(game_result=exmple))
