A = 2.0  

K = 0
current_sum = 0.0

while current_sum + 1 / (K + 1) < A:
    K += 1
    current_sum += 1 / K

print("Наибольшее K:", K)
print("Сумма равна:", current_sum)
