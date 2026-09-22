#!/usr/bin/env python3

def add_one(number):
    number = number + 1
    print(f"Inside the method: {number}")

my_var = 5
print(f"Before calling add_one: {my_var}")

add_one(my_var)

print(f"After calling add_one: {my_var}")