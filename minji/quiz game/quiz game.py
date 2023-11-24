from guizero import App, Box, PushButton, Text



app = App()

questions = ['다음 중 음식물이 직접 지나가지 않는 소화 기관은 무엇인가?', '다음 중 쓸개즙을 만드는 곳은 어디인가?']
answer1 = ['입', '쓸개']

message = Text(app, text=questions[0], size=12)

answer = 0
def correct():
    message.value = "정답!"
    message.text_color = "green"
def next_qna(answer):
    message.value = questions[0+1]
    message.text_color = "black"
    answer += 1

button_box = Box(app, layout="grid")

button1 = PushButton(button_box, text=answer1[answer], grid=[0, 0])
button2 = PushButton(button_box, text="위", grid=[0, 5])
button3 = PushButton(button_box, text="소장", grid=[1, 0])
button4 = PushButton(button_box, text="간", grid=[1, 5], command=correct)
button5 = PushButton(button_box, text="다음 문제", grid=[4, 10], command=next_qna)

button1.tk.grid(padx=10, pady=20)
button2.tk.grid(padx=30, pady=10)
button3.tk.grid(padx=30, pady=10)
button4.tk.grid(padx=10, pady=20)





app.display()