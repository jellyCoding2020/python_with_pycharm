print('안녕 내 이름은 이은성이라고 해')

name = input('너는 이름이 뭐니?')

greeting = '음.. 그렇군!? 어쨋든 반가워! ' + name + '!'

print(greeting)

do_you_like_computer = input('너는 컴퓨터를 좋아하니? (어/아니) ')

if do_you_like_computer == '어':
  print('그래? 그럼 같이 컴퓨터 할래?')
  
if do_you_like_computer == '아니':
  print('알겠어.. 잘가---!')

else:
  print('모르겠으면 나랑 컴퓨터 같이 해 보는건 어때?')

