#proc29
def digit_count(k):
    if k <= 0:
        return 0
    return len(str(k))
    
five_numbers = [7, 42, 105, 9999, 123456]
for num in five_numbers:
    print(f"Число {num} содержит цифр: {digit_count(num)}")
