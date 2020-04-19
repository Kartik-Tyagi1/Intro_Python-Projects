"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------


def print_string():
    print("He's got super powers, he's no ordinary kid, he's Ben 10!")


# Functions need 2 or more lines between them and other lines of code
baruch = 5


def print_variable(a):
    print(a)


print_string()
print_variable(baruch)

# ----------------------------------------------------------------------------------------------------------------------

"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

var1 = 2
var2 = 4
var3 = 6


def subtract(a, b):
    print(a-b)


def multiply(a, b, c):
    print(a * b * c)


subtract(var1, var2)
multiply(var1, var2, var3)


# ----------------------------------------------------------------------------------------------------------------------

"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
 parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------

homie1 = 2.5
homie2 = 3.5
homie3 = 4.5


def division(a, b):
    c = a/b
    return c


def division_again(d, e, f):
    c = division(d, e)
    return(c/f)


test = division(homie1, homie2)
print(test)
print(division_again(homie1, homie2, homie3))

# ----------------------------------------------------------------------------------------------------------------------