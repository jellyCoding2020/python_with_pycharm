from guizero import App,PushButton,TextBox,Text,Box

def button_clicked(buttonText):
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
        
        #update_text.value = 2
         #if buttonText == 'X':
             #update_text.value = str( int(update_text.value) * 2 )

def tebox():
    big_result.value = update_text.value

app = App(title="caculator",height=1000,width=1900,layout="grid")
box = Box(app, layout= "grid", grid=[1,0])
big_result = Text(app, text="Welcome to my caculator",grid=[50,0])
update_text = TextBox(app,command=tebox,width=100,height=100,text='',grid=[3,4])

Button1 = PushButton(app, command=button_clicked, args = ["1"], text= "1",width=8,height=4,grid=[100,40])
Button2 = PushButton(app, command=button_clicked, args = ["+"],text= "+",width=8,height=4,grid=[110,40])
Button3 = PushButton(app, command=button_clicked, args = ["-"], text= "-",width=8,height=4,grid=[110,41])
Button4 = PushButton(app, command=button_clicked, args = ["="], text= "=",width=8,height=4,grid=[110,7])
Button5 = PushButton(app, command=button_clicked, args = ["X"], text= "X",width=8,height=4,grid=[110,42])
Button6 = PushButton(app, command=button_clicked, args = ["2"], text= "2",width=8,height=4,grid=[101,40])
Button7 = PushButton(app, command=button_clicked, args = ["3"], text= "3",width=8,height=4,grid=[102,40])
Button8 = PushButton(app, command=button_clicked, args = ["4"], text= "4",width=8,height=4,grid=[100,41])
Button9 = PushButton(app, command=button_clicked, args = ["5"], text= "5",width=8,height=4,grid=[101,41])
Button10 = PushButton(app, command=button_clicked, args = ["6"], text= "6",width=8,height=4,grid=[102,41])
Button11= PushButton(app, command=button_clicked, args = ["7"], text= "7",width=8,height=4,grid=[100,42])
Button12 = PushButton(app, command=button_clicked, args = ["8"], text= "8",width=8,height=4,grid=[101,42])
Button13 = PushButton(app, command=button_clicked, args = ["9"], text= "9",width=8,height=4,grid=[102,42])
Button14 = PushButton(app, command=button_clicked, args = ["0"], text= "0",width=8,height=4,grid=[100,7])
Button15 = PushButton(app, command=button_clicked, args = ["@"], text= "@",width=8,height=4,grid=[101,7])
app.display()