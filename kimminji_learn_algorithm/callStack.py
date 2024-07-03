def greet(name):
    print ("Nice to meet you," + name + "!")
    greet2(name)
    print("Getting ready to say bye...")
    bye(name)

def greet2(name):
    print("How are you," + name + "?")

def bye(name):
    print("Ok, " + name +  " bye!")


greet("Mack")


