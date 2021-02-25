from display import *
from draw import *

s = new_screen()
c = [255, 0, 0]

# roof
for x in range(500):
    y1 = 300 + 0.5 * x
    if 150 < x <= 350:
        y1 = 300 + 75
    if x > 350:
        y1 = 300 + 0.5 * (XRES - x)
    draw_line(x, 300, x, y1, s, c)

# base
c[GREEN] = 255
c[BLUE] = 255
for x in range(50, 449):
    draw_line(x, 0, x, 300, s, c)

# windows
c[RED] = 135
c[GREEN] = 206
c[BLUE] = 235

for x in range(112, 162):
    y0 = 230 - 2 * (x - 112)
    y1 = 230 + 2 * (x - 112)
    if x >= 137:
        y0 = 230 - 2 * (162 - x)
        y1 = 230 + 2 * (162 - x)
    draw_line(x, y0, x, y1, s, c)
    draw_line(XRES - x, y0, XRES - x, y1, s, c)

# window lines
c[RED] = 0
c[GREEN] = 0
c[BLUE] = 0
for x in range(135, 139):
    draw_line(x, 182, x, 278, s, c)
    draw_line(XRES - x - 1, 182, XRES - x - 1, 278, s, c)
for y in range(229, 233):
    draw_line(112, y, 162, y, s, c)
    draw_line(XRES - 112, y, XRES - 162, y, s, c)

# door
c[RED] = 150
c[GREEN] = 75
c[BLUE] = 0
for x in range(225, 274):
    draw_line(x, 0, x, 100, s, c)

# chimney
for x in range(321, 341):
    draw_line(x, 376, x, 425, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')