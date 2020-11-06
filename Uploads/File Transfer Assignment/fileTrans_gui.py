import os
from tkinter import *
import tkinter as tk
import fileTrans_func
import fileTrans_main







def load_gui(self):

    #Buttons Declaration
    self.b1 = tk.Button(self.master, text = 'Set Root Directory', command = lambda: fileTrans_func.setSource(self))
    self.b2 = tk.Button(self.master, text = 'Set Backup Folder', command = lambda: fileTrans_func.setDestination(self))
    self.b3 = tk.Button(self.master, text = 'Manual Execute', command = fileTrans_func.manualStart)
    self.b4 = tk.Button(self.master, text = 'AUTO Execute Daily', command = lambda : fileTrans_func.start())
    
    #Buttons Assigning Variables
    self.b1.grid(row= 0, column = 0, pady = 5, padx = 5)
    self.b2.grid(row=2, column = 0, pady = 5, padx = 5)
    self.b3.grid(row=4, column = 0, pady = 5, padx = 5)
    self.b4.grid(row=6, column = 0, pady = 5, padx = 5)
    
    #Labels for showing user information
    self.lbl1 = tk.Label(self.master, text = 'None Path Set')
    self.lbl2 = tk.Label(self.master, text = 'None Path Set')
    self.lbl3 = tk.Label(self.master, text = '')
    self.lbl4 = tk.Label(self.master, text = '')


    #Labels on screen assignment
    self.lbl1.grid(row = 0, column = 1)
    self.lbl2.grid(row = 2, column = 1)
    self.lbl3.grid(row = 4, column = 1)
    self.lbl4.grid(row = 6, column = 1)
    
    

    






if __name__ == "__main__":
    pass
