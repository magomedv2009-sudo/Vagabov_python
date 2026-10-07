# Boolean15. Проверить истинность высказывания: «Ровно два из чисел А, В, С являются положительными».
a = int(input())
b = int(input())
c = int(input())
positive_count = (a > 0) + (b > 0) + (c > 0)
print(positive_count == 2)
