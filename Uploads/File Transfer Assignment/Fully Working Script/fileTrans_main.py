import shutil
import os
import time
import datetime

# set where th source of the files are
source = '/Users/Bilal/Desktop/Folder A/'

# set the destination path to folderB
destination = '/Users/Bilal/Desktop/Folder B/'


#Global Variables
files = os.listdir(source)
filesBUP = os.listdir(destination)
nextBackup = datetime.date.today()

def copyFiles():
    for i in files:
        try:
            shutil.move(source+i, destination)
        except:
            pass


def checkTime():
    for i in files:
        mainFiles = os.path.getmtime(source+ i)
        backupFiles = os.path.getmtime(destination+ i)
        if mainFiles == backupFiles:
            print('File already exists in Backup Directory NO CHANGE!...')
            pass
        else:
            os.remove(destination+ i)
            shutil.move(source+i, destination)
            print(i + ' Not same modified version, will backup...')
        print('Next Backup on {}'.format(nextBackup))
        start()


def start():
    backupLock = True
    while backupLock:
        #Call to global variable
        global nextBackup
        if nextBackup == datetime.date.today():
            backupLock = False
            break
        else:
            pass
    print('Starting Backup')
    nextBackup = nextBackup + datetime.timedelta(days=1)
    # Lock it back up to prevent continual backup
    backupLock= True
    print('completed')
    copyFiles()
    checkTime()


if __name__ == "__main__":
    start()

