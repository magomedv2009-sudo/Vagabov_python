#proc26
def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k //= 5
    return k == 1

numbers = [1, 5, 10, 25, 50, 125, 200, 625, 1000, 3125]
pow5_count = sum(1 for x in numbers if is_power5(x))
print(f"Количество степеней пятёрки: {pow5_count}")
