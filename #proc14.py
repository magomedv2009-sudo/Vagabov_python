#proc14
def shift_right3(a, b, c):

    return c, a, b

sets_to_shift_r = [
    (1, 2, 3), 
    (10, 20, 30)
]

print("--- Proc14 ---")
for s in sets_to_shift_r:
    print(f"Исходный набор {s} -> Сдвиг вправо: {shift_right3(*s)}")
