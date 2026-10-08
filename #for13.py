#for13
N = int(input("Введите N (> 0): "))
result = 0.0
sign = 1  # начинаем с плюса

for i in range(1, N + 1):
    term = 1.0 + i * 0.1
    result += sign * term
    sign *= -1  # меняем знак на противоположный

print(f"Результат чередующейся суммы: {result:.6f}")
