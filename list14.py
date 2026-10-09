A = [10, 20, 30, 20, 40]
D = 20                    

count_D = A.count(D)
index_D = A.index(D) if D in A else -1

print("Число вхождений:", count_D)
print("Индекс первого вхождения:", index_D)
