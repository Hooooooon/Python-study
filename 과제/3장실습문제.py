# 3.10
def noVowel(s):
    for c in s:
        ## 문자열 s에 모음이 없다면 True를 아니면 False
            if c in 'aeiouAEIOU' :
                    return True
            return False


"""
str = input()
for i in range(0, len(str)) :
    result = noVowel(str[i])
    print(result)
"""

# 3.11번

# for문을 사용해서 리스트내의 각 원소가 짝수인지 판별,
# 한 개라도 짝수가 아니면 False 바로 반환
# for문의 반복이 끝나고 True 반환

def allEven(numList)    :
    for num in numList :
            if num%2 != 0 :
                    return False
    return True
"""
arrNum = map(int, input().split() )


result =allEven(arrNum)
print(result)"""

# 3.37
# 기울기 -> y증가분/x증가분
    # 거리    -> sqrt(x-x)^2+(y-y)^2
    # 출력하는 함수
    # 기울기가 수직선이면 infinity로 출력
    # 기울기와 거리를 출력하기전에 문자열로 변한 한 뒤

import math
def points(x1, y1, x2 ,y2) :
    if (x2-x1 == 0) : slope = "infinity"
    else :
        slope = (y2 - y1) / (x2 - x1)
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The slope is " + str(slope) + " and the distance is " + str(distance))


















    
    
