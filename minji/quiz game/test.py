from guizero import App, Window, PushButton

def show_tab1():
    tab1.show()

def show_tab2():
    tab2.show()

app = App("Tab Example")

# Create two windows (tabs)
tab1 = Window(app, "Tab 1")
tab2 = Window(app, "Tab 2")

# Create buttons to switch between tabs
button_tab1 = PushButton(app, show_tab1, text="Tab 1")
button_tab2 = PushButton(app, show_tab2, text="Tab 2")

# Initially show the first tab
show_tab1()

app.display()
