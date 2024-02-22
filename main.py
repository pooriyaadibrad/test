from tkinter import *


win=Tk()

win.geometry("800x600")
def test(e):
    print("hi")
btn=Button(win,text="Click ")
btn.bind("<Button-1>",test)
btn.pack(side="top",fill=BOTH)

win.mainloop()
