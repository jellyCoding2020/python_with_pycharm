import random

number = random.randint(1, 2)
count = 0

while True:
    answer = int(input('내가 고른 숫자를 맞쳐봐!'))
    count += 1

    if answer == number:
        print('제법이군! 정답이야!')
        print(str(count)+'번 만에 맞혔어!')
        break

    elif answer < number:
        print('업 up!')

    else:
        print('다운 down!')
