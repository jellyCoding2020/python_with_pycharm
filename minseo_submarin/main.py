from tkinter import *

def bAaction():
    print('고맙습니다!')
def bBaction():
    print('아얏, 아파요!')

window =Tk()

buttonA = Button(window, text='누르세요!', command=bAaction)
buttonB = Button(window, text='누르지 마세요!', command=bBaction)
buttonA.pack()
buttonB.pack()

window.mainloop()