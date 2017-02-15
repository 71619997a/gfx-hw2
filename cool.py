from line import line
from base import Image

img = Image(500, 500)
y = lambda x: 500 * (x/250. - 1)**2
dy = lambda x: 4 * (x/250. - 1)
xs = range(0, 501, 4)
ys = [y(x) for x in xs]
xys = zip(xs, ys)
points = []
for x, y in xys:
    slope = dy(x)
    y0 = int(-slope * x + y)
    y500 = int(slope * (500 - x) + y)
    pts = line(0, y0, 500, y500)
    pts = filter(lambda tup: 500 > tup[0] >= 0 and 500 > tup[1] >= 0, pts)
    coloredpoints = [(px, py, (x / 2, y / 2, (x + y) / 4)) for px, py in pts]
    points.extend(coloredpoints)
img.setPixels(points)
img.saveAs('cool.png')
img.display()
