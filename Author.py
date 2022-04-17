'''
This program will help you add author comments in all files at once
1. Select directory containing all files that need to be manipulated
2. Select task
3. Done

Script made by Saim 17/04/2022
'''

import glob
import os
from tkinter import Tk, filedialog

################################################################
# Enter file type
filetype = "java"
################################################################
# Change these accordingly
name = "Abdullah Saim"
email = "asaim.bscs21seecs@seecs.edu.pk"
section = "BSCS-11C"
year = "2022"
################################################################
# Manually add anything you want to add
author = "/*\nAuthor: "+name+"\n"+email+"\n"+section+"\nThis is completely my own work. All rights reserved "+year+"\n*/\n\n"
################################################################
effected = []

# Main Script
if input("Do you want to select the directory for your java files? (leave blank to use current directory): ") != "":
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection
    open_file = filedialog.askdirectory() # Returns opened path as 
    folder_path = open_file
else:
    folder_path = os.getcwd()

if input("Do you want to (a)dd or (r)emove author comments ") != "r":
    for filename in glob.glob(os.path.join(folder_path, '*.'+filetype)):
        with open(filename, 'r') as f:
            str = f.read()
        f.close()
        with open(filename, 'w') as f:
            if author not in str:
                f.writelines(author)      
            f.writelines(str)
        effected.append(filename)
    effected.append("were added to")
else:
    for filename in glob.glob(os.path.join(folder_path, '*.'+filetype)):
        with open(filename, 'r') as f:
            str = f.read()
        f.close()
        with open(filename, 'w') as f:    
            f.writelines(str.replace(author,""))
            
        effected.append(filename)
    effected.append("were removed from")

            
print("Commentes "+effected[-1]+" these files:")
for f in effected[:-1]:
    print(f)

input("\nPress enter to exit")

