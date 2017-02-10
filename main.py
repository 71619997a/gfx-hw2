import math
from base import Image
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
    return pts

img = Image(1000, 500)
if len(argv) < 6:
    print 'Usage: python main.py <display | save | saveconv> <x1> <y1> <x2> <y2>'
    exit(1)
for pt in line(*[int(i) for i in argv[2:]]):
    img.setPixel(pt[0], 499 - pt[1], (255,0,0))

if argv[1] == 'display':
    img.display()
elif argv[1] == 'save':
    img.savePpm('line.ppm')
elif argv[1] == 'saveconv':
    img.saveAs('line.png')
else:
    print 'Usage: python main.py <display | save | saveconv> <x1> <y1> <x2> <y2>'
