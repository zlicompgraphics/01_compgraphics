from display import *


def draw_line(x0, y0, x1, y1, screen, color):
    x0 = round(x0)
    x1 = round(x1)
    y0 = round(y0)
    y1 = round(y1)
    if x1 < x0:  # start from left to right
        tempX = x0
        tempY = y0
        x0 = x1
        y0 = y1
        x1 = tempX
        y1 = tempY
    deltaY = y1 - y0
    deltaX = x1 - x0
    d = 2 * deltaY + -deltaX  # starting midpoint
    if deltaX == 0:  # vertical line
        while y0 <= y1:
            plot(screen, color, x0, y0)
            y0 += 1
        return
    slope = deltaY/deltaX
    if 0 <= slope <= 1:  # octants 1 and 5, slope of 1, horizontal lines
        while x0 <= x1:
            plot(screen, color, x0, y0)
            if d > 0:
                y0 += 1
                d += 2 * -deltaX
            x0 += 1
            d += 2 * deltaY
    elif -1 <= slope < 0:  # octants 8 and 4, slope of -1
        while x0 <= x1:
            plot(screen, color, x0, y0)
            if d < 0:
                y0 -= 1
                d -= 2 * -deltaX
            x0 += 1
            d += 2 * deltaY
    elif slope > 1:  # octants 2 and 6
        while y0 <= y1:
            plot(screen, color, x0, y0)
            if d < 0:
                x0 += 1
                d += 2 * deltaY
            y0 += 1
            d += 2 * -deltaX
    elif slope < -1:  # octants 7 and 3
        while y0 >= y1:
            plot(screen, color, x0, y0)
            if d > 0:
                x0 += 1
                d += 2 * deltaY
            y0 -= 1
            d -= 2 * -deltaX