from guizero import App, Waffle
import random
from time import sleep

colours = ["red", "orange", "yellow", "green", "blue", "purple"]


board_size = 16

def fill_board():
    for x in range(board_size):
      for y in range(board_size):
        board.set_pixel(x, y, random.choice(colours))


def init_palette():
    column = 0
    for colour in colours:
        palette.set_pixel(colomn, 0, colour)
        column += 1

        




app = App("Flood It")




board = Waffle(app,
               width=board_size,
               height=board_size,
               pad=0)

fill_board()

palette = Waffle(app, width=6, height=1, dotty=True)






app.display()