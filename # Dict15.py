# Dict15
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30, 'd': 40}

ignored_count = 0

for k, v in d2.items():
    if k not in d1:
        d1[k] = v
    else:
        ignored_count += 1

print(len(d1), ignored_count)
