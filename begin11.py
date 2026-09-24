a = float(input("Введите ненулевое число a: "))
b = float(input("Введите ненулевое число b: "))
ma = abs(a)
mb = abs(b)

sum_mod = ma + mb
diff_mod = ma - mb
prod_mod = ma * mb
quot_mod = ma / mb  # mb > 0, так как b != 0

print(f"Сумма модулей = {sum_mod}")
print(f"Разность модулей = {diff_mod}")
print(f"Произведение модулей = {prod_mod}")
print(f"Частное модулей = {quot_mod}")
