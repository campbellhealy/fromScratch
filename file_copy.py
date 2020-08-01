import shutil, os

def list_folders_files(path):
    '''
    Creat a list of folders and files.
    Slice out some folders
    '''
    path = path
    folders = os.listdir(path)
    folder_list = []
    for folder in folders[3:-18]: #Slicing the folders from the list
        folder_list.append(str(folder))
    return folder_list


def filecopy(*args):
    files = [*args]
    print(files)
    folders = list_folders_files('V:\Python\pyBites')
    print(folders)
    for folder in folders:
        try:
            for file in files:
                print(f'V:\Python\pyBites\{folder}')
                shutil.copy(file, f'V:\Python\pyBites\{folder}')
        except SameFileError as e:
            print(f'File already Exists: {e}')
        except:
            print('Unknown error: '), sys.exec_info()

    print('Done')

# Tests
# print(list_folders_files('V:\Python\pyBites'))
filecopy('decorators.py','key_value_swapper.py', 'in_stock.py')