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