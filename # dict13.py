# Dict13
sklad = {
    'яблоки': (50, 10),
    'бананы': (60, 5),   
    'груши': (80, 10)  
}
total_cost = 0
most_expensive_name = None
max_item_cost = -1

for name, info in sklad.items():
    price = info[0]
    count = info[1]
    
    item_cost = price * count
    total_cost += item_cost
    
    if item_cost > max_item_cost:
        max_item_cost = item_cost
        most_expensive_name = name

print("Суммарная стоимость склада:", total_cost)
print("Самый дорогой предмет:", most_expensive_name)
