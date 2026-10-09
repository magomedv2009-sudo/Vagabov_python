A = [1, 5, 8, 2, 9]  

avg = sum(A) / len(A)
greater_than_avg = [x for x in A if x > avg]

print("Элементы больше среднего:", greater_than_avg)
print("Количество:", len(greater_than_avg))
