#!/usr/bin/env python3

# Ask the user for a number
user_input = input("Enter a number: ")

# Check if the input is a decimal (float) or an integer
try:
    num = float(user_input)
    if num == int(num):
        print(f"{user_input} is an integer.")
    else:
        print(f"{user_input} is a decimal (floating-point number).")
except ValueError:
    print("Invalid input! Please enter a valid number.")
