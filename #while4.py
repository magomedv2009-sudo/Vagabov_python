#while4
N = 27  

is_power_of_3 = True
if N <= 0:
    is_power_of_3 = False
else:
    while N > 1:
        if N % 3 != 0:
            is_power_of_3 = False
            break
        N //= 3

print(is_power_of_3)  
