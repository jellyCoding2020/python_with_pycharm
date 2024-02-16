from guizero import App,PushButton,TextBox,Text,Box
three = 3
two = 2
Calc = []


def split_operand(equation, op1, op2):
        operand_list = []
        temp1 = equation.split(op1)

        operand_list.append( int(temp1[0])   )

        temp2 = temp1[1].split(op2)

        operand_list.append(int(temp2[0]))
        operand_list.append(int(temp2[1]))

        numOfOperand = len(operand_list)

        print('피연산자의 개수 = ', numOfOperand)
        print('피연산자 {}'.format(operand_list))

        return operand_list

def button_clicked(buttonText):
    global math_operation

    print(f"{buttonText}부분을 눌렀습니다.")
    if buttonText == '1':
        update_text.value = update_text.value + str(1)
    elif buttonText == '2':
        update_text.value = update_text.value + str(2)
    elif buttonText == '3':
        update_text.value = update_text.value + str(3)
    elif buttonText == '4':
        update_text.value = update_text.value + str(4)
    elif buttonText == '5':
        update_text.value = update_text.value + str(5)
    elif buttonText == '6':
        update_text.value = update_text.value + str(6)
    elif buttonText == '7':
        update_text.value = update_text.value + str(7)
    elif buttonText == '8':
        update_text.value = update_text.value + str(8)
    elif buttonText == '9':
        update_text.value = update_text.value + str(9)
    elif buttonText == '0':
        update_text.value = update_text.value + str(0)
    elif buttonText == '+':
        update_text.value = update_text.value + str("+")
        Calc.append('+')
        math_operation = '+'



    elif buttonText == '-':
        update_text.value = update_text.value + str("-")
        Calc.append('-')
        math_operation = '-'

    elif buttonText == 'X':
        update_text.value = update_text.value + str("*")
        Calc.append('*')
        math_operation = '*'
    elif buttonText == '%':
        update_text.value = update_text.value + str("%")
        math_operation = '%'
    elif buttonText == '.':
        update_text.value = update_text.value + str(".")
    elif buttonText == '=':
        if len(Calc) >= 2:
            Cal1, Cal2 = Calc
            print(Cal1, Cal2)

        operand_list = split_operand(update_text.value, Cal1, Cal2 )
        numOfOperand = len(operand_list)
        if Cal1 == '+':
          a1 = operand_list[0] + operand_list[1]
        elif Cal1 == '-':
          a1 = operand_list[0] - operand_list[1]
        elif Cal1 == '*':
          a1 = operand_list[0] * operand_list[1]
        elif Cal1 == '/':
          a1 = operand_list[0] / operand_list[1]


        if Cal2 == '+':
          y = a1 + operand_list[2]
        elif Cal2 == '-':
          y = a1 - operand_list[2]
        elif Cal2 == '*':
          y = a1 * operand_list[2]
        elif Cal2 == '/':
          y = a1 / operand_list[2]

        '''for operand in operand_list:
            if math_operation == '+':
                result = result + int(operand)
            elif math_operation == '-':
                result = result - int(operand)'''


        update_text.value = str(y)

        #update_text.value = 2
         #if buttonText == 'X':
             #update_text.value = str( int(update_text.value) * 2 )

def tebox():
    big_result.value = update_text.value

app = App(title="caculator",height=500,width=1000,layout="grid")
box = Box(app, layout= "grid", grid=[1,1])
big_result = Text(app, text="Welcome to my caculator",grid=[20,0])
update_text = TextBox(app,command=tebox,width=100,height=100,text='',grid=[3,4])



Button1 = PushButton(app, command=button_clicked, args = ["1"], text= "1",width=8,height=4,grid=[100,40])
Button2 = PushButton(app, command=button_clicked, args = ["+"],text= "+",width=8,height=4,grid=[110,40])
Button3 = PushButton(app, command=button_clicked, args = ["-"], text= "-",width=8,height=4,grid=[110,41])
Button4 = PushButton(app, command=button_clicked, args = ["="], text= "=",width=8,height=4,grid=[110,43])
Button5 = PushButton(app, command=button_clicked, args = ["X"], text= "X",width=8,height=4,grid=[110,42])
Button6 = PushButton(app, command=button_clicked, args = ["2"], text= "2",width=8,height=4,grid=[101,40])
Button7 = PushButton(app, command=button_clicked, args = ["3"], text= "3",width=8,height=4,grid=[102,40])
Button8 = PushButton(app, command=button_clicked, args = ["4"], text= "4",width=8,height=4,grid=[100,41])
Button9 = PushButton(app, command=button_clicked, args = ["5"], text= "5",width=8,height=4,grid=[101,41])
Button10 = PushButton(app, command=button_clicked, args = ["6"], text= "6",width=8,height=4,grid=[102,41])
Button11= PushButton(app, command=button_clicked, args = ["7"], text= "7",width=8,height=4,grid=[100,42])
Button12 = PushButton(app, command=button_clicked, args = ["8"], text= "8",width=8,height=4,grid=[101,42])
Button13 = PushButton(app, command=button_clicked, args = ["9"], text= "9",width=8,height=4,grid=[102,42])
Button14 = PushButton(app, command=button_clicked, args = ["0"], text= "0",width=8,height=4,grid=[100,43])
Button15 = PushButton(app, command=button_clicked, args = ["."], text= ".",width=8,height=4,grid=[101,43])
Button16 = PushButton(app, command=button_clicked, args = ["%"], text= "%",width=8,height=4,grid=[102,43])
app.display()