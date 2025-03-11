#!/usr/bin/env python3
import sys

# Check if exactly one parameter is provided
if len(sys.argv) == 2:
    print(sys.argv[1].lower())  # Convert to lowercase and print
else:
    print("none")  # Print "none" if there are no or multiple parameters
