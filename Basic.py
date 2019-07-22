"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding
instructions clearly without using any shortcuts
"""
# Multiply 3 and any number
def mult(number):
  >>>  outcome = 3*9
print (3*9)



# adds two numbers together
def add(a, b):
number1 = 2
number2 = 100
sum = number1 + number2

print ('sum of {0} and {1} is {2}' .format(number1, number2, sum))




"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1,2,3,6]
def sumOfListNumbers(someList):

   x = 0
   for numbers in someList:
   x += numbers
 total += x

print(x)



# Program checker (do not change the lines below)
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4
