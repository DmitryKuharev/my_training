# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Airline.
# Подходящий шрифт искать на сайте

from PIL import Image, ImageFont, ImageDraw, ImageColor


def make_ticket():
    image = Image.open('ticket_template.png')
    font = ImageFont.truetype('Ubuntu.ttf', 30)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), 'Hello', font=font, fill=ImageColor.getrgb("black"))
    return image.show()


ticket = make_ticket()

