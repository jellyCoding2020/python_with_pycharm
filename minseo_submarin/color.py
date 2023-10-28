from tkinter import *
from random import *


size = 500
window = Tk()
canvas = Canvas(window, width=size*2, height=size)
canvas.pack()

n = 90
while n<100:
    col = choice(['pink','orange', 'purple', 'yellow'])
    x0 = randint(0,size*2)
    y0 = randint(0,size)
    d = randint(0, size/5)
    canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=col)
    window.update()
    n +=1

window.mainloop()

