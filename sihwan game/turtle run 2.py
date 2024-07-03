from turtle import *
import turtle as t


def write_a():
    t.write('밥동고리', font='나눔명조')


def write_q():
    t.write('qwer!', font='나눔고딕')
def go_right():
    t.setheading(0)
    t.fd(100)


def go_up():
    t.setheading(90)
    t.fd(100)


def go_left():
    t.setheading(180)
    t.fd(100)

def go_down():
    t.setheading(270)
    t.fd(100)




t.shape('turtle')
t.onkeypress(go_right, 'Right')
t.onkeypress(go_up, 'Up')
t.onkeypress(go_left, 'Left')
t.onkeypress(go_down, 'Down')
t.onkeypress(write_a, 'a')
t.onkeypress(write_q, 'q')


t.listen()
t.mainloop()