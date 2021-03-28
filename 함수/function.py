def print_sqrt() :
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {} 입니다.'.format(r1, r2))

a = 1
b = 2
c = -8

# 함수 호출
print_sqrt()

a = 2
b = -6
c = -8

# 한 번 더 구하려면

print_sqrt()