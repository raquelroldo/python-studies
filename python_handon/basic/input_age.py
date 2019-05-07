# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 
# 100 years old."
import datetime

dt=datetime.datetime.now()
name = input("What is your name? ")
age = input("How old are you? ")
ag = int(age)

hundred = (100 - ag) + dt.year

print("Hello, ", name, "! You will turn 100 in ", hundred)
