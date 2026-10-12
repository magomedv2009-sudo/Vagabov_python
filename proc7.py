#proc7
def add_right_digit(d, k):
    
    return int(str(k) + str(d))

K = 100
D1 = 5
D2 = 9

print("--- Proc8 ---")
print(f"Стартовое число K: {K}")

K = add_right_digit(D1, K)
print(f"Шаг 1 (приписали {D1} справа): {K}")

K = add_right_digit(D2, K)
print(f"Шаг 2 (приписали {D2} справа): {K}")
