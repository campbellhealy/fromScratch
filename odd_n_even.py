# odd_n_even.py
''' A small program to determine if an integer is odd or even
    After writing the basicd from scratch I decided to add in a few more features.
    1. Capturing ValueErrors for non=integer input
    2. Rolling the code to keep the program running
    3. Adding a Quit facility
    Clear the screen for each new entry with a pause to see the current result
    '''
import os

from time import sleep

def odd_n_even():
    os.system('cls') # Clear the console for a clean look
    print('\n\nIs the number  odd or end')
    print('  Only use whole numbers\n')
    print('    To quit press "0"')
    print('\n\n')
    try:
        i = (input('What is the number?  '))
    # Input of the value is a string and needs converted to an integer
        x = int(i)

    except ValueError: # Catch the input if it is not an integer
        print(f'\nYour input "{i}" was not a number')
        print(' Only use whole numbers, please.\n')
        sleep(3)
        odd_n_even() Restart

    if x == 0:
        exit()

    if (x % 2)== 0:
        print(f'\nNumber {x} is even\n')
        sleep(2)
        odd_n_even()
    else: 
        print(f'\nNumber {x} is odd\n')        
        sleep(2)
        odd_n_even()

odd_n_even()