A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C (между A и B): "))
AC = abs(C - A)
BC = abs(B - C)
product_AC_BC = AC * BC
print(f"Произведение длин AC и BC = {product_AC_BC}")
