from guizero import App,PushButton,TextBox,Text

def button_clicked(button):
    print(f"{button.text}부분을 눌렀습니다.")

def tebox():
    big_result.value = update_text.value

app = App(title="caculator")
big_result = Text(app, text="Welcome to my caculator")
update_text = TextBox(app,command=tebox,text=7,grid=[3,4])

Button1 = PushButton(app, command=button_clicked, text= "버튼1",grid=[100,4])
Button2 = PushButton(app, command=button_clicked, text= "+")
Button3 = PushButton(app, command=button_clicked, text= "-")
Button4 = PushButton(app, command=button_clicked, text= "=")
Button5 = PushButton(app, command=button_clicked, text= "X")
app.display()