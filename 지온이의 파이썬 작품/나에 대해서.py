#지온이의 첫번째 파이썬 대화게임

print("안녕? 반가워 내 이름은 윤지윤이라고 해!")

yourName = input("너 이름이 뭐니?")

introduce = '아!' + yourName + ' 반가워! 내가 내는 퀴즈를 마춰봐~~'

print(introduce)


score = 0
## -- 1번 퀴즈 내기 ------------------------------------------------------------
answer = input ("너를 영어로 무엇인지 알아?")

print('당신의 답변: ', answer)

#if answer == 'you' :
if 'you' in answer : # answer 변수에 글자값 'you'가 포함되었다면, 굿을 출력하기 
    print(' 굿!!  Good  ')
    score = score + 7
    print('당신의 점수: ', score)

else : # 'you'라는 글자값이 answer에 포함되지 않았다면, 아래의 메시지를 보여주기  
    print(' 정말 못했어! 그 정도도 모르니?')
    
    


answer = input ("달을 영어로 무엇인지 알아?")

print('당신의 답변: ', answer)

#if answer == 'moon' :
if 'moon' in answer : # answer 변수에 글자값 'moon'가 포함되었다면, 굿을 출력하기 
    print(' 굿!!  Good  ')
    score = score + 7
    print('당신의 점수: ', score)

else : # 'moon'라는 글자값이 answer에 포함되지 않았다면, 아래의 메시지를 보여주기  
    print(' 정말 못했어! 그 정도도 모르니?')




