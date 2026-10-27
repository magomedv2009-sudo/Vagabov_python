S = input()
count = 0
for char in S:
    is_lowercase_latin = 'a' <= char <= 'z'
    is_lowercase_cyrillic = ('а' <= char <= 'я') or (char == 'ё')
    if is_lowercase_latin or is_lowercase_cyrillic:
        count += 1
print(count)
