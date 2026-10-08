#for12
N = int(input("Введите N (> 0): "))

product = 1.0
for i in range(1, N + 1):
    factor = 1.0 + i * 0.1
    product *= factor

print(f"Произведение {N} сомножителей: {product:.6f}")
