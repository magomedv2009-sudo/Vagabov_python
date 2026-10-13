#proc25
import math

def is_square(k):
    if k <= 0:
        return False
    root = int(math.isqrt(k)) 
    return root * root == k
numbers = [4, 5, 9, 11, 16, 20, 25, 30, 36, 50]
squares_count = sum(1 for x in numbers if is_square(x))
print(f"Количество полных квадратов: {squares_count}")
