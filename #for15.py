#for15
A = float(input("Введите число A: "))
N = int(input("Введите степень N (> 0): "))

power = 1.0
for _ in range(N):
    power *= A

print(f"{A} в степени {N}: {power:.6f}")
