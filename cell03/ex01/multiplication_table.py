#!/usr/bin/env python3

try:
    print("Enter a number")
    num = int(input())
    
    i = 0
    while i <= 9:
        print(f"{i} x {num} = {i * num}")
        i += 1
except ValueError:
    pass