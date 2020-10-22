
import os
import sqlite3

# File list I need to use to grab and iterate through the names.

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')



# Create the Datebase with colums followed by closing the connection
def start():
    conn = sqlite3.connect('fileNamesdb.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS file_directory( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_names TEXT \
            )")
        DB = 'CREATED'
        conn.commit()
    conn.close()


        
# Grabs the file names from fileList global variable and returns files matching
# the ending.

def readExt():
    fileList2 = []
    for i in fileList:
        if i.endswith(".txt"):
            fileList2.append(i)
    return fileList2


def addListdb():

    conn = sqlite3.connect('fileNamesdb.db')
    with conn:
        for each in readExt():
            cur = conn.cursor()
            cur.execute('INSERT INTO file_directory(file_names) VALUES (?)', [each])
        conn.commit()
    conn.close()
    x = readExt()
    print("The files added to the DB are: \n")
    for i in x:
        print('{}'.format(i))

start()
readExt()
addListdb()

