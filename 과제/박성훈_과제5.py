# 별 피라미드
for i in range(5) :
    for j in range(4-i):
        print(' ', end = '')    # 공백
    for j in range(i*2+1):
        print('*', end = '')    # 별
    print()                     # 개행

# 터틀
import turtle
t= turtle.Turtle()

len = 100   # 오각형 변의 길이
# 오각형을 그린다 5개 그린다
for i in range(5):
    # 오각형 1개를 그린다
    for j in range(5):
        t.forward(len)
        t.left(72)
    # 다음에 그릴 오각형 각도를 달리한다
    t.left(72)
t.hideturtle()  # 터틀 숨김

