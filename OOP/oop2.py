class Point:
    x = 2
    def __init__(self):
        pass
    def __add__(self, other):
        return self.x + other


pt = Point()
print(type(pt) + 2)