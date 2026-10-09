A = 2.0 
K = 0
current_sum = 0.0

while current_sum <= A:
    K += 1
    current_sum += 1 / K

print("Наименьшее K:", K)
print("Сумма равна:", current_sum)
