from subprocess import BELOW_NORMAL_PRIORITY_CLASS


print("Welcome to the coffee shop")
#input variable in following format nameofvariable = input()
name = input("What is your name?\n")
#To add to string add + variablename + unless at the beginning r end of sentence
#if else statements
#ctrl+tab backsteps off If for else
if name == "Ben":
    print("You're not welcome here evil Ben, get out!!!")
    exit()
else:
    print("Hello " + name + " Thank you for coming in today.\n\n")

menu = "Coffee, Green Tea, Chai, Cappuccino"
#\n means new line
print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 8

quantity = input("How many drinks would you like?\n")
#convert input from one type of variable to another
total = price * int(quantity)

print("Thank you for your order, your total is $" + str(total))
print("That sounds wonderful, " + name + ", we'll have your " + quantity + " " + order + " ready for you in a just a few moments")
