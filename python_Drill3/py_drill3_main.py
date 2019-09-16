#
# Python Ver:   3.5.1
#
# Author:       Fred Picard
#
# Purpose:      Drill on Tkinder module
#
# Tested OS:  This code was written and tested to work with Windows 10.



import tkinter
from tkinter import *





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, *args, **kwargs) 

        
        self.master = master
        self.master.minsize(800,250) #(Height, Width)
        self.master.maxsize(800,250)
        self.master.title("Check Files")
        self.master.configure(bg="lightgrey")
       # self.master.protocol("WM_DELETE_WINDOW", lambda: drill50_phonebook_func.ask_quit(self))
        arg = self.master

        self.varbtn_1 = StringVar()
        self.varbtn_2 = StringVar() 

        self.btn_1 = Entry(self.master,text=self.varbtn_1, font=("Helvetica", 16), fg="black", bg="white", width="48")
        self.btn_1.grid(row=5, column=4, padx=(10,10), pady=(70,0))

        self.btn_2 = Entry(self.master,text=self.varbtn_2, font=("Helvetica", 16), fg="black", bg="white", width="48" )
        self.btn_2.grid(row=6, column=4, padx=(10,10), pady=(10,0))

        
        self.btn_1 = Button (self.master, text="Browse...", width=20, height=1,command=self.browse1)
        self.btn_1.grid(row=5, column=1, padx=(20,10), pady=(70,0), sticky=NE)
        
        self.btn_2 = Button (self.master, text="Browse...", width=20, height=1, command=self.browse2)
        self.btn_2.grid(row=6, column=1, padx=(20,10), pady=(10,0), sticky=SE)


        self.btn_3 = Button (self.master, text="Check for files...", width=20, height=3, command=self.callback)
        self.btn_3.grid(row=7, column=1, padx=(20,10), pady=(20,10), sticky=W)

        self.btn_4 = Button (self.master, text="Close Program", width=20, height=3, command=root.destroy)
        self.btn_4.grid(row=7, column=4, padx=(20,10), pady=(20,10), sticky=E)



    def browse1(self, text):
            widget = e.focus_get(btn-1)
            if widget in e.entries:
                widget.insert(0, text)
          
   
    def browse2(self, text):
            widget = e.focus_get()
            if widget in e.entries:
                widget.insert(0, text)

    def callback():
        tkMessageBox.showinfo( "Hello Python", "Hello World")

           

 
                     
             













        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
