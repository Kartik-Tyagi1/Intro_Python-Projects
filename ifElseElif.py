"""
For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.
1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
 for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
 Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
 have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
 input number.
 Vending Machine:
 1.water = $1.00
 2.cola = $1.50
 3.gatorade = $2.00




2.After placing an order, the user should be prompted to enter inputs 4 times:
 1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
 number to a variable as an integer.
 2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
 number to a variable as an integer.
 3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
 number to a variable as an integer.
 4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
 number to a variable as an integer.




3.Create a variable to hold the total value of all the coins the user has put into the machine.



4.Use flow control statements to print the user's change or output a message asking the user to try again depending
 on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()
"""


import sys

print("What Drink Would You Like? Water is $1.00, Cola is $1.50, Gatorade is $2.00")
choice = int(input("Press 1 for Water, Press 2 for Cola, Press 3 for Gatorade"))


# PART 1
# This portion is where the user chooses which drink they want. Depending on the choice
# The variable price is assigned the price of the drink

price = 0.0
item = ""

if choice == 1:
    price = 1.00
    item = "Water"
elif choice == 2:
    price = 1.50
    item = "Cola"
elif choice == 3:
    price = 2.00
    item = "Gatorade"
else:
    sys.exit("Please Try Again")

# END OF PART 1


# PART 2/3
# This part is where the user inputs the amount of coins they need to
# And where the amount is totaled up

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

amount_1 = int(input("Please insert amount of quarters"))
amount_2 = int(input("Please insert amount of dimes"))
amount_3 = int(input("Please insert amount of nickels"))
amount_4 = int(input("Please insert amount of pennies"))

total = (quarters * amount_1) + (dimes * amount_2) + (nickles * amount_3) + (pennies * amount_4)

# END OF PART 2/3


# PART 4

change = 0.0

if total == price:
    print("Here Is Your %s! Your change is $ %f. Have A Nice Day!" %(item, change))
elif total > price:
    change = total - price
    print("Here Is Your %s. Your change is $ %f. Have A Nice Day!" %(item, change))
else:
    print("That Is Not Enough For %s. Please Insert More Coins" %(item))



























