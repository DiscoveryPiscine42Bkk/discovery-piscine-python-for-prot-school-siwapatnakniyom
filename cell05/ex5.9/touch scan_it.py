#!/usr/bin/env python3
import sys

# Check if exactly two parameters are provided
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    count = text.count(keyword)  # Count occurrences of keyword in text
    
    if count > 0:
        print(count)  # Print the count if found
    else:
        print("none")  # Print "none" if keyword is not in text
else:
    print("none")  # Print "none" if incorrect number of arguments
