#!/usr/bin/env python3
import sys

# Check if exactly one parameter is provided
if len(sys.argv) == 2:
    param = sys.argv[1]
    user_input = input("Enter a word: ")  # Prompt the user for input
    
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")  # Print "none" if incorrect number of arguments
