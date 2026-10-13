#proc24
def even(k):
    return k % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = sum(1 for x in numbers if even(x))
print(f"Количество чётных чисел в наборе: {even_count}")
