#!/usr/bin/env python3

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the product
product = num1 * num2

# Determine if the product is positive, negative, or zero
if product > 0:
    print("The result is positive.")
elif product < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

# Display the multiplication result
print("Multiplication result:", product)