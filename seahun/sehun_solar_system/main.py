

class planet:
    def __init__(self, Mass, Name, Distance):
        self.__name = Name
        self.__distance = Distance
        self.mass = Mass
    def get_name(self):
        return self.__name

    def set_name(self, newName):
        self.__name = newName

    def get_Dist(self):
        return self.__distance


Mucury = planet(100, 'M1', 150000)

name = Mucury.get_name()
print(name)

Mucury.set_name('Earth')
name = Mucury.get_name()
print(name)

Mucury.mass = 200