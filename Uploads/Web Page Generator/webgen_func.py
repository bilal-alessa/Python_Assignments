import webbrowser
import os
from tkinter import *
import tkinter as tk
import webgen_main
import webgen_gui


# Using the HTML provided as a base template and inserting entry between.

originalText1 ="""
<html> 
    <body> 
        <h1>"""
originalText2 ="""
        </h1>
    </body> 
</html> """


def userInput(self):
    s = self.text1.get()
    print(s)
    return str(s)

# this one I didn't want to touch since it works didn't want to break it. I'm sure I can size it down
# if I need to such as userText variable and others.
def buildFile(self):
    file_exists = os.path.exists("index.html")
    print(file_exists)
    if file_exists:
        webbrowser.open("index.html", new = 0, autoraise=True)
        print("File already found!")
    else:
        newHTML = open("index.html", "x")
        userText = originalText1 + userInput(self) +originalText2
        print("File not found. Made and added HTML to index")
        newHTML.write(userText)
    webbrowser.open("index.html", new = 0, autoraise=True)




# Dont activate wrong script
if __name__ == "__main__":
    pass
