import turtle as t
from itertools import cycle


colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white'])
t.bgcolor('black')
def circle(size, angle, shift, bgg):
    t.speed(0)
    t.pensize(bgg)
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    circle(size + 0.7, angle + 0.5, shift + 1, bgg + 0.05)

t.goto(0, 70)
circle(4, 1, 0, 0.2)






