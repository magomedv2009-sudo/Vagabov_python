#proc21
def sum_range(a, b):
    if a > b:
        return 0
    return (a + b) * (b - a + 1) // 2

A, B, C = 5, 10, 15
print(f"Сумма от {A} до {B}: {sum_range(A, B)}")
print(f"Сумма от {B} до {C}: {sum_range(B, C)}")
