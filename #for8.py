#for8
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

product = 1
for number in range(A, B + 1):
    product *= number

print(f"Произведение чисел от {A} до {B}: {product}")
