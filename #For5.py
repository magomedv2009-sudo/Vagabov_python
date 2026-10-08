#For5
price_per_kg = float(input("Введите цену 1 кг конфет: "))

for i in range(1, 11):          # i = 1..10
    weight = i * 0.1           # 0.1, 0.2, ..., 1.0
    cost = price_per_kg * weight
    print(f"{weight:.1f} кг: {cost:.2f}")

