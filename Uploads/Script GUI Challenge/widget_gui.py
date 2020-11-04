from tkinter import *
import tkinter as tk

import widget_main
import widget_func


currentFileOpen = ''



def load_gui(self):
        self.b1 = Button(self.master,width =12, text='Browse...', command = lambda : getDir(self))
        self.b2 = Button(self.master, width =12, text='Browse FAKE...')
        self.b3 = Button(self.master, height=2, text='Check for files...', )
        self.b4 = Button(self.master, height=2, text='Close Program  ')

        self.lbl1 = Entry(self.master, width = 60)
        self.lbl2 = Entry(self.master, width = 60)

        


        self.b1.grid(row=1, column= 0, pady = 10)
        self.b2.grid(row=2, column=0)
        self.b3.grid(row=3, column=0, pady=10, padx = 10)
        self.b4.grid(row=3, column=5)

        self.lbl1.grid(row=1, column = 1, columnspan= 5)
        self.lbl2.grid(row=2, column = 1, columnspan= 5)


def getDir(self):
    self.dirName = tk.filedialog.askdirectory(initialdir = "/", title = "Select A Dir")
    currentFileOpen = self.dirName
    textbox = Label(self.master, text = "" , pady = 8)
    textbox.grid(row=0, column = 1)
    textbox.configure(text = currentFileOpen)




if __name__ == "__main__":
    pass
##
##filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
##filetypes = (("jpeg", "*.jpg"), ("All Files", "*.*"))

