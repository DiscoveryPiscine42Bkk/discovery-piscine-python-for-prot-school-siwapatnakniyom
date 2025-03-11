#!/usr/bin/env python3

# Prompt the user to enter a number
num = int(input("Enter a number for the multiplication table: "))

# Display the multiplication table for the given number
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
