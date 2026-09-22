#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

for num in original_array:
    if num > 5:
        new_array.add(num + 2)

print(original_array)
print(new_array)