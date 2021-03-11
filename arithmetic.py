
from os import system
import operator
ops = { "+": operator.add, "-": operator.sub } # etc.

system('cls') # This clears the terminal to allow only the latest run to show


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

# This allows each problem total to be assessed
for problem in problems:
    # Split the string into components
    problem = problem.split()

    prob0 = int(problem[0])  # First number
    prob2 = int(problem[2]) # Second number

    # This gets the sum value
    if problem[1] == '+':
        x = prob0 + prob2
    else:
        x = prob0 - prob2

    # Sum Total
    print(prob0)
    print(problem[1], prob2)
    print("---------")
    print(x, '\n')

"""
Iterate over each item
Split each item into three components
    Convert [0] to an int
    Convert [1] to an operator
    Convert [2] to an int
    Perform a sum to get the answer
"""