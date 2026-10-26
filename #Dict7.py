#Dict7
d = {'a': 10, 'b': 50, 'c': 30}
max_key = None
for key in d:
    if max_key is None or d[key] > d[max_key]:
        max_key = key
print(max_key)
