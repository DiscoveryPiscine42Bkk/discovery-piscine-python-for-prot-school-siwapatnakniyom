#!/usr/bin/env python3

import math  # Import math module for rounding up

# Ask the user for a number
user_input = input("Enter a number: ")

# Try converting the input to a float and round it up
try:
    num = float(user_input)
    rounded_num = math.ceil(num)
    print(f"The number {num} rounded up is {rounded_num}.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
