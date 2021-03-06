from random import randint
from termcolor import cprint
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py
# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.
# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)
# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня
# Человеку и коту надо вместе прожить 365 дней.


class Cat:
    def __init__(self):
        self.cat_name = None
        self.cat_satiety = 10
        self.cat_house = None

    def __str__(self):
        return 'Я - {}, моя сытость {}'.format(
            self.cat_name, self.cat_satiety)

    def eat(self):
        """сытость увеличивается на 20, кошачья еда в доме уменьшается на 10."""
        if self.cat_house.cat_food >= 10:
            cprint('{} поел'.format(self.cat_name), color='yellow')
            self.cat_satiety += 20
            self.cat_house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.cat_name), color='red')

    def cat_sleep(self):
        """сытость уменьшается на 10"""
        cprint('{} спит'.format(self.cat_name), color='red')
        self.cat_satiety -= 10

    def tear_up_wallpaper(self):
        """сытость    уменьшается    на    10, степень    грязи    в    доме    увеличивается    на    5"""
        cprint('{} портит обои'.format(self.cat_name), color='red')
        self.cat_satiety -= 10
        self.cat_house.dirt += 5

    def __del__(self):
        pass

    def cat_act(self):
        if self.cat_satiety <= 0:
            cprint('{} умер...'.format(self.cat_name), color='red')
            return
        dice = randint(1, 3)
        if self.cat_satiety <= 10:
            self.eat()
        elif dice == 1:
            self.cat_sleep()
        elif dice == 2:
            self.tear_up_wallpaper()


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.house.cat_food <= 20:
            self.buy_cat_food()
        dice = randint(1, 6)
        if self.fullness < 40:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()

    def take_cat(self, the_cat, cat_name, house):
        self.cat = the_cat
        self.cat.cat_house = house
        self.cat.cat_name = cat_name
        print('{} принес в дом кота {}'.format(self.name, self.cat.cat_name))


    def buy_cat_food(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кормом'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cat_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean_house(self):
        cprint('{} Убрал в доме'.format(self.name), color='red')
        self.fullness -= 20
        self.house.dirt -= 100


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}. Кошачьей еды {}, а мусора в доме {}'.format(
            self.food, self.money, self.cat_food, self.dirt)



citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
]

my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)


cat = Cat()
citizens[0].take_cat(the_cat=cat, cat_name="Barsik", house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    cat.cat_act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(cat)
    print(my_sweet_home)
