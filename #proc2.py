#proc2
def power_a234(a):
    
    return a**2, a**3, a**4


numbers = [2, 3, 5, 1.5, 10]

print("--- Proc2 ---")
for num in numbers:
    p2, p3, p4 = power_a234(num)
    print(f"Число {num}: 2-я ст. = {p2}, 3-я ст. = {p3}, 4-я ст. = {p4}")
