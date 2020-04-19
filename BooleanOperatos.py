"""
and, or, and not:
1.create a variable and set it equal to True using a statement containing an "and" Boolean operator
2.create a variable and set it equal to False using a statement containing an "and" Boolean operator
3.create a variable and set it equal to True using a statement containing an "or" Boolean operator
4.create a variable and set it equal to False using a statement containing an "or" Boolean operator
5.create a variable and set it equal to True using a statement containing an "not" Boolean operator
6.create a variable and set it equal to False using a statement containing an "not" Boolean operator
"""
# type your code for "and, or, and not" below this comment and above the one below it.---------------------------------

ex1 = True and True

ex2 = True and False

ex3 = True or False

ex4 = False or False

ex5 = not False

ex6 = not True

print(ex1, ex2, ex3, ex4, ex5, ex6)

# ----------------------------------------------------------------------------------------------------------------------
"""
order of operations for Boolean operators:
1.make var1 evaluate to False by changing or removing a single Boolean operator
2.make var2 evaluate to True by changing or removing a single Boolean operator
"""
# type your code for "order of operations for Boolean operators" below this comment and above the one below it. --------
var1 = not 3 > 1 and 5 != 2 or 6 == 6
var_1 = not 3 > 1 and 5 != 2 and 6 == 6
# step 1: not true and true or true
# step 2: false and true or true
# step 3: false or true
# step 4: true
# if we change the last or to an and then this will be false

print( var1, var_1)


var2 = 4 * 2 != 6 and not 7 % 6 == 1
var_2 = 4 * 2 != 6 and 7 % 6 == 1
# step 1: true and not true
# step 2: true and false
# step 3: false
# if we remove the not this evaluates to true

print(var2, var_2)





# ----------------------------------------------------------------------------------------------------------------------