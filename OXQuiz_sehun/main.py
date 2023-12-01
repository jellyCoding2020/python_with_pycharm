WIDTH = 1280
HEIGHT = 720

Question_box = Rect(0, 0, 1000, 240)
OBox = Rect(0, 0, 495, 330)
XBox = Rect(0, 0, 495, 330)

score = 00


q1 = ["Is the '1+2(1+2)=6'?",
      "O", "X", 2]

q2 = ["Is the '3'"]

Question_box.move_ip(50, 40)
OBox.move_ip(50, 358)
XBox.move_ip(735, 358)

def draw():
    screen.fill("yellow")
    screen.draw.filled_rect(Question_box, "sky blue")
    screen.draw.filled_rect(OBox, "orange")
    screen.draw.filled_rect(XBox, "orange")

def game_over():
    pass

def correct():
    pass

def on_mouse_down(pos):
    pass

def update_time_left():
    pass

