from tkinter import PhotoImage, Tk, Label
# window
root = Tk()
root.title("PYTHON GUI")
photo = PhotoImage(file = '')
# label 객체
hello = Label(master = root, image = photo, width = 150, height= 150)
# 위치 명시
hello.pack()

# 윈도우 생성
root.mainloop()