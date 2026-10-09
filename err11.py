try:
    a = float(input())
    b = float(input())
    res = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{res:.2f}")
