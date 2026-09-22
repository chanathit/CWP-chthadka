#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    result = ""
    for char in text:
        if char == "z":
            result += "z"
    if len(result) > 0:
        print(result)
    else:
        print("none")
else:
    print("none")