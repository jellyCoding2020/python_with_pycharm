from turtle import *
def turtle_controller(do, val):
    do = do.upper()
    if do == 'F':
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
    elif do == 'C':
        circle(val)
    else:
        print('Unrecognized command')

def string_artist(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_list == 0:
            command
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        turtle_controller(cmd_type, num)

instrucions = '''거북이에게 명령을 내려 주세요:
예 F100-R45-U-F100-L45-D-F100-R90-B50-C80
N = 새로 그리기
U/D = 펜 올리기/내리기
F100 = 앞으로 100 가기
B50 = 뒤로 50 가기
R90 = 오른쪽으로 90도 회전
L45 = 왼쪽으로 45도 회전
C80 = 반지름이 80 원 그리기'''
screen = getscreen()
while True:
    t_program = screen.textinput('그림 그리는 기계', instrucions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    string_artist(t_program)



