#Dict9
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 30}
common_key = next(k for k in d1 if k in d2)
d1.update(d2)
print(len(d1), d1[common_key])
