# folder_creator.py
from pathlib import Path
import list_names
''' 
Using Python 3.5 +
Windows 10

exist_ok= True
This prevents an exception error halting the process
'''
# def create_named_folders(thelist):
#     names = thelist
#     for i in range (len(names)):
#         for name in names:
#             Path(f"C:/Users/User/Desktop/PyBites/{name}").mkdir(parents=True, exist_ok=True)
#     return print('Done') # Console Message to tell user code has completed

# create_named_folders(list_names.male)
# create_named_folders(list_names.female)
# create_named_folders(list_names.surnames)

# What I actually needed was just numbered folders
for i in range (1, 300):

    Path(f"C:/Users/User/Desktop/PyBites/{i}").mkdir(parents=True, exist_ok=True)

print('Done') # Console Message to tell user code has completed
