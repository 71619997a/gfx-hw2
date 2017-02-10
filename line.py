import math
from draw import Image
from sys import argv

def line(x0, y0, x1, y1):
    pts = []
    x = x0
    y = y0
    a = 2 * (y1 - y0)
    b = x0 - x1
    d = a + b
    b *= 2
    while x <= x1:
        pts.append((x, y))
        if d > 0:
            y += 1
            d += b
        x += 1
        d += a
    print pts
    return pts

img = Image(1000, 500)
for pt in line(*[int(i) for i in argv[1:]]):
    img.setPix(pt[0],pt[1],(255,0,0))

img.drawTo("line1.ppm")
