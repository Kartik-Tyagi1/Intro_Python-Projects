"""
Importing Modules:
1.Use a generic import to import the "random" module
2.Use a universal import to get everything from the "math" module
3.Use a function import to get the exit() function from the "sys" module
4.Use a function from the random module to generate a float greater than or equal to 0 and less than 100 and
assign that
 number to a variable
5.use the sqrt() function from the math module to get the square root of the number from step 4 and assign
that to a
 variable
6.call the exit() function from the sys module with the variable from step 5 as what it will display
"""

# Generic Import for Random
import random


# Universal Import for Math
from math import *


# Function Import
from sys import exit

'''
random is the module and random is the function. 
Since it returns float between 0 and 1 we muliply by 100 to get our value
'''

spider = random.random() * 100
print(spider)

pig = sqrt(spider)

exit(pig)




