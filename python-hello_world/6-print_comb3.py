#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        if x != y:
            print("{:02d}, {:02d}, ".format(x, y), end="")

print("89")
