# createFolder.py

''' 
This is a selection of scripts to create folders in a Windows
environment. 
'''
import os

# Create a folder if the folder does not exist
def make_new_path():
    newfolder = r'C:\VC_Healy\arbitrary' 
    if not os.path.exists(newfolder):
        os.makedirs(newfolder)

#Create a folder, if it exists check, then gives a message
def make_relative_path():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    newfolder = r'directory' 

    if os.path.exists(newfolder):
        print(f'Folder "{fileDir}\{newfolder}" exists')
    else:
        os.makedirs(newfolder)

# Input a directory name, check to see if it exists, *** Use Terminal not Output
def inputname_relative_path():
    fileDir = os.path.dirname(os.path.abspath(__file__))
    dirname = input('What is the directory name? ')
    newfolder = rf'{dirname}' 
    if os.path.exists(newfolder):
        print(f'Folder "{fileDir}\{newfolder}" exists \n')
        # print('Folder exists')
    else:
        os.makedirs(newfolder)
        print(f'\nFolder Created\n\n"{fileDir}\{newfolder}"\n')


# Input directory names from a file, if folder exists skip
def create_folder_list(folders):
    f= open(folders, 'r')
    words = f.readlines()
    items = []
    for item in words:
        item = item[:-1] # This remove the character return
        items.append(item)

    for item in items:
        fileDir = os.path.dirname(os.path.abspath(__file__))
        newfolder = item

        if os.path.exists(newfolder):
            print(f'Folder "{fileDir}\{newfolder}" exists')
        else:
            print(f'Folder "{fileDir}\{newfolder}" created')
            os.makedirs(newfolder)


# make_new_path()
# make_relative_path()
# inputname_relative_path()
# create_folder_list('folders.txt')