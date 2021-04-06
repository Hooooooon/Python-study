import math # math.sqrt 함수를 사용하기 위해 import

# 함수 정의 (x1, y1), (x2, y2) 
def points(x1, y1, x2 ,y2) :                    
    if (x2-x1 == 0) : 
        slope = "infinity"                          # 기울기가 수직이면 infinity
    else :                                          # 기울기가 수직이 아니면
        slope = (y2 - y1) / (x2 - x1)               # 기울기 값 계산, y증가량/x증가량
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)     # 두 점사이의 거리를 구한다.
    print("The slope is " + str(slope) + " and the distance is " + str(distance))   # 기울기와 거리를 문자열로 변형 후 출력

# 함수 실행
x1, y1, x2, y2 = map(int, input().split())
points(x1, y1, x2, y2)

