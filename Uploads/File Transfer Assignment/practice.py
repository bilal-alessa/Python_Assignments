import os
import datetime
import shutil
import time




source = '/Users/Bilal/Desktop/Folder A/'

destination = '/Users/Bilal/Desktop/Folder B/'
files = os.listdir(source)


for i in files:
    x = int(os.path.getmtime(source+i))
    currentTime= int(time.time())
    getHours = int((currentTime - x) / 3600)
    if getHours > 24:
        print(i + ' is greater')
    else:
        print(i + ' is not ready NO')
    print(getHours)
    #print(currentTime)
    #print(x)
    
    
##
##def checkTime():
##    for i in files:
##        timeEach = files[i]
##        if timeEach.os.path
        
