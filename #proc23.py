#proc23
def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
points = [(2, 3), (-4, 5), (1, -2)]
for i, (x, y) in enumerate(points, 1):
    print(f"Точка {i} находится в {quarter(x, y)}-й четверти")
