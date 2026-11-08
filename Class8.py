class Hero:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "damage": self.damage
        }

    @staticmethod
    def from_dict(data):
        return Hero(data["name"], data["health"], data["damage"])

name = input()
hp = int(input())
dmg = float(input())
hero_first = Hero(name, hp, dmg)
save_data = hero_first.to_dict()
hero_restored = Hero.from_dict(save_data)
print(hero_restored.health)
