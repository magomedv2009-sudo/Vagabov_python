# Begin34
X = float(input("Масса шоколадных конфет (X) в кг: "))
A = float(input("Цена шоколадных конфет (A) в руб: "))
Y = float(input("Масса ирисок (Y) в кг: "))
B = float(input("Цена ирисок (B) в руб: "))

price_choc = A / X
price_toff = B / Y
ratio = price_choc / price_toff

print("1 кг шоколадных конфет стоит:", price_choc)
print("1 кг ирисок стоит:", price_toff)
print("Шоколадные конфеты дороже в", ratio, "раз")
