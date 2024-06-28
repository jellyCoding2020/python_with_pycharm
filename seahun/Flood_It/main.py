#app = App("Flood It")
#board = Waffle(app)
#app.display()




class student:
    def __init__(self, data1, data2, data3, erm):
        self.runData1 = data1
        self.runData2 = data2
        self.runData3 = data3
        self.__name = erm



    def average(self):
        return (self.runData1+self.runData2+self.runData3) / 3

    def get_name(self):
        return self.__name


st1 = student(13.5, 16.6, 12, "chulsoo")
st2 = student(16.5, 9.6, 13.4, "minsoo")


result = st1.average()


print(st1.get_name(), result)

result = st2.average()
print(result)

