import webbrowser
import os
from tkinter import *
import tkinter as tk
import webgen_func
import webgen_gui






class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 150)
        self.master.maxsize(500,150)

        self.master.title("Web Page Generator")

        
        webgen_gui.load_gui(self)






if __name__ == "__main__":
    print('This works')
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

