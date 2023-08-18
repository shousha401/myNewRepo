# Get username
user_name = input("please enter your name: ")
# Getting user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Finding the largest number using nested if statements
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3

# Displaying the largest number
print(f"Hello {user_name}! The largest number is {largest}")
