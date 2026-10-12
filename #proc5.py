#proc5
def invert_digits(k):

    sign = -1 if k < 0 else 1
    return sign * int(str(abs(k))[::-1])

numbers_to_invert = [123, 450, 9081, 7, 2468]

print("--- Proc7 ---")
for num in numbers_to_invert:
    print(f"Исходное: {num} -> Перевернутое: {invert_digits(num)}")
