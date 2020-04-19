"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""
# type your code for "string and escape sequences" in between this single line comment and the one below it ------------

string1 = "This is a string in double quotes"
string2 = 'This is a string in single quotes'
string3 = "This is a string \"with the double quote escape\" sequence in it"
string4 = "This is a string 'with the sing quote escape' sequence in it"

# ----------------------------------------------------------------------------------------------------------------------


"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters. 
3.create a variable and assign it the "J" from the string assigned to the variable lannisters. 
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters. 
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters. 
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.

"""




# type your code for "accessing values by index and string slicing" in between this comment and the one below it -------

lannisters = "JamieCerseiTyrion"
stringA = lannisters[1]
stringJ = lannisters[0]
stringJamie = lannisters[:5]
stringCersei = lannisters[5:11]
stringTyrion = lannisters[11:]

# ----------------------------------------------------------------------------------------------------------------------

print(stringA, stringJ, stringJamie, stringCersei, stringTyrion)