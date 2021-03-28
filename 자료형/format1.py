# 인사 로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# old way
print(number , '번 손님', greeting, '.', place , '에 오신 것을', welcome, '!')

# new way
base = '{}번 손님 {}. {}에 오신 것을 {}!.' 
new_way = base.format(number, greeting, place, welcome)

print(base)
print(new_way)