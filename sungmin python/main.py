from tkinter import Tk, simpledialog, messagebox

print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()

the_world = {}

def read_from_flie():
    with open('capital_data.txt') as flie:
        i = 1
        for line in flie:#파일에 줄을 알려줌
            line = line.rstrip('\n') #line 값에 인자된 모든 값을 제거
            country, city = line.split('/')#
            print(i, country, city)# 괄호안에 있는 것들을 출력한다
            i=i+1

read_from_flie()