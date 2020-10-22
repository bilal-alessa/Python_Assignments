# Python    3.7.8
#
#
#
# Author    Bilal M Al-Essa
#
#


import os



fileNames = {""}




def gatherNames():
    currentDir = os.listdir(path="C:\\Users\\Bilal\\Desktop\\School Work\\Python\\Python\\Uploads\\Assignment PG 167")
    for i in currentDir:
        if i.endswith(".txt"):
            completePath = os.path.join("C:\\Users\\Bilal\\Desktop\\School Work\\Python\\Python\\Uploads\\Assignment PG 167", i)
            timeDate = os.path.getmtime(i)

            print(i)
            print(i)

    return i

    





gatherNames()
