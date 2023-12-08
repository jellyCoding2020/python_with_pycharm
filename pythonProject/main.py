
#quiz = ['2X2는 무엇일까요?', '2X2는 무엇일까요?']
#solution = [4, 8]

quizAndSol = [  ['2X2는 무엇일까요?', 4], ['4X4는 무엇일까요?', 16] ]
for text in quizAndSol:
    print(text[0])
    a=int(input('여기에 정답을 입력해주세요'))
    if a== text[1]:
      print('잘했어요!')
    else:
      print(text[0][0:3]+'는 ' +text[1]+'입니다')


quizAndSolDict = {  '곱하기 문제': ['2X2는 무엇일까요?', 4],
                    '제곱근 문제': ['제곱해서 4가 되는 숫자는 무엇일까요?', [2, -2] ] }


quiz = quizAndSolDict['곱하기 문제'][0]
print(quiz)
a = int(input('여기에 정답을 입력해주세요'))
if a ==  quizAndSolDict['곱하기 문제'][1]:
    print('정답입니다.')


quiz = quizAndSolDict['제곱근 문제'][0]
print(quiz)
a = int(input('여기에 정답을 입력해주세요'))
if a in quizAndSolDict['제곱근 문제'][1]:
    print('정답입니다.')





