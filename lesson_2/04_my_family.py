# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Папа', 'Мама', 'Брат']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Папа', 175], ['Мама', 168], ['Брат', 180]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост папы:', my_family_height[0][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print('Общий рост моей семьи', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1])
