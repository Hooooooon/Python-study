class Queue:
    ''' 고전 Queue 클래스 '''
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return (len(self.q) == 0)
    
    def enqueue(self, item):
        return self.q.append(item)
    
    def dequeue(self, item):
        # 맨 앞에 item 제거하고 반환
        return self.q.pop(0)

class Point:
    x = 0
    y = 0
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        ''' 표준 문자열 반환 '''
        return 'Point({}, {})'.format(self.x, self.y)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)
        
    def __mul__(self, other): # 벡터 내적
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        else :
            return self.x * other + self.y * other

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

v1 = Vector(1,3)
v2 = Vector(-2,4)
print(v1 + v2)
print(v1 * v2)