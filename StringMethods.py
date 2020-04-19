"""
len() and str() practice:
1.create a variable and assign it the string "Python"
2.create another variable and assign it the length of the string assigned to the variable in step 1
3.create a variable and use string slicing and len() to assign it the length of the slice "yth" from the string assigned
 to the variable from step 1
4.create a variable and assign it the float 1.32
5.create a variable and assign it the string "2" from the float assigned to the variable from the last problem (use the
 str() string method for this)
"""
# type your code for "len() and str() practice" below this single line comment and above the one below it --------------

string = "python"
length = len(string) #assigns length of python to length
length2 = len(string[1:4]) #assigns lenth of yth to lenght 2
print(string, length , length2)

num = 1.32
print(num)

string2 = str(num) #converts num to string
string3 = string2[3] #assign 2 to string 3
print(string3)


# ----------------------------------------------------------------------------------------------------------------------
"""
.upper() and .lower() practice:
1.create a variable and assign it the string "upper" changed to "UPPER" using .upper()
2.create a variable and assign it the string "owe" from "LOWER" using string slicing and .lower()
"""
# type your code for ".upper() and .lower() practice" below this single line comment and above the one below it --------

string4 = "upPeR"
string5 = string4.upper() #makes string 4 upper case
print(string5)

string6 = "LOwEr"
string7 = string6.lower() #makes string 6 lower case
string8 = string7[1:4] #slices string 7 into owe
print(string7)
print(string8)






# ----------------------------------------------------------------------------------------------------------------------