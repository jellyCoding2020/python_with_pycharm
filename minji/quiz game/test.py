
from guizero import App, PushButton

def toggle_button_state():
    if button.enabled:
        button.disable()
        button.text = "Disabled"
    else:
        button.enable()
        button.text = "Enabled"

app = App("Enabled Example")

button = PushButton(app, text="Enabled", command=toggle_button_state)

app.display()
