
from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.master = master
        self.master.minsize(700,260)
        self.master.maxsize(700,260)
        self.master.title('Check Files')
        self.master.configure(bg='#F0F0F0')

        self.varFname = StringVar()
        self.varLname = StringVar()

        self.btnBrowse1 = Button(self.master, text = "Browse...",width=13,height=1, font=14,)
        self.btnBrowse1.grid(row=1, column=0, padx=(30,0), pady=(80,0), sticky=NW)
        self.btnBrowse2 = Button(self.master, text = "Browse...",width=13,height=1, font=14)
        self.btnBrowse2.grid(row=2, column=0, padx=(30,0), pady=(15,15), sticky=NW)
        self.btnCheck = Button(self.master, text = "Check for files...",width=13,height=2, font=14)
        self.btnCheck.grid(row=3, column=0, padx=(30,0), pady=(0,0), sticky=SW)

        self.txtEntry = Entry(self.master,text =self.varFname, font = ('Arial', 16), width=38)
        self.txtEntry.grid(row=1, column=1, columnspan=4, padx=(50,0), pady=(80,0), sticky=W)
        
        self.txtEntry2 = Entry(self.master,text =self.varLname, font = ('Arial', 16), width=38)
        self.txtEntry2.grid(row=2, column=1, columnspan=4, padx=(50,0), pady=(10,10), sticky=W)

        self.btnClose = Button(self.master, text = "Close Program",width=14,height=2, font=14, command=self.close)
        self.btnClose.grid(row=3, column=4, padx=(20,0), pady=(0,0), sticky=SE)

    def close(self):
        self.master.destroy()



    
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() 
