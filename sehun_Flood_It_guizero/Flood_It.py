from guizero import App, Waffle, Text, PushButton, info
from random import randint, choice
#---------  변수 선언 --------------------------------------------
colours = ["white", "black", "red",
           "green", "blue", "cyan", "yellow", "magenta"]

board_size = 16
moves_limit = 4

palette = Waffle
width = 6 #너비가 6
height = 1 #높이가 1
dotty = True

#------함수 선언 ------------------------------------------------
def fill_board():
  for 
    board.set_pixel(0, 0, choice(colours))


#-----메인 코드 시작 --------------------------------------------
application  = App("Flood it")

board = Waffle(application, width=board_size, height=board_size, pad=0)
palette = Waffle(application, width=6, height=1, dotty=True)

fill_board()

application.display()

