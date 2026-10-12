#proc11
def sort_dec3(a, b, c):
    """Возвращает три значения по убыванию."""
    return tuple(sorted([a, b, c], reverse=True))

# Упорядочить два набора
sets_to_sort = [
    (10, 30, 20), 
    (5, 1, 9)
]

print("--- Proc13 ---")
for s in sets_to_sort:
    print(f"Исходный набор {s} -> По убыванию: {sort_dec3(*s)}")
