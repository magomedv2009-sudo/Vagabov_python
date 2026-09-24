import math

a = float(input("Введите неотрицательное число a: "))
b = float(input("Введите неотрицательное число b: "))
# Предполагается, что a >= 0 и b >= 0
avg_geometric = math.sqrt(a * b)
print(f"Среднее геометрическое = {avg_geometric}")
