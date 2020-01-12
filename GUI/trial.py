from tkinter import *


def click_me():
   print(i.get())


root = Tk()

i = StringVar()
r1 = Radiobutton(root, text="male", value="radio 1", variable=i)
r2 = Radiobutton(root, text="female", value="radio 2",  variable=i)
r1.pack()
r2.pack()



button = Button(root, text="check", command=click_me)
button.pack()
root.geometry("300x300+120+120")
root.mainloop()