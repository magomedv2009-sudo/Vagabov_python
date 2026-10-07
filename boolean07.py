# Boolean7. Проверить истинность высказывания: «Число В находится между числами А и С».
a = int(input())
b = int(input())
c = int(input())
print(a < b < c or c < b < a)
