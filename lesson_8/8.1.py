# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

fur_coat = 0
total_money = 0
total_food = 0


class House:
    def __init__(self):
        self.pollution = 0
        self.money = 100
        self.food = 50
        self.cat_food = 30

    def __str__(self):
        self.pollution += 5
        if self.food < 0:
            cprint(f'NO FOOD', color="red")
        return f'House: pollution - {self.pollution},' \
               f'money - {self.money},' \
               f' food - {self.food},' \
               f' cat food - {self.cat_food}'


class Human:
    def __init__(self, name, home_for_life):
        self.name = name
        self.happy = 100
        self.fullness = 30
        self.home = home_for_life

    def __str__(self):
        if self.fullness <= 0:
            cprint(f'{self.name} died of hunger', color='red')
        elif self.home.pollution >= 90:
            self.happy -= 10
        elif self.happy <= 10:
            cprint(f'{self.name} died of depression', color='red')
        return f'My name is {self.name}, my happy - {self.happy}, my fullness {self.fullness}'

    def pet_cat(self):
        self.happy += 5

    def eat(self):
        global total_food
        quantity = randint(10, 30)
        self.fullness += quantity
        self.home.food -= quantity
        total_food += quantity
        print(f'{self.name} - eating')


class Husband(Human):
    def __init__(self, name, home_for_life):
        super().__init__(name=name, home_for_life=home_for_life)

    def __str__(self):
        return super().__str__()

    def work(self):
        global total_money
        total_money += 150
        self.fullness -= 10
        self.home.money += 150
        print(f'{self.name} - working')

    def gaming(self):
        self.fullness -= 10
        self.happy += 20
        print(f'{self.name} - playing')

    def act(self):
        if self.fullness <= 20:
            return self.eat()
        dice = randint(1, 3)
        if dice == 1:
            return self.gaming()
        elif dice == 2:
            return self.work()


class Wife(Human):
    def __init__(self, name, home_for_life):
        super().__init__(name=name, home_for_life=home_for_life)

    def __str__(self):
        return super().__str__()

    def shopping(self):
        if self.home.cat_food <= 20:
            self.home.cat_food += 10
            self.home.money -= 10
            print(f'{self.name} - buy cat food')
        self.fullness -= 10
        if self.home.food <= 50:
            quantity = randint(25, 40)
            self.home.money -= quantity
            self.home.food += quantity
            print(f'{self.name} - shopping')

    def buy_fur_coat(self):
        global fur_coat
        self.fullness -= 10
        self.home.money -= 350
        self.happy += 60
        fur_coat += 1
        print(f'{self.name} - buy fur coat')

    def clean_house(self):
        self.home.pollution -= 100
        self.fullness -= 10
        print("I'm cleaning our house")

    def act(self):
        if self.fullness <= 20:
            return self.eat()
        elif self.home.money >= 400:
            return self.buy_fur_coat()
        elif self.home.pollution >= 100:
            return self.clean_house()
        elif self.home.food <= 50 or self.home.cat_food <= 20:
            return self.shopping()


class Cat:
    def __init__(self, name, cat_house):
        self.cat_fullness = 30
        self.name = name
        self.home = cat_house

    def act(self):
        if self.cat_fullness <= 20:
            return self.eat()
        dice = randint(1, 2)
        if dice == 1:
            return self.sleep()
        else:
            self.soil()

    def eat(self):
        self.home.cat_food -= 10
        self.cat_fullness += 20
        cprint(f'{self.name} - eat')

    def sleep(self):
        self.cat_fullness -= 10
        cprint(f'{self.name} - sleep')

    def soil(self):
        self.cat_fullness -= 10
        self.home.pollution += 5
        cprint(f'{self.name} - soil')

    def __str__(self):
        if self.cat_fullness <= 0:
            cprint(f'{self.name} - die', color='red')
        return f'{self.name}. Fullness = {self.cat_fullness}'


home = House()
serge = Husband(name='Сережа', home_for_life=home)
masha = Wife(name='Маша', home_for_life=home)
murzik = Cat(name='Мурзик', cat_house=home)

for day in range(366):
    cprint('================== День {} =================='.format(day), color='green')
    serge.act()
    masha.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murzik, color='cyan')
    cprint(home, color='cyan')

cprint(f'All money {total_money}', color='yellow')
cprint(f'All fur {fur_coat}', color='yellow')
cprint(f'All food {total_food}', color='yellow')



