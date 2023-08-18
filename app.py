# Hello World
print("Hello World")
# Draw A shape
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
# Printing a triangle shape
for i in range(5):
    print('*' * (i + 1))

# Variables & Data Types
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old. ")
print("he really liked the named " + character_name + ",")
print("but he didn't like being " + character_age + ".")
character_name = "Juan"
character_age = "70"
print("There once was a man named " + character_name + ",")
print("he was " + character_age + " years old. ")
print("he really liked the named " + character_name + ",")
print("but he didn't like being " + character_age + ".")

# Working With Strings
print("Fresno\nCity")
print("Fresno\"City")
print("Fresno City")
phrase = "Fresno City"
print(phrase)
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0]) # index start at 0
print(phrase.index("t"))
print(phrase.replace("City", "State"))

# Working With Numbers
print(1)
print(1.0934)
print(-1.9872)
print(1+5)
print(1+5.9)
print(1-5.9)
print(1*5.9)
print(1/5.9)
print(1 * 5 + 7)
print(1 * (5 + 7))
print(10 % 3)
my_num = (1 * 5 + 7)
print(my_num)
print(str(my_num) + " my Fav Number")
print(abs(my_num))
print(pow(3, 2))
print(pow(4, 6))
print(max(3, 2))
print(min(3, 2))
print(round(3.6))
from math import *
print(sqrt(36))

# Getting Input From Users
name = input("Enter you Name: ")
age = input("Enter you age: ")

print("Hello " + name + "!")
print("You are  " + age + "!")
print("Hello " + name + "! you are " + age)

# Build a basic calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)

# Mad Libs Game
color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("Enter a celebrity ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love "+celebrity)


































