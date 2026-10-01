# Begin33
X = float(input("X кг конфет стоит: "))
A = float(input("A рублей. Введите Y кг, для которого нужна цена: "))
price_per_kg = A / X
price_Y = price_per_kg * A  # тут опечатка: должно быть * Y
# Исправим:
Y = float(input("Сколько кг (Y) нужно? "))
price_per_kg = A / X
price_Y = price_per_kg * Y

print("Цена за 1 кг:", price_per_kg)
print("Цена за", Y, "кг:", price_Y)
