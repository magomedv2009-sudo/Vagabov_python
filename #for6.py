#for6
price_per_kg = float(input("Введите цену 1 кг конфет: "))

weight = 1.2
while weight <= 2.0 + 1e-9:    # небольшая погрешность учтена
    cost = price_per_kg * weight
    print(f"{weight:.1f} кг: {cost:.2f}")
    weight += 0.2
