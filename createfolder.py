# CreateFolder.py

''' 
This is a selection of scripts to create folders in a Windows
environment. 
'''
import os

# Create a folder if the folder does not exist
def make_new_path():
    newpath = r'C:\VC_Healy\arbitrary' 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

#Create a folder, if it exists check, then gives a message
def make_relative_path():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    newpath = r'directory' 

    if os.path.exists(newpath):
        print(f'Folder "{fileDir}\{newpath}" exists')
    else:
        os.makedirs(newpath)

# Input a directory name, check to see if it exists, *** Use Terminal not Output
def inputname_relative_path():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    dirname = input('What is the directory name? ')
    newpath = rf'{dirname}' 
    if os.path.exists(newpath):
        print(f'Folder "{fileDir}\{newpath}" exists \n')
        # print('Folder exists')
    else:
        os.makedirs(newpath)
        print(f'\nFolder Created\n\n"{fileDir}\{newpath}"\n')



# make_new_path()
# make_relative_path()
inputname_relative_path()