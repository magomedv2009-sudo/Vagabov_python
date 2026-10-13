#proc20
import math

def triangle_p(a, h):
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    return a + 2 * b

triangles = [(6, 4), (10, 12), (3, 5)] 
for i, (a, h) in enumerate(triangles, 1):
    print(f"Периметр треугольника {i}: {triangle_p(a, h):.2f}")
