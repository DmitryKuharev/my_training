import cv2
import os

WEATHER = {'Sun.jpg': 'солнечно, ясно, малооблачно, облачно с прояснениями',
           'Rain.jpg': 'дождь, небольшой дождь, град, ливень, гроза',
           'Snow.jpg': 'снег, мокрый снег, снег с дождем, снегопад , обледенение, метель',
           'Cloud.jpg': 'облачно, пасмурно, туман'
           }


class ImageMaker:
    def __init__(self):
        self.blank = 'image/probe.jpg'
        self.b_color, self.g_color, self.r_color = 0, 0, 0
        self.b_color_delta, self.g_color_delta, self.r_color_delta = 0, 0, 0
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.color = cv2.COLOR_BAYER_BG2RGB
        self.mockup_dict = {0: 'Sun.jpg', 1: 'Rain.jpg', 2: 'Snow.jpg', 3: 'Cloud.jpg'}

    def make_mockup(self):
        image = cv2.imread(self.blank)
        height, width = image.shape[0], image.shape[1]
        icon = cv2.imread('image/sun.png')
        for mockup_number in range(4):
            if mockup_number == 0:
                self.b_color, self.g_color, self.r_color = 0, 255, 255
                self.b_color_delta, self.g_color_delta, self.r_color_delta = round(255 / height, 2), 0, 0
            elif mockup_number == 1:
                self.b_color, self.g_color, self.r_color = 255, 0, 0
                self.b_color_delta, self.g_color_delta, self.r_color_delta = 0, round(255 / height, 2), round(
                    255 / height, 2)
                icon = cv2.imread('image/rain.png')
            elif mockup_number == 2:
                self.b_color, self.g_color, self.r_color = 255, 170, 85
                self.b_color_delta, self.g_color_delta, self.r_color_delta = 0, round((255 - 170) / height, 2), round(
                    (255 - 85) / height, 2),
                icon = cv2.imread('image/snow.png')
            elif mockup_number == 3:
                self.b_color, self.g_color, self.r_color = 120, 120, 120
                self.b_color_delta, self.g_color_delta, self.r_color_delta = round((255 - 120) / height, 2), round(
                    (255 - 120) / height, 2), round((255 - 120) / height, 2)
                icon = cv2.imread('image/cloud.png')
            for x in range(0, width):
                if mockup_number == 2:
                    self.b_color, self.g_color, self.r_color = 255, 170, 85
                elif mockup_number == 3:
                    self.b_color, self.g_color, self.r_color = 120, 120, 120
                for y in range(0, height):
                    image[y, x] = [self.b_color, self.g_color, self.r_color]
                    self.b_color += self.b_color_delta
                    self.g_color += self.g_color_delta
                    self.r_color += self.r_color_delta
            roi = image[0:icon.shape[0], int(width - icon.shape[1]):width]
            icon_gray = cv2.cvtColor(icon, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(icon_gray, 10, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            icon_fg = cv2.bitwise_and(icon, icon, mask=mask)
            dst = cv2.add(img_bg, icon_fg)
            image[0:icon.shape[0], int(width - icon.shape[1]):width] = dst
            cv2.imwrite(self.mockup_dict[mockup_number], image)

    def draw_postcard(self, data: dict):
        check_img = []
        for value in self.mockup_dict.values():
            check_img.append(os.path.exists(value))
        if False in check_img:
            self.make_mockup()
        for key, value in WEATHER.items():
            if data["weather"].lower() in value:
                self.blank = key
        else:
            print(f'Данную погоду "{data["weather"].lower()}" необходимо добавить в нужный раздел переменной WEATHER ')
        image = cv2.imread(self.blank)
        cv2.putText(image, f'{data["date"]}', (210, 30), self.font, 1, self.color)
        cv2.putText(image, 'Погода', (50, 30), self.font, 1, self.color)
        cv2.putText(image, f'Температура днем: {data["t_day"]}', (5, 90), self.font, 1, self.color)
        cv2.putText(image, f'Температура ночью: {data["t_night"]}', (5, 140), self.font, 1, self.color)
        cv2.putText(image, f'{data["weather"]}', (5, 190), self.font, 1, self.color)
        cv2.putText(image, 'У природы нет плохой погоды!', (80, 245), self.font, 0.6, self.color)
        cv2.imshow('Test', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
