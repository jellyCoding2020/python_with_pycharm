import turtle as t


def rectangle(x, y, horizontal, vertical, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for count in range(2):
        t. forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
