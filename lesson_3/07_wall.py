import simple_draw as sd

sd.resolution = (600, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

width = 100
height = 50
y = 0
y1 = height
for i in range(12):
    start = sd.get_point(0, y)
    end = sd.get_point(600, y)
    sd.line(start, end, width=4)
    if i % 2 == 0:
        x1 = 0
        x2 = 0
        for _ in range(7):
            start = sd.get_point(x1, y)
            end = sd.get_point(x2, y + y1)
            sd.line(start, end, width=4)
            x1 += width
            x2 += width
    else:
        x1 = width/2
        x2 = width/2
        for _ in range(7):
            start = sd.get_point(x1, y)
            end = sd.get_point(x2, y + y1)
            sd.line(start, end, width=4)
            x1 += width
            x2 += width
    y += height
sd.pause()
