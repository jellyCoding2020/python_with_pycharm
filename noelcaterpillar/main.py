import turtle as t
window = t.Screen()
window.title('창을 닫으려면 아무 버튼이나 눌러 주세요:')
def close_window():
    window.bye()

window.listen()
window.onkeypress(close_window)

caterpillar=t.Turtle()
caterpillar.shape('square')
caterpillar.color('blue')
caterpillar.
t.mainloop()

