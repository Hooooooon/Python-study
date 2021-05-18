from tkinter import Tk, Label, PhotoImage
from tkinter.constants import LEFT, RIGHT

root = Tk()

img1 = PhotoImage(file = 'GUI/도지.png')
imgLabel = Label(root, image = img1, width = 100, height = 100, padx = 100, pady = 100)
imgLabel.pack(fill = 'y', side = LEFT)

img2 = PhotoImage(file = 'GUI/도지.png')
img2Label = Label(root, image= img2, width = 100, height = 100, padx = 100, pady = 100)
img2Label.pack(fill='y', side = RIGHT)

root.mainloop()
