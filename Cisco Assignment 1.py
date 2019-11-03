print("Cisco Assignment 1")
print('Rushan Rafiq')
print('Question 1')
print('Twinkle, twinkle, little star,\n\t\
How I wonder what you are!\n\t\t\
Up above the world so high,\n\t\t\
Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\
How I wonder what you are')

print('Question 2')
import sys
print("Python version")
print (sys.version)


print("Question 3")
import datetime
Date = datetime.datetime.now()
print(Date)


print("Question 4")
from math import pi
try:
    radius= int(input('Enter radius of the circle of whose area is to be calculated: '))
    A=pi*(radius**2)
    print("The Area of Circle is: ",A)
except ValueError:
    print("Please give integer value..!")


print("Question 4")
f_name=(input('Enter your First Name: '))
l_name=str(input('Enter your Last Name: '))
print('Hey!',l_name,' ',f_name)

print('Question 5')
try:
    num1=int(input("Enter first num: "))
    num2=int(input("Enter second num: "))
    print('Addition of two numbers will be: ',num1+num2)
except ValueError:
    print('Invalid Command!')
