# delete_folder.py
'''
This is a selection of code that will delete folders and files in a Windows 10 system.
Written using Python 3.9
'''

import os
import shutil # Only for folders with content

# Convert Text to Raw Text
def raw(text):
    """Returns a raw string representation of text"""
    escape_dict={'\a':r'\a',
            '\b':r'\b',
            '\c':r'\c',
            '\f':r'\f',
            '\n':r'\n',
            '\r':r'\r',
            '\t':r'\t',
            '\v':r'\v',
            '\'':r'\'',
            '\"':r'\"',
            '\0':r'\0',
            '\1':r'\1',
            '\2':r'\2',
            '\3':r'\3',
            '\4':r'\4',
            '\5':r'\5',
            '\6':r'\6',
            '\7':r'\7',
            '\8':r'\8',
            '\9':r'\9'}
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string

# Delete a file, check if file does not exist
def delete_file(thing):
    delfile = raw(thing)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    oldfile = os.path.join(fileDir,delfile)
    if os.path.exists(oldfile):
        os.unlink(oldfile)
        print(f'File "{oldfile}" \nDeleted')
    else:
        print(f'File "{oldfile}" \nDoes Not Exist')

# Delete an Empty Folder
def del_empty_folder(thing):
    delfolder = raw(thing)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    oldfolder = os.path.join(fileDir,delfolder) 
    if os.path.exists(oldfolder):
        os.rmdir(oldfolder)
        print(f'Folder "{oldfolder}" \nDeleted')
    else:
        print(f'Folder "{oldfolder}" \nDoes Not Exist')

# Delete a folder with content, not caring about content
def del_content_folder(thing):
    delfolder = raw(thing)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    oldfolder = os.path.join(fileDir,delfolder) 
    if os.path.exists(oldfolder):
        shutil.rmtree(oldfolder)
        print(f'Folder "{oldfolder}" \nDeleted')
    else:
        print(f'Folder "{oldfolder}" \nDoes not exist')


# Delete folders/subfolders with no content in relative path, with check for content
# *** ONLY USE CLI ***
def del_folders_subfolder_content(thing):
    # Use the raw function to convert the string input
    delfolder = raw(thing)
    fileDir = os.path.dirname(os.path.abspath(__file__))
    del_path = os.path.join(fileDir,delfolder)
    y = []
    for del_path, dirs, files in os.walk(del_path):
        if files:
            # Deletion of files in the root folder and any subfolders
            print(f'{del_path} has files\n')
            for name in files:
                print(os.path.join(del_path, name))
                # Do you want to Delete this content?
                ques = input(f'Do you want to delete {name}?\n ').lower()
                if ques == 'y':
                    name = os.path.join(del_path, name)
                    os.unlink(name)
                    print(f'{name} \nDeleted\n')
                else:
                    print('Okay, files sorted \n')

        if dirs:
            # Deletion of folder, after deletion of sub folders further (from the root first)
            for name in dirs:
                x = (os.path.join(del_path, name))
                y.append(x)
    for item in range(len (y)):
        item = y.pop()
        print(f'The lowet subfolder is {item}\n')
    # Do you want to Delete this content?
        ques = input(f'Do you want to delete {item}?\n ').lower()
        if ques == 'y':
            os.rmdir(item)
            print(f'{item} \nDeleted\n')
        else:
            print('Okay no more folders to delete\n') 



# Make sure not to lead with a \ in the argument

# delete_file('rubbish\file1.txt')
# del_empty_folder('rubbish\folder2')
# del_content_folder('rubbish\folder3')
# del_folders_subfolder_content('rubbish\ffolder3')
