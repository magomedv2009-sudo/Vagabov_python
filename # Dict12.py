# Dict12
d = {'a': 10, 'b': 20, 'c': 30}
reversed_d = {value: key for key, value in d.items()}
for item in reversed_d.items():
    print(item)
