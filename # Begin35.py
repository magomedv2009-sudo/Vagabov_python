# Begin35
V = float(input("Скорость лодки в стоячей воде (V) в км/ч: "))
U = float(input("Скорость течения (U) в км/ч (U < V): "))
T1 = float(input("Время по озеру (T1) в ч: "))
T2 = float(input("Время против течения (T2) в ч: "))

S_lake = V * T1
S_river = (V - U) * T2
S_total = S_lake + S_river

print("Путь по озеру:", S_lake, "км")
print("Путь против течения:", S_river, "км")
print("Общий путь S:", S_total, "км")
