#!/usr/bin/env python3
import sys

# Check if there are at least two parameters
if len(sys.argv) > 2:
    print(" ".join(sys.argv[:0:-1]))  # Reverse and print arguments (excluding script name)
else:
    print("none")  # Print "none" if there are fewer than two parameters
