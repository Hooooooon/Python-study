[33mcommit a2774122e91b1798f8b0f1c095113545f3e6f555[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: Hooooooon <shonn2323@gmail.com>
Date:   Tue Jun 1 21:15:03 2021 +0900

    OOP 개념 잡기1

[1mdiff --git a/.vscode/settings.json b/.vscode/settings.json[m
[1mnew file mode 100644[m
[1mindex 0000000..90604cb[m
[1m--- /dev/null[m
[1m+++ b/.vscode/settings.json[m
[36m@@ -0,0 +1,3 @@[m
[32m+[m[32m{[m
[32m+[m[32m    "python.pythonPath": "C:\\Users\\shonn\\AppData\\Local\\Programs\\Python\\Python39\\python.exe"[m
[32m+[m[32m}[m
\ No newline at end of file[m
[1mdiff --git a/OOP/oop1.py b/OOP/oop1.py[m
[1mnew file mode 100644[m
[1mindex 0000000..6a1a55f[m
[1m--- /dev/null[m
[1m+++ b/OOP/oop1.py[m
[36m@@ -0,0 +1,49 @@[m
[32m+[m[32mclass Queue:[m
[32m+[m[32m    ''' 고전 Queue 클래스 '''[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        self.q = [][m
[32m+[m
[32m+[m[32m    def isEmpty(self):[m
[32m+[m[32m        return (len(self.q) == 0)[m
[32m+[m[41m    [m
[32m+[m[32m    def enqueue(self, item):[m
[32m+[m[32m        return self.q.append(item)[m
[32m+[m[41m    [m
[32m+[m[32m    def dequeue(self, item):[m
[32m+[m[32m        # 맨 앞에 item 제거하고 반환[m
[32m+[m[32m        return self.q.pop(0)[m
[32m+[m
[32m+[m[32mclass Point:[m
[32m+[m[32m    x = 0[m
[32m+[m[32m    y = 0[m
[32m+[m[32m    def __init__(self, x = 0, y = 0):[m
[32m+[m[32m        self.x = x[m
[32m+[m[32m        self.y = y[m
[32m+[m
[32m+[m[32m    def __repr__(self):[m
[32m+[m[32m        ''' 표준 문자열 반환 '''[m
[32m+[m[32m        return 'Point({}, {})'.format(self.x, self.y)[m
[32m+[m
[32m+[m[32mclass Vector:[m
[32m+[m[32m    def __init__(self, x, y):[m
[32m+[m[32m        self.x = x[m
[32m+[m[32m        self.y = y[m
[32m+[m[32m    def __add__(self, other):[m
[32m+[m[32m        if type(other) == Vector:[m
[32m+[m[32m            return Vector(self.x + other.x, self.y + other.y)[m
[32m+[m[32m        else:[m
[32m+[m[32m            return Vector(self.x + other, self.y + other)[m
[32m+[m[41m        [m
[32m+[m[32m    def __mul__(self, other): # 벡터 내적[m
[32m+[m[32m        if type(other) == Vector:[m
[32m+[m[32m            return self.x * other.x + self.y * other.y[m
[32m+[m[32m        else :[m
[32m+[m[32m            return self.x * other + self.y * other[m
[32m+[m
[32m+[m[32m    def __repr__(self):[m
[32m+[m[32m        return 'Vector({}, {})'.format(self.x, self.y)[m
[32m+[m
[32m+[m[32mv1 = Vector(1,3)[m
[32m+[m[32mv2 = Vector(-2,4)[m
[32m+[m[32mprint(v1 + v2)[m
[32m+[m[32mprint(v1 * v2)[m
\ No newline at end of file[m
