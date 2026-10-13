#proc18
def circle_s(r):
    pi = 3.14
    return pi * (r ** 2)

radii = [3, 5, 7.5]
for i, r in enumerate(radii, 1):
    print(f"Площадь круга {i} (r={r}): {circle_s(r)}")
