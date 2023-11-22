print('hello')

from guizero import App, Box, PushButton

app = App("My App")

button_box = Box(app, layout="grid")

button1 = PushButton(button_box, text="Button 1", grid=[0, 0])
button2 = PushButton(button_box, text="Button 2", grid=[0, 5])
button3 = PushButton(button_box, text="Button 3", grid=[1, 0])
button4 = PushButton(button_box, text="Button 4", grid=[1, 5])

button1.tk.grid(padx=10, pady=10)
button2.tk.grid(padx=10, pady=10)
button3.tk.grid(padx=10, pady=10)
button4.tk.grid(padx=10, pady=10)

app.display()