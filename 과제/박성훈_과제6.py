# 숫자 n을 x 진법으로 표현한 문자열을 반환하는 함수
def d2x(num, x) :
    # 0 이상의 정수 n, 2와 9사이의 정수 x 만 받는다
    if(num < 0 or not(x>=2 and x<=9)) :
        print("0 이상의 정수 n 또는 2와 9사이의 정수 x 만 입력!")
        return
    
    result = str()
    # num을 계속 나누고 갱신하니 0이하면 더이상 나눌게 없다
    while(num > 0):
        mod = num % x
        num = num // x
        result += str(mod)
    # 문자열을 뒤집고 그 문자열을 반환한다.
    return result[::-1]


print("d2x(10, 2) = ", d2x(10,2))
print("d2x(10, 3) = ", d2x(10,3))
print("d2x(10, 8) = ", d2x(10,8))
print("d2x(34, 2) = ", d2x(34,2))
