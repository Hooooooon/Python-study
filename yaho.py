class p1:
    def bubblesort(self, lst):
        for i in range(len(lst)-1, 0, -1):
            for j in range(i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]

    def print(self):
        lst = [3, 1, 7, 9, 2, 5]
        bubblesort(lst)
        print(lst)

class p2:
    def test(self, num):
        if num > 0:
            return 'Positive'
        elif num < 0:
            return 'Negative'
        else :
            return 'Zero'

    def print(self):
        print(self.test(0))
        print(self.test(-3))
        print(self.test(3))

class chpater5:
    def mult3(self, lst):
        for num in lst :
            if num % 3 == 0 :
                print(num)
    def vowels(self, str):
        for idx, s in enumerate(str):
            if s in 'aeiouAEIOU':
                print(idx)
    def indexes(self, str, find):
        lst = list()
        for idx, ch in enumerate(str):
            if ch is find :
                lst.append(idx)
        return lst

class chapter6:
    def easyCrypto(self, vStr):
        crpStr = str()
        for idx, ch in enumerate(vStr):
            if idx % 2 == 0: #짝수
                crpStr += chr(ord(vStr[idx])+1)
            else :
                crpStr += chr(ord(vStr[idx])-1)
        print(crpStr)
import math
import random 

class chpater8:
    class Point:
        def setx(self, x):
            self.x = x
        def sety(self, y):
            self.y = y
        def distance(self, other):
            return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2)) 

from tkinter import Entry, Frame, Label, Tk, LEFT
import random
class gameGUI(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.pack()
        # Frame 생성 후
        lable = Label(root, text = 'Enter your guess')
        lable.pack()

        self.ent = Entry(root)
        self.ent.pack()

        btn = Button(root, text = 'Enter', command = self.clicked)
        btn.pack()

    def clicked(self, event):
        user = self.ent.get()
        com = random.randrange(0, 10)
        if com == user :

        


root = Tk()
app = gameGUI(root)
app.pack()
root.mainloop()