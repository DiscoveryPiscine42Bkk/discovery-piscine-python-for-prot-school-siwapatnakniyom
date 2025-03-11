#!/usr/bin/env python3

# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is greater than 25
if num > 25:
    print("Error")
else:
    # Loop from the input number up to 25
    for i in range(num, 26):
        print(i)