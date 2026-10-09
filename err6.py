s = input()

try:
    idx = int(input())
    print(s[idx])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")
