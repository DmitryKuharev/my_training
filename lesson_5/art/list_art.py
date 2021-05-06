import simple_draw as sd

sd.resolution = 1200, 600
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def man(x, y):
    center = sd.get_point(x, y)
    sd.circle(center, 50)
    sd.circle(sd.get_point(x - 25, y + 20), 10)
    sd.circle(sd.get_point(x + 25, y + 20), 10)
    sd.line(sd.get_point(x - 20, y - 25), sd.get_point(x + 20, y - 25))
    sd.line(sd.get_point(x - 35, y - 15), sd.get_point(x - 20, y - 25))
    sd.line(sd.get_point(x + 20, y - 25), sd.get_point(x + 35, y - 15))
    sd.line(sd.get_point(x, y - 50), sd.get_point(x, y-200))
    sd.line(sd.get_point(x, y - 50), sd.get_point(x-50, y-100))
    sd.line(sd.get_point(x, y - 50), sd.get_point(x+50, y-100))
    sd.line(sd.get_point(x, y - 200), sd.get_point(x - 50, y - 300))
    sd.line(sd.get_point(x, y - 200), sd.get_point(x + 50, y - 300))


def rainbow():
    point = sd.get_point(1200, 50)
    radius = 500
    for color in rainbow_colors:
        radius += 5
        sd.circle(center_position=point, radius=radius, color=color, width=6)


def grass():
    sd.line(sd.get_point(0, 0), sd.get_point(sd.resolution[0], 0), color=sd.COLOR_GREEN,  width=100)


def house():
    brick_x, brick_y = 75, 25
    width_wall, height_wall = 500, 300
    layer = 0
    for i in range(0, 1 + height_wall, brick_y):
        layer += 1
        for j in range(100, 101 + width_wall, brick_x):
            j0 = j if layer % 2 else j + brick_x/2
            j1 = width_wall//brick_x * brick_x + 100 + brick_x if layer % 2 else 100
            left_bottom = sd.get_point(j0, i)
            right_top = sd.get_point(j0+brick_x, i + brick_y)
            sd.rectangle(left_bottom, right_top, width=1)
            left_bottom_1 = sd.get_point(j1, i)
            right_top_1 = sd.get_point(j1 + brick_x/2, i + brick_y)
            sd.rectangle(left_bottom_1, right_top_1, width=1)
    sd.line(sd.get_point(100, height_wall+brick_y), sd.get_point(100 + width_wall/2, height_wall + height_wall/2))
    sd.line(sd.get_point(100 + width_wall/2, height_wall + height_wall/2),
            sd.get_point(100 + width_wall + brick_x * 0.8, height_wall + brick_y))


def generate_snow():
    x = sd.random_number(10, 510)
    y = sd.random_number(0, 50)
    length = sd.random_number(10, 20)
    return {'x': x,
            'y': y,
            'length': length}


def snow(center, length):
    sd.snowflake(center, length)


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
