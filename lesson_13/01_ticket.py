# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Airline.
# Подходящий шрифт искать на сайте

from PIL import Image, ImageFont, ImageDraw, ImageColor


def make_ticket():
    image = Image.open('ticket_template.png')
    font = ImageFont.truetype('Ubuntu.ttf', 20)
    draw = ImageDraw.Draw(image)
    text = {'ИВАНОВ': (45, 120), 'SKYSITY': (45, 190), 'SUNCITY': (45, 255), '08.12': (285, 255)}
    for key in text:
        draw.text(text[key], key, font=font, fill=ImageColor.getrgb("black"))
    return image.save('filled_ticket.png')


ticket = make_ticket()

