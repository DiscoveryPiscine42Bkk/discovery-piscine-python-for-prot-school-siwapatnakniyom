#!/usr/bin/env python3
import sys

# Check if there are arguments (excluding script name)
if len(sys.argv) > 1:
    print(sys.argv[1])  # Print the first argument
else:
    print("none")  # Print "none" if no arguments are passed
