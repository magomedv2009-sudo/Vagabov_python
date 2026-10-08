#for11
N = int(input("Введите N (> 0): "))

total = 0
for k in range(N, 2 * N + 1):
    total += k ** 2

print(f"Сумма квадратов от {N} до {2*N}: {total}")
