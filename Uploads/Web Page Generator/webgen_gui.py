import webbrowser
import os
from tkinter import *
import tkinter as tk
import webgen_func
import webgen_main
# Don't think ill need os but might as well import in incase I need it for now


# Calling seperate line of code to make the gui easier and less cluttered. Remember to use (self.)
def load_gui(self):
    # Buttons assign variables
    # lambda seems to avoid executing the command on launch so use that as an onclick function.
    self.b1 = Button(self.master, text = "Add Changes", command = lambda: webgen_func.buildFile(self))

    # Textbox assign variables
    self.text1 = tk.Entry(self.master, width = 60, text='')

    # Buttons define values
    self.b1.pack(side = tk.TOP, pady = 20)
        
    # Textbox define values
    self.text1.pack(side = tk.TOP)




# using to avoid activating the wrong script
if __name__ == "__main__":
    pass
        
