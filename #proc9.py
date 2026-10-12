#proc9
def minmax(x, y):

    return (x, y) if x < y else (y, x)


A, B, C, D = 15, 4, 42, 8

print("--- Proc11 ---")
print(f"Данные числа: {A}, {B}, {C}, {D}")

min1, max1 = minmax(A, B)      
min2, max2 = minmax(C, D)      
final_min, _ = minmax(min1, min2)  
_, final_max = minmax(max1, max2)  

print(f"Минимум = {final_min}, Максимум = {final_max}")
