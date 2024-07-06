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
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()


leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20),
              (6, 18), (2, 14))
t.register_shape('my_leaf', leaf_shape)
leaf.shape('my_leaf')
leaf.color('#003300','#99ff99')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)


game_started = False
text_turtle=t.Turtle()
text_turtle.write('press SPACE', align='center',
                  font=('arial',16,'bold'))
text_turtle.hideturtle()

score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)


t.mainloop()

