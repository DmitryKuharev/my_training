# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Airline.
# Подходящий шрифт искать на сайте

from PIL import Image, ImageFont, ImageDraw, ImageColor


def make_ticket():
    image = Image.open('ticket_template.png')
    font = ImageFont.truetype('Ubuntu.ttf', 20)
    draw = ImageDraw.Draw(image)
    text = ['ИВАНОВ', 'SKYSITY', 'SUNCITY', '08.12']
    draw.text((45, 120), text[0], font=font, fill=ImageColor.getrgb("black"))
    draw.text((45, 190), text[1], font=font, fill=ImageColor.getrgb("black"))
    draw.text((45, 255), text[2], font=font, fill=ImageColor.getrgb("black"))
    draw.text((285, 255), text[3], font=font, fill=ImageColor.getrgb("black"))
    return image.show()


ticket = make_ticket()

