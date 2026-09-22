#!/usr/bin/env python3

correct_password = "Python is awesome"
user_input = input().strip()

if user_input == correct_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")