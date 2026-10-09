try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
    print(f"Принято: {age}")
except ValueError as e:
    if str(e) == "Возраст вне допустимого диапазона":
        print(f"Отклонено: {e}")
    else:
        raise e
