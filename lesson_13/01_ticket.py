# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Airline.
# Подходящий шрифт искать на сайте

from PIL import Image, ImageFont, ImageDraw


image = Image.open('ticket_template.png')
font = ImageFont.truetype('Ubuntu.ttf', 20)

draw = ImageDraw.Draw(image)
draw.text((100, 100), 'Hello', font=font)
image.show()

