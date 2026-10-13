#proc17
def roots_count(a, b, c):
    D = b**2 - 4 * a * c
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

equations = [(1, -3, 2), (1, 4, 4), (5, 2, 1)]  # (a, b, c)
for i, (a, b, c) in enumerate(equations, 1):
    print(f"Уравнение {i}: {roots_count(a, b, c)} корня(ей)")
