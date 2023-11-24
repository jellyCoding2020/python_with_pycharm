from guizero import App, Box, PushButton, Text

app = App()


questions_bio = ['다음 중 음식물이 직접 지나가지 않는 소화 기관은 무엇인가?',
                 '다음 중 녹말 분해 효소는 무엇인가?',
                 '다음 중 호흡 기관에 포함되지 않는 것은?',
                 '다음 중 배설과정과  관련이 없는 것은?']

answer1 = ['입', '트립신', '폐', '콩팥']
answer2 = ['위', '펩신', '기관', '오줌관']
answer3 = ['소장', '라이페이스', '코', '세뇨관']
answer4 = ['간', '아밀레이스', '입', '대장']



class quiz():
    def __init__(self, quiz, ans1,ans2,ans3,ans4):
        self.questions = quiz
        self.answer1 = ans1
        self.answer2 = ans2
        self.answer3 = ans3
        self.answer4 = ans4
        self.question_number = 1


    def show_UI_main(self):
        pass

    def show_UI_quiz(self):
        self.message = Text(app, text=self.questions[self.question_number - 1], size=12)

        self.button_box = Box(app, layout="grid")

        self.button1 = PushButton(self.button_box, text=self.answer1[self.question_number - 1], grid=[0, 0])
        self.button2 = PushButton(self.button_box, text=self.answer2[self.question_number - 1], grid=[0, 5])
        self.button3 = PushButton(self.button_box, text=self.answer3[self.question_number - 1], grid=[1, 0])
        self.button4 = PushButton(self.button_box, text=self.answer4[self.question_number - 1], grid=[1, 5], command=self.correct)
        self.button5 = PushButton(self.button_box, text="다음 문제", grid=[4, 10], command=self.next_qna)
        self.button1.tk.grid(padx=10, pady=20)
        self.button2.tk.grid(padx=30, pady=10)
        self.button3.tk.grid(padx=30, pady=10)
        self.button4.tk.grid(padx=10, pady=20)

        #self.check_button1()

    def correct(self):
        self.message.value = "정답!"
        self.message.text_color = "green"

    def next_qna(self):
        self.question_number += 1
        self.message.value = self.questions[self.question_number-1]
        self.button1.text = self.answer1[self.question_number-1]
        self.button2.text = self.answer2[self.question_number - 1]
        self.button3.text = self.answer3[self.question_number - 1]
        self.button4.text = self.answer4[self.question_number - 1]
        self.message.text_color = "black"

    def check_button1(self):
        while True:
            if self.button1.value == 1:
                print("Button is pressed")

biologi_quiz = quiz(questions_bio, answer1, answer2, answer3, answer4)

#biologi_quiz.show_UI_main()
biologi_quiz.show_UI_quiz()

app.display()


