from tkinter import Tk, Button
from time import strftime, localtime

def clicked():
    time = strftime('Day : %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    print(time)

root = Tk()

button = Button(root, text = 'click it', command=clicked)
button.pack()

root.mainloop()