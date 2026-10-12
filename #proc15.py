#proc15
def shift_left3(a, b, c):
    return b, c, a

sets_to_shift_l = [
    (1, 2, 3), 
    (10, 20, 30)
]

print("--- Proc15 ---")
for s in sets_to_shift_l:
    print(f"Исходный набор {s} -> Сдвиг влево: {shift_left3(*s)}")
