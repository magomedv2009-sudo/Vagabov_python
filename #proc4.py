#proc4
def rect_ps(x1, y1, x2, y2):
    
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    P = 2 * (width + height)
    S = width * height
    return P, S
rectangles = [
    (0, 0, 3, 4),
    (1, 1, 5, 4),
    (-2, -2, 2, 2)
]
print("--- Proc5 ---")
for r in rectangles:
    p, s = rect_ps(*r)
    print(f"Прямоугольник {r}: Периметр = {p}, Площадь = {s}")
