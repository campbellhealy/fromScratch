import shutil
import os


file_path = 'V:\\Python\\pyBites'


def list_folders_files(path):
    '''
    Creat a list of folders and files.
    Slice, as a form of filter, the folders of interest
    '''
    path = path
    folders = os.listdir(path)
    folder_list = []
    for folder in folders[3:-18]:  # Slicing the folders from the list that I wanted
        folder_list.append(str(folder))
    return folder_list


def filecopy(*args):
    files = [*args]
    print(files)
    folders = list_folders_files(file_path)
    print(folders)
    for folder in folders:
        try:
            for file in files:
                print(f'{file_path}{folder}')
                shutil.copy(file, f'{file_path}{folder}')
        except SameFileError as e:
            print(f'File already Exists: {e}')
        except:
            print('Unknown error: '), sys.exec_info()

    print('Done')


# Tests
# print(list_folders_files('V:\Python\pyBites'))
filecopy('decorators.py', 'key_value_swapper.py', 'in_stock.py')
