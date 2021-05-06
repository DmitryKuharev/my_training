# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def get_prime_numbers(self):
        for prime in self.prime_numbers:
            if self.i % prime == 0:
                return False
        return True

    def __next__(self):
        while self.i < self.n:
            self.i += 1
            if self.get_prime_numbers():
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()
#
# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

'''==================First var=================='''
def deco(function):
    def check_num(n):
        result = []
        for num in function(n):
            if len(str(num)) % 2 != 0 and len(str(num)) > 1:
                result.append(num)
                yield num
    return check_num


@deco
def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n+1, 2):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


# l1 = prime_numbers_generator(1000)
# for i in l1:
#     print(i)
#==================================================

# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n + 1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
def check_lucky_number(x):
    str_number = str(x)
    if len(str_number) <= 2:
        raise ValueError(f'{x} - Недопустимое число, минимально допустимое число это трехзначное')
    dev = int(len(str_number)/2)
    first_part = str_number[:dev]
    second_part = str_number[-dev:]
    if summa(first_part) == summa(second_part):
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')


def summa(number):
    a = 0
    for i in str(number):
        a += int(i)
    return a


# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
def palindrome(x):
    str_number = str(x)
    dev = int(len(str_number) / 2)
    first_part = str_number[:dev]
    second_part = str_number[-dev:][::-1]
    print(f'{x} - palindrome' if first_part == second_part else print(f'{x} - NOT palindrome'))

palindrome(723327)
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
