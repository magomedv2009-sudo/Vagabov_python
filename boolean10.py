# Boolean10. Проверить истинность высказывания: «Ровно одно из чисел А и В нечетное».
a = int(input())
b = int(input())
odd_count = (a % 2 != 0) + (b % 2 != 0)
print(odd_count == 1)
