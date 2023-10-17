from turtle import *

def turtle_controller(do, val=0):
    do = do.upper()
    if do == 'F':
        print("hello")
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Unrecognized command')

def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)


instructions = '''거북이에게 명령을 내려주세요:
예 F100-R45-U-F100-L45-D-F100-R90-B50
N = 새로 그리기
U/D = 펜 올리기/ 펜 내리기
F100 = 앞으로 100 가기
B50 = 뒤로 50 가기
R90 = 오른쪽으로 90도 회전
L45 = 왼쪽으로 45도 회전'''
screen = getscreen()
past_program = ""
while True:
    t_program = screen.textinput('그림 그리는 기계', instructions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    elif t_program.upper() == "REPLAY":
        t_program = past_program

    string_artist(t_program)
    past_program = t_program

'''
turtle_controller('d')
turtle_controller('F', 150)
turtle_controller('l', 120)
turtle_controller('f', 150)
turtle_controller('l', 120)
turtle_controller('f', 150)
'''

while True:
    pass
