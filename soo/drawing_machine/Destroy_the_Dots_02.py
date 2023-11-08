from guizero import App, Text, Waffle
from random import randint

GRID_SIZE = 5


app = App("Destroy the dots")
instuctions = Text(app, text="Click the dots to destroy them")
#board = Waffle(app, width=5, height=5)

def app_dot():
    x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    while board[x, y].dotty == True:
        x, y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    board[x, y].dotty = True
    board.set_pixel(x, y, "red")

def destroy_dot(x,y):
    if board[x,y].dotty == True:
        board[x,y].dotty == False
        board.set_pixel(x, y, "white")
        board.after(1000, app_dot)

board = Waffle(app, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)





app.display()