"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it. -----------------------------

print("hello " + "world") #sting concatination which joins string, watch for spaces
num1 = 11
num2 = 38
string1 = str(num1) + str(num2) #string concat with numbers
print(string1)

# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
 [name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it.-----------------------------------

faveRestaurnt = input("What is your favorite resaurant?") #asks user question and requests response, spaceing matters
vactionSpot = input("What is a place that you'd like to visit?")
nickName = input("What is your nickname? If you don't have one, what is your first name?")

print("Your favorite restaurant is %s, you want to visit %s, and your nickname or first name is %s" %(faveRestaurnt, vactionSpot, nickName))

# %s is the place holder for variables so we can avoid breaks in quotations







# ----------------------------------------------------------------------------------------------------------------------