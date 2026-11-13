# ================================================
# МОДУЛЬ «DUNGEON» — правила игры
# Автор: Вагабов Магомед
# Дата: 20.10.2026
#
# Класс Hero: характеристики, урон, запас сил,
# правила траты и лечения. Класс Enemy: рабочая
# копия карточки на один бой. fight дерётся
# с объектами. Сохранение — Hero.to_dict
# и Hero.from_dict.
# ================================================

import random

# --- Цены и карточки врагов -----------------------
prices = {"potion": 10, "torch_oil": 15, "war_elixir": 40}

enemy_stats = {
    "призрак астронома": {"hp": 40, "damage": 5, "loot": 25},
    "каменный страж": {"hp": 55, "damage": 7, "loot": 30},
    "пещерный паук": {"hp": 25, "damage": 3, "loot": 12},
    "звёздная тень": {"hp": 15, "damage": 2, "loot": 6},
}


# --- Класс героя ----------------------------------

class Hero:
    """Герой забега: характеристики, урон, запас сил.

    Правила траты и лечения живут методами; игра помнит
    потолки забега и передаёт их параметром.
    """

    def __init__(self, name, health, strength, agility, endurance):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.damage = 10 + strength * 1.5
        self.crit_damage = self.damage * 2
        self.stamina = health // 10 + endurance

    def __str__(self):
        return f"{self.name}: health {self.health}, damage {self.damage:.1f}, stamina {self.stamina}"

    def strike(self, n):
        """Урон героя в удар номер n; возвращает пару (hit, crit)."""
        if n % 3 == 0:
            return self.crit_damage, True
        return self.damage, False

    def spend_stamina(self, cost):
        """Тратит cost сил. Если не хватает — списывает недостающее из здоровья.

        Возвращает True, если шли на упорстве (здоровье списано).
        """
        if self.stamina >= cost:
            self.stamina -= cost
            return False
        self.health -= cost - self.stamina
        self.stamina = 0
        return True

    def heal(self, amount, cap):
        """Лечит на amount, но не выше cap."""
        self.health = min(self.health + amount, cap)

    def to_dict(self):
        """Словарь для сохранения: имя, текущее состояние, характеристики."""
        return {"name": self.name, "health": self.health,
                "stamina": self.stamina, "strength": self.strength,
                "agility": self.agility, "endurance": self.endurance}

    @staticmethod
    def from_dict(data):
        """Собирает героя из словаря сохранения.

        После конструктора доводит stamina до файлового значения:
        конструктор пересчитывает её по endurance, а в файле — текущая.
        """
        hero = Hero(data["name"], data["health"], data["strength"],
                    data["agility"], data["endurance"])
        hero.stamina = data["stamina"]
        return hero


# --- Класс врага ----------------------------------

class Enemy:
    """Рабочая копия карточки врага на один бой.

    Баланс правится в enemy_stats, поведение — в классе.
    """

    def __init__(self, name, stats):
        self.name = name
        self.hp = stats["hp"]
        self.damage = stats["damage"]
        self.loot = stats["loot"]


# --- Бой ------------------------------------------

def fight(enemy, hero, bonus=0):
    """Бой с enemy до гибели одного из двоих.

    enemy — объект Enemy, hero — объект Hero. bonus — надбавка
    к урону героя; прибавляется ПОСЛЕ удвоения критом.
    Печатает строки раундов. Возвращает (rounds, won, loot).
    Здоровье героя живёт в объекте: вызывающий читает hero.health.
    """
    rounds = []
    round_n = 0
    print(f"Ты спускаешься по винтовой лестнице. Из темноты навстречу выходит {enemy.name}!")
    while enemy.hp > 0 and hero.health > 0:
        round_n += 1
        hit, crit = hero.strike(round_n)
        hit = hit + bonus
        enemy.hp -= hit
        line = f"Раунд {round_n}: ты наносишь {hit:.1f}"
        if crit:
            line += " урона — критический!"
        else:
            line += " урона."
        if enemy.hp <= 0:
            line += f" {enemy.name.capitalize()} повержен!"
            rounds.append([round_n, hit, 0])
        else:
            blow = enemy.damage
            hero.health -= blow
            line += f" Здоровье {enemy.name}: {enemy.hp:.1f}. {enemy.name.capitalize()} бьёт в ответ на {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy.hp <= 0
    loot = enemy.loot if won else 0
    return rounds, won, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.

    Возвращает (gold_left, ok). Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


if __name__ == "__main__":
    test_hero = Hero("Тест", 100, 7, 5, 4)
    test_enemy = Enemy("призрак астронома", enemy_stats["призрак астронома"])
    rounds, won, loot = fight(test_enemy, test_hero, 0)
    print(f"self-test: {len(rounds)} rounds, won={won}, loot={loot}")