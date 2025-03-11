#!/usr/bin/env python3
import sys

# Get the parameters (excluding script name)
params = sys.argv[1:]

if params:
    for param in params:
        if not param.endswith("ism"):
            print(param + "ism")
else:
    print("none")
