# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

import cv2
from datetime import datetime


class ImageMaker:
    def __init__(self, date=datetime.today().strftime('%d.%m.%Y')):
        self.date = date
        self.blank = 'image/probe.jpg'
        self.b_color, self.g_color, self.r_color = 0, 0, 0
        self.b_color_delta, self.g_color_delta, self.r_color_delta = 0, 0, 0

    def draw_postcard(self):
        image = cv2.imread(self.blank)
        height, width = image.shape[0], image.shape[1]
        foo = 3
        if foo == 1:
            self.b_color, self.g_color, self.r_color = 0, 255, 255
            self.b_color_delta, self.g_color_delta, self.r_color_delta = round(255/height, 2), 0, 0
        elif foo == 2:
            self.b_color, self.g_color, self.r_color = 255, 0, 0
            self.b_color_delta, self.g_color_delta, self.r_color_delta = 0, round(255/height, 2), round(255/height, 2)
        elif foo == 3:
            self.b_color, self.g_color, self.r_color = 255, 170, 85
            self.b_color_delta, self.g_color_delta, self.r_color_delta = 0, round((255 - 170) / height, 2), 0
        else:
            self.b_color, self.g_color, self.r_color = 133, 133, 133
            self.b_color_delta, self.g_color_delta, self.r_color_delta = round((255 - 133) / height, 2), round((255 - 133) / height, 2), round((255 - 133) / height, 2)
        for x in range(0, width):
            for y in range(0, height):
                image[y, x] = [self.b_color, self.g_color, self.r_color]
                self.b_color += self.b_color_delta
                self.g_color += self.g_color_delta
                self.r_color += self.r_color_delta


        cv2.putText(image, self.date, (80, 80), cv2.FONT_HERSHEY_COMPLEX, 2, cv2.COLOR_BAYER_BG2RGB)
        cv2.imshow('Test', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    card = ImageMaker()
    card.draw_postcard()