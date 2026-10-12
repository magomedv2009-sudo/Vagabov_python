#proc13
def sort_dec3(a, b, c):
 
    return tuple(sorted([a, b, c], reverse=True))

sets_to_sort = [
    (10, 30, 20), 
    (5, 1, 9)
]

print("--- Proc13 ---")
for s in sets_to_sort:
    print(f"Исходный набор {s} -> По убыванию: {sort_dec3(*s)}")
