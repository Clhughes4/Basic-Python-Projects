import tkinter
from tkinter import *
from tkinter import filedialog
import os
import shutil
import sqlite3
import time


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        self.master = master
        self.master.minsize(700,260)
        self.master.maxsize(700,260)
        self.master.title('Check Files')
        self.master.configure(bg='#F0F0F0')

        self.Var1 = StringVar()
        self.Var2 = StringVar()

        self.btnBrowse1 = Button(self.master, text = "Browse...",width=13,height=1, font=14, command=self.source_dir)
        self.btnBrowse1.grid(row=1, column=0, padx=(30,0), pady=(80,0), sticky=NW)
        self.btnBrowse2 = Button(self.master, text = "Browse...",width=13,height=1, font=14, command=self.dest_dir)
        self.btnBrowse2.grid(row=2, column=0, padx=(30,0), pady=(15,15), sticky=NW)
        self.btnCheck = Button(self.master, text = "Move File",width=13,height=2, font=14,command =self.find_file)
        self.btnCheck.grid(row=3, column=0, padx=(30,0), pady=(0,0), sticky=SW)

        self.txtEntry = Entry(self.master,text =self.Var1, font = ('Arial', 14), width=38)
        self.txtEntry.grid(row=1, column=1, columnspan=4, padx=(50,0), pady=(80,0), sticky=W)
        
        self.txtEntry2 = Entry(self.master,text =self.Var2, font = ('Arial', 14), width=38)
        self.txtEntry2.grid(row=2, column=1, columnspan=4, padx=(50,0), pady=(10,10), sticky=W)

        self.btnClose = Button(self.master, text = "Close Program",width=14,height=2, font=14, command=self.close)
        self.btnClose.grid(row=3, column=4, padx=(20,0), pady=(0,0), sticky=SE)

    def close(self):
        self.master.destroy()

    def source_dir(self):
        fileName = filedialog.askdirectory()
        self.txtEntry.delete(0,END)
        self.txtEntry.insert(0,fileName)

    def dest_dir(self):
        fileName = filedialog.askdirectory()
        self.txtEntry2.delete(0,END)
        self.txtEntry2.insert(0,fileName)

    def find_file(self):
        dirName = self.txtEntry.get()
        print(dirName)
        self.create_db()

        dirList = os.listdir(dirName)
        # print the list
        conn = sqlite3.connect('DATA.db')
        with conn:
            cur = conn.cursor()
            for file in dirList:
                if file.endswith('.txt'):
                    print(file)
                    modTime = os.path.getmtime(os.path.join(dirName,file))
                    # print the last modification time
                    print(modTime)

                    realTime = time.ctime(modTime)
                    print(realTime,'\n')
                    cur.execute('INSERT INTO tbl_DataFile(File_Name, Modified_Date) VALUES (?, ?)', \
                                (file, realTime))
            conn.commit()
        conn.close()
        self.new_dir()



    def new_dir(self):
        src = source_dir
        dst = dest_dir
        print(dst)
        for files in src:
            if files.endswith('.txt'):
                shutil.move(files,dst)
        
        
        

    def create_db(self):
        conn = sqlite3.connect('DATA.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_DataFile( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                File_Name TEXT, \
                Modified_Date TEXT \
                );")
            conn.commit()
        conn.close()
        



    

    
    

    


        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
