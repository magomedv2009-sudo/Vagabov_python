import os

name = input()
a = float(input())
d = float(input())

with open(name, "w", encoding="utf-8") as f:
    for i in range(10):
        val = a + i * d
        f.write(str(val) + "\n")
