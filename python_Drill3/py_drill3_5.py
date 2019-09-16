import tkinter
from tkinter import *




class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        
        self.master = master
        self.master.minsize(800,300) #(Height, Width)
        self.master.maxsize(800,300)
        self.master.title("Check Files")
        self.master.configure(bg="#ffe6e6")
top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

top.mainloop()
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
