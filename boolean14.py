# Boolean14. Проверить истинность высказывания: «Ровно одно из чисел А, В, С положительное».
a = int(input())
b = int(input())
c = int(input())
positive_count = (a > 0) + (b > 0) + (c > 0)
print(positive_count == 1)
