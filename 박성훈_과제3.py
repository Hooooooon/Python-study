import turtle

print("길이를 입력해주세요 >> ")
n = int(input())
# 한변의 길이가 n인 정사각형
# 지름의 길이가 n인 원
t = turtle.Pen()

t.circle(n/2) # circle -> n/2 반지름
t.forward(n/2)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)

# 터틀 숨김
#t.hideturtle()