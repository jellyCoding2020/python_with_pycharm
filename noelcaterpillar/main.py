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

def outside_window():
    pass
def game_over():
    pass
def display_score(current_score):
    pass
def place_leaf():
    pass
def start_game():
    global game_started
    if game_started:
        return
    game_started=True

    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()


    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length=caterpillar_length+1
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed=caterpillar_speed+1
            score=score+10
            display_score(score)
            if outside_window():
                game_over()
                break
t.mainloop()

