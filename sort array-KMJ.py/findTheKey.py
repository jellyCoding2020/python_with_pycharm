#--------------------------While version---------------------------
class box:
  def __init__(self, things, name, inMyBox):
    self.__things = things
    self.__Name = name
    self.__item = inMyBox

  def getItem(self):
      return self.__item

  def getName(self):
      return self.__Name

  def getThings(self):
      return self.__things

  def is_a_key(self):
      if self.__things != 'key':
          return False
      else :
          return True

  def is_a_box(self):
      if len(self.__item) != 0:
          return True
      else:
          return False


  def append_box(self, newBox):
      self.__item.append(newBox)

  def __str__(self):
      return '<'+self.__Name+ ' : ' + self.getThings()+'>'



smallBox1 = box('key', 's1box', [])
smallBox2 = box('milk', 's2box', [])

medium_Box1 = box('pen', 'm2box', [])
medium_Box2 = box('cheese', 'm1box', [smallBox2, smallBox1])
BigBox = box('book', 'BigBox', [medium_Box1, medium_Box2])

print(BigBox.is_a_box() )

#medium_Box1 = [smallBox1, smallBox2]
#medium_Box2 = []
#BigBox =[medium_Box1, medium_Box2]



def look_for_key_recursion(box):
    for item in box.getItem():
        if item.is_a_box():
            look_for_key_recursion(item)
        elif item.is_a_key():
            print('find the key in {}'.format(item.getName()))
        else:
            print(item)



#-------------------------
#------main code----------
look_for_key_recursion(BigBox)
#-------------------------





def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                print('It Is not Key')
                pile.append(item)
            elif item.is_a_key():
                print("find the key!")