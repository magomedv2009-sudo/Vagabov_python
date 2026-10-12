#proc8
def add_left_digit(d, k):
    
    return int(str(d) + str(k))

K = 100
D1 = 5
D2 = 9

print("--- Proc9 ---")
print(f"Стартовое число K: {K}")

K = add_left_digit(D1, K)
print(f"Шаг 1 (приписали {D1} слева): {K}")

K = add_left_digit(D2, K)
print(f"Шаг 2 (приписали {D2} слева): {K}")
