strings = ["apple", "banana", "kiwi", "pear", "cherry"] 

longest = shortest = strings[0]

for s in strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s

print(f"Самая длинная: '{longest}' (длина {len(longest)})")
print(f"Самая короткая: '{shortest}' (длина {len(shortest)})")
