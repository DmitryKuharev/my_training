import random

SECRET_NUMBER = '1234'
step = 0


def make_a_number():
    """Генератор четырехзначного числа"""
    global SECRET_NUMBER
    while len(SECRET_NUMBER) < 4:
        number = str(random.randint(1, 9))
        if number in SECRET_NUMBER:
            pass
        else:
            SECRET_NUMBER += number


def check_user_input(user_number):
    """Проверка введенного числа на корректность"""
    if user_number.isdigit() is False:
        print("Введите число а не буквы!")
        return False
    if len(user_number) != 4:
        print('Число должно быть четырехзначное!')
        return False
    if len(user_number) != len(set(user_number)):
        print("Цифры в загаданном числе должны быть без повтора!")
        return False
    if user_number[0] == '0':
        print("Число не должно начинаться на 0")
        return False
    else:
        return True


def check_a_number(user_number):
    """Функция сравнения числа введенного пользователем с секретным числом"""
    d = {'bulls': 0, 'cows': 0}
    global step
    counter = 0
    step += 1
    if check_user_input(user_number):
        for number in user_number:
            if number in SECRET_NUMBER:
                d['cows'] += 1
            if user_number[counter] == SECRET_NUMBER[counter]:
                d['bulls'] += 1
                d['cows'] -= 1
            counter += 1
        return d


