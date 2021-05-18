from tkinter import Label, Tk
from tkinter.constants import RAISED
from calendar import monthrange

def cal(year, month):
    root = Tk()

    days = monthrange(year, month) # days -> tuple, 
    strWeek = ['Mon', 'Tue', 'Wed', "Thu", 'Fri', 'Sat', 'Sun']
    for i in range(7):
        label = Label(root, padx = 10, text = strWeek[i])
        label.grid(row = 0, column= i)
    for i in range(42):
        day = i-days[0]+1
        if day > 0 and day <= days[1]:
            label = Label(root, padx = 10, text = day)
            label.grid(row = int(i/7)+1, column = i%7)
    root.mainloop()

cal(2021, 5)