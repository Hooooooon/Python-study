def _sqrt(a,b,c) :
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1,r2

x = 1
y = 2
z = -8

# 함수 호출
r1,r2 = _sqrt(x,y,z)

print('해는 {}, {}'.format(r1,r2))