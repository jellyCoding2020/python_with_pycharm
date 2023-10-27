from tkinter import Tk, simpledialog, messagebox

print('Ask the Expert - Capital Cities of the World')
root = Tk()
root.withdraw()

the_world = {}

def read_from_flie():
    with open('capital_data.txt') as flie:
        i = 1
        for line in flie:
            line = line.rstrip('\n')
            country, city = line.split('/')
            print(i, country, city)
            i=i+1

read_from_flie()
