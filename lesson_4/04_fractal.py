# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)

point_s = sd.get_point(600, 0)


def draw_branches(point, angle, length):
    if length < 10:
        return
    v = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v.draw()
    next_point = v.end_point
    next_angle = angle - sd.random_number(18, 42)
    next_length = length * 0.75
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    next_angle = angle + sd.random_number(18, 42)
    next_length = length * 0.8
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    # next_length = length * 0.75
    # draw_branches(point=next_point, angle=next_angle, length=next_length)


draw_branches(point=point_s, angle=90, length=200)
# for i in range(150, 0, -30):
#     draw_branches(point=point_s, angle=i, length=80)


sd.pause()


