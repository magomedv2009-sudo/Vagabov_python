#Begin23
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

temp = A
A = B
B = C
C = temp
print("Новые значения: A =", A, "B =", B, "C =", C)
