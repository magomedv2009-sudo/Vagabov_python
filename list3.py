A = [1, 2, 3, 4, 5, 6]  

total_sum = sum(A)

even_prod = 1
for x in A[::2]:
    even_prod *= x

print("Сумма всех:", total_sum)
print("Произведение четных индексов:", even_prod)
