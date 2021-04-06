# 주민번호를 입력받고 그 값을 생년월일로 변환.

numBirth = 991209
print("주민번호 = ",numBirth)

year = 1900 + (numBirth // 10000)   #년
month = (numBirth // 100) % 100     #월
day = (numBirth % 1000) % 100       #일
print("생년월일 = ",year, "년", month,"월", day, "일")
