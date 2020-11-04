from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import widget_func
import widget_gui



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        self.master = master
        self.master.minsize(490,180)
        self.master.maxsize(490,180)


        self.master.title("Script GUI")

        
        widget_gui.load_gui(self)







if __name__ == "__main__":
    print('This works')
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
