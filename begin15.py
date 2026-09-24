PI = 3.14
S = float(input("Введите площадь круга S: "))
R = (S / PI) ** 0.5  # sqrt(S / PI)
D = 2 * R
L = 2 * PI * R
print(f"Диаметр D = {D}")
print(f"Длина окружности L = {L}")
