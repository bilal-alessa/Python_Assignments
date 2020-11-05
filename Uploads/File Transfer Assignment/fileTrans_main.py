import webbrowser
import os
from tkinter import *
import tkinter as tk
import fileTrans_func
import fileTrans_gui




class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(450, 150)
        self.master.maxsize(450, 150)

        self.master.title("Web Page Generator")

        
        fileTrans_gui.load_gui(self)




if __name__ == "__main__":
        print('Initiating File Transfer GUI...')
        root = tk.Tk()
        App = ParentWindow(root)
        root.mainloop()
        

