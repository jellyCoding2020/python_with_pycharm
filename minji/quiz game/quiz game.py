from guizero import App, Box, PushButton, Text, TextBox

app = App(width=700)


questions_bio = ['다음 중 음식물이 직접 지나가지 않는 소화 기관은 무엇인가?',
                 '다음 중 녹말 분해 효소는 무엇인가?',
                 '다음 중 호흡 기관에 포함되지 않는 것은?',
                 '다음 중 배설과정과  관련이 없는 것은?',
                 '다음 중 동물에겐 있지만 식물에겐 없는 것은?']

answer1 = ['입', '트립신', '폐', '콩팥', '세포']
answer2 = ['위', '펩신', '기관', '오줌관', '개체']
answer3 = ['소장', '라이페이스', '코', '세뇨관', '기관']
answer4 = ['간', '아밀레이스', '입', '대장', '기관계']

questions_hist = ['과거 송나라의 황제가 무신을 무시하고 문신을 우대한 정책은?',
                  '세상에서 가장 넓은 땅을 보유했었던 몽골 제국의 첫번째 왕은?',
                  '최초로 세계 일주를 성공한 사람은?',
                  '아메리카 대륙을 최초로 발견한 사람은?']
answer_description = ['문치주의', '칭기즈칸', '마젤란', '콜럼버스']

class quiz():
    def __init__(self, quiz, ans1=[],ans2=[],ans3=[],ans4=[], type=1, answer=[]):
        self.questions = quiz
        self.type = type
        if type == 1:
            print('객관식 문제 객체 만들기')
            self.answer1 = ans1
            self.answer2 = ans2
            self.answer3 = ans3
            self.answer4 = ans4
        else :
            print('주관식 문제 객체 만들기')
            self.answer = answer

        self.question_number = 1
        self.layoutType = type


    def show_UI_main(self):
        pass

    def show_UI_quiz(self):
        self.message = Text(app, text=self.questions[self.question_number - 1], size=10)
        self.check = 0

        self.button_box = Box(app, layout="grid")
        if self.type == 1:
            self.button1 = PushButton(self.button_box, text=self.answer1[self.question_number - 1], grid=[0, 0])
            self.button2 = PushButton(self.button_box, text=self.answer2[self.question_number - 1], grid=[0, 5])
            self.button3 = PushButton(self.button_box, text=self.answer3[self.question_number - 1], grid=[1, 0])
            self.button4 = PushButton(self.button_box, text=self.answer4[self.question_number - 1], grid=[1, 5], command=self.correct)

            self.button1.tk.grid(padx=10, pady=20)
            self.button2.tk.grid(padx=30, pady=10)
            self.button3.tk.grid(padx=30, pady=10)
            self.button4.tk.grid(padx=10, pady=20)
        else :
            self.userAnswer = TextBox(self.button_box, grid=[1, 0])

        self.button5 = PushButton(self.button_box, text="다음 문제", grid=[4, 10], command=self.next_qna)
        self.button6 = PushButton(self.button_box, text="이전 문제", grid=[1, 10], command=self.pior_qna)
        self.button7 = PushButton(self.button_box, text="확인하기", grid=[6, 10], command=self.check_answer)
        #self.check_button1()

    def check_answer(self):
        print("bbbbb")
        if self.userAnswer.value == self.answer[self.question_number - 1]:
            print("텍스트 상자의 내용:", self.userAnswer)
            self.correct()
        else:
            self.wrong()

    def correct(self):
        self.message.value = "정답!"
        self.message.text_color = "green"

    def wrong(self):
        self.message.value = "오답!"
        self.message.text_color = "red"

    def next_qna(self):
        self.question_number += 1
        self.message.value = self.questions[self.question_number-1]

        if self.type == 1:
            self.button1.text = self.answer1[self.question_number-1]
            self.button2.text = self.answer2[self.question_number - 1]
            self.button3.text = self.answer3[self.question_number - 1]
            self.button4.text = self.answer4[self.question_number - 1]
        else :
            self.userAnswer.value = ''

        self.message.text_color = "black"
    def pior_qna(self):
        if self.question_number > 1:
            self.question_number -= 1
            self.message.value = self.questions[self.question_number-1]
    def check_button1(self):
        while True:
            if self.button1.value == 1:
                print("Button is pressed")

    #def __del__(self):
    #    print('bye')
     #   self.button5.destroy()

#biologi_quiz = quiz(questions_bio, answer1, answer2, answer3, answer4)

#biologi_quiz.show_UI_main()
#biologi_quiz.show_UI_quiz()

hist_quiz = quiz(questions_hist, type=2, answer = answer_description)
hist_quiz.show_UI_quiz()

app.display()

#del biologi_quiz