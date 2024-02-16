from guizero import App, Waffle
import random
from time import sleep

colours = ["red", "blue"]


board_size = 16

def fill_board():
    for x in range(board_size):
      for y in range(int(board_size/2)):
        board.set_pixel(x, y, random.choice(colours))
      #leep(0.5)


app = App("Flood It")




board = Waffle(app,
               width=board_size,
               height=board_size,
               pad=0)

fill_board()

palette = Waffle(app, width=6, height=1, dotty=True)






app.display()