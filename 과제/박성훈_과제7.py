import random

user = input('가위, 바위, 보 중 하나를 입력하세요!>>')
# 가위, 바위, 보 중 랜덤으로 하나 선택
computer = random.choice(['가위', '바위', '보'])

result = -1
# 사용자가 입력한 것과 컴퓨터의 선택을 비교하여 승패를 정한다
if(user == '가위') :
   if(computer == '가위') :
       result = '비겼습니다'
   elif(computer == '바위') :
       result = '졌습니다!'
   else :
       result = '이겼습니다!'
elif(user == '바위') :
   if(computer == '가위') :
       result = '이겼습니다!'
   elif(computer == '바위') :
       result = '비겼습니다'
   else :
       result = '졌습니다!'
elif(user == '보') :
    if(computer == '가위') :
       result = '졌습니다!'
    elif(computer == '바위') :
       result = '이겼습니다!'
    else :
        result = '비겼습니다'
else :
   print('잘못 입력하셨습니다!')

# 입력을 제대로 했으면 결과를 출력한다.
if(result != -1): 
    print('사용자 : {}'.format(user))
    print('컴퓨터 : {}'.format(computer))
    print(result)
