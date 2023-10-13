from random import randint
print('유령 게임')
feeling_brave =True
score = 0
while feeling_brave:
    ghost_door = randint(1,3)
    print('문이 3개 있다.')
    print('3개의 문 중 1개의 문 뒤에 유령이 있다.')
    print('몇 번 문을 열 것인가?')
    door = input('1,2, 아니면 3 ?')
    door_num = int(door)
    if door_num == ghost_door:
      print('유령이다!')
      feeling_brave = False
    else:
       print('유령이 없다!')
       print('옆방으로 들어가라.')
       score = score + 1
print('도망쳐!')
print('Game over! 점수는',score)