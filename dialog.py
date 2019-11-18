
import tkinter
from tkinter import *
from tkinter import filedialog
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(400,150))
        self.master.title('Dialog Box')
        

        self.Input= Text(self.master,width=25, height=5, font=11)
        self.Input.grid(row=0,column=0,padx=(10,10), pady=(10,0),sticky=W)
         
        self.btn_Click = Button(self.master,text='Click',width=10,height=2, command=self.open_dir) 
        self.btn_Click.grid(row=0,column=1,padx=(10,0),pady=(10,0),sticky=NE)
        

        

    def open_dir(self):
        fileName = filedialog.askdirectory()
        self.Input.delete(0.0,END)
        self.Input.insert(0.0,fileName)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


