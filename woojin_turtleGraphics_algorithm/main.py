import turtle as t

t.shape('circle')
def draw_rectangle(width, height, color , xtz , ytz, s):
    t.penup()
    t.goto(xtz, ytz)
    t.pendown()
    t.pensize(2)
    t.color(color)
    t.begin_fill()
    t.speed(s)
    for counter in range(1, 3):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(0,0)



while True:
    width = int(input("w: "))
    height = int(input("h: "))
    xtz = int(input("x: "))
    ytz = int(input("y: "))
    s = int(input("s: "))
    draw_rectangle(width, height, "black", xtz, ytz, s)
    print(xtz)
    print(ytz)