#proc2
import math

def triangle_ps(a):
   
    P = 3 * a
    S = (a**2) * math.sqrt(3) / 4
    return P, S

sides = [3, 5, 8.5]

print("--- Proc4 ---")
for side in sides:
    p, s = triangle_ps(side)
    print(f"Сторона {side}: Периметр = {p:.2f}, Площадь = {s:.2f}")
