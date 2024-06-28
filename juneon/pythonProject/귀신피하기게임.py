#Ghost game

from random import randint
print('Ghost game')
feeling_brave = True
score = 0

while feeling_brave:
    ghost_door = randint(1, 5)
    print('             ')
    print('문이 5개 있다.')
    print('5개의 문 중 1개의 문뒤에 유령이 있다.')
    print('몇 번 문을 열 것인가?')
    door = input('1, 2, 3, 4 아니면 5?')
    door_num = int(door)
    
    if door_num == ghost_door:
        print('        ')
        print('유령이다!')
        feeling_brave = False
    else:
        print('           ')
        print('유령이 없다!')
        print('옆방으로 들어가라.')
        score = score + 1
        
print('도망쳐!')
print('Game over! 점수는', score)