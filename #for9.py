#for9
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

sum_squares = 0
for number in range(A, B + 1):
    sum_squares += number ** 2

print(f"Сумма квадратов от {A} до {B}: {sum_squares}")
