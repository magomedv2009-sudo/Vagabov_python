N = 10 
K = 0
current_sum = 0

while current_sum + (K + 1) <= N:
    K += 1
    current_sum += K

print("Наибольшее K:", K)
print("Сумма равна:", current_sum)
