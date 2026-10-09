try:
    a = int(input())
    b = int(input())
    res = a / b
    print(f"{res:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
