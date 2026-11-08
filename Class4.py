class Potion:
    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"

name = input()
price = int(input())
heal = int(input())

potion = Potion(name, price, heal)
print(potion.describe())
