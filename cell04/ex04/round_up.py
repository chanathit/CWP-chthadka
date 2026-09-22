#!/usr/bin/env python3
import math

try:
    num = float(input("Give me a number: "))
    print(math.ceil(num))
except ValueError:
    pass