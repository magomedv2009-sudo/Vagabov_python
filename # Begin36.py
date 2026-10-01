# Begin36
V1 = float(input("Скорость первого автомобиля (V1) в км/ч: "))
V2 = float(input("Скорость второго автомобиля (V2) в км/ч: "))
S = float(input("Начальное расстояние между ними (S) в км: "))
T = float(input("Время (T) в ч: "))

distance_after = S + (V1 + V2) * T
print("Расстояние через", T, "ч:", distance_after, "км")
