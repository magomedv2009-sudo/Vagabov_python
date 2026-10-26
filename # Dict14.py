# Dict14
d = {'a': 10, 'b': 5, 'c': 20, 'd': 2}
V = 6

keys_to_delete = [k for k, v in d.items() if v < V]

for k in keys_to_delete:
    del d[k]

print(len(d))
