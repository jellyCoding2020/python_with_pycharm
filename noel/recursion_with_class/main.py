class box:
    def __init__(self,name,item,baby):
        self.name=name
        self.item=item
        self.baby_box=[]

    def is_a_key(self):
        if self.item=='key':

    def is_a_box(self):
        if self.item=='box':


A_box=box('A박스','key')
main_box=box('매인 박스','box',)