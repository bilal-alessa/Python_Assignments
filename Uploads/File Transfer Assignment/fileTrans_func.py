import shutil
import os
import time
import datetime
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import fileTrans_func
import fileTrans_main

# set where th source of the files are
source = "/"

# set the destination path to folderB
destination = "/"

#Global Variables
files = os.listdir(source)
filesBUP = os.listdir(destination)
nextBackup = datetime.date.today()

def getSource():
    global source
    rootDir = source
    files = os.listdir(source)
    return source

def getList():
    fileList = os.listdir(source)
    return fileList

def getDestination():
    global destination
    rootDir = destination
    filesBUP = os.listdir(destination)
    return filesBUP

def setSource(self):
    self.dirName = tk.filedialog.askdirectory(initialdir = "/", title = "Select A Dir")
    self.lbl1.configure(text = 'Root Directory: '+ self.dirName)
    global source
    source = self.dirName + '/'
    print(source)

def setDestination(self):
    self.dirBackup = tk.filedialog.askdirectory(initialdir = "/", title = "Select A Dir")
    self.lbl2.configure(text = 'Backup Directory: '+ self.dirBackup)
    global destination
    destination = self.dirBackup + '/'
    print(destination)


def checkTime():
    for i in source:
        fileList=files
        print('task 1')
        x = int(os.path.getmtime(fileList+i))
        print('task 2')
        currentTime= int(time.time())
        print('task 3')
        getHours = int((currentTime - x) / 3600)
        print('task 4')
        if getHours < 24:
            try:
                print('task 5')
                os.remove(destination+ i)
                shutil.copy(source+i, destination)
                print('File Backuping Up...')
            except:
                print('File Exists Overwriting Backup...')
                shutil.copy(source+i, destination)
                print('Overwrite Complete')
        else:
            pass
        print('DONE')


#avoids the loop and allows the user to press button to initiate. Cant run if 24 loop is active.
def manualStart():
    #copyFiles()
    checkTime()
    


# this is to start the loop during the 24 hour session and repeats
def start():
    global nextBackup
    backupLock = True
    while backupLock:
        #print('waiting on loop...')
        #Call to global variable
        if nextBackup == datetime.date.today():
            backupLock = False
            break
        else:
            print(nextBackup, datetime.date.today())
            #print('still waiting on loop...')
            continue
    nextBackup = nextBackup + datetime.timedelta(days=1)
    # Lock it back up to prevent continual backup
    backupLock= True
    checkTime()
    start()


if __name__ == "__main__":
    pass

