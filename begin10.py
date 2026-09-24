a = float(input("Введите ненулевое число a: "))
b = float(input("Введите ненулевое число b: "))
a2 = a ** 2
b2 = b ** 2

sum_sq = a2 + b2
diff_sq = a2 - b2
prod_sq = a2 * b2
quot_sq = a2 / b2  # b != 0 по условию

print(f"Сумма квадратов = {sum_sq}")
print(f"Разность квадратов = {diff_sq}")
print(f"Произведение квадратов = {prod_sq}")
print(f"Частное квадратов = {quot_sq}")
