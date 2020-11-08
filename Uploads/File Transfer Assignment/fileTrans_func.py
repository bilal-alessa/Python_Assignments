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


def copyFiles():
    fileList = getList()
    backupList = getDestination()
    print(fileList)
    for i in fileList:
        if i not in backupList:
            shutil.copy(source+i, destination)
        else:
            print("Element already in the list")






##def copyFiles():
##    print('starting copyfiles')
##    fileList = getList()
##    backupList = getDestination()
##    print(fileList)
##    for i in fileList:
##        if i != backupList:
##            shutil.copy(source+i, destination)



def checkTime():
    global source
    fileList = getList()
    for i in fileList:
        x = int(os.path.getmtime(source+i))
        currentTime= int(time.time())
        getHours = int((currentTime - x) / 3600)
        if getHours < 24:
            try:
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


### finds last modified time and compares each file in folders. Copies and deletes if different.
##def checkTime():
##    print('starting checktime')
##    fileList = getList()
##    for i in fileList:
##        mainFiles = os.path.getmtime(source+ i)
##        backupFiles = os.path.getmtime(destination+ i)
##        if mainFiles == backupFiles:
##            print('File already exists in Backup Directory NO CHANGE!...')
##            pass
##        else:
##            #os.remove(destination+ i)
##            shutil.copy(source+i, destination)
##            print(i + ' Not same modified version, will backup...')
##        print('Next Backup on {}'.format(nextBackup))


    


#avoids the loop and allows the user to press button to initiate. Cant run if 24 loop is active.
def manualStart():
    copyFiles()
    print('started')
    #checkTime()
    


# this is to start the loop during the 24 hour session and repeats
def start():
    print('starting loop')
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
    print('Starting Backup')
    nextBackup = nextBackup + datetime.timedelta(days=1)
    # Lock it back up to prevent continual backup
    backupLock= True
    print('completed')
    copyFiles()
    print('start checktime')
    checkTime()
    start()


if __name__ == "__main__":
    pass

