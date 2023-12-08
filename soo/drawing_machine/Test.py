from guizero import App, Box, Text

app = App(title="Test", height=300, width=400)
box = Box(app)
text1 = Text(box, text="이건 테스트 용도임", size=14, color="red", font="Arial")
text2 = Text(app, text="이것 역시 테스트 용도임", size=14, color="blue", font="Courier New")
app.display()