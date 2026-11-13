# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ЗАБЫТАЯ ОБСЕРВАТОРИЯ»
# Автор: Вагабов Магомед
# Дата: 5.11.2026
# Версия: 1.0
#
# Правила боя, покупок, классы Hero и Enemy —
# в модуле dungeon.py. Сохранение забега —
# в save.json через Hero.to_dict/from_dict.
# Выход и Ctrl+C сохраняют, гибель стирает,
# newgame удаляет. При продолжении формуляр
# не перепечатывается (осознанное решение).
# ================================================

import random
import os
import json
import dungeon

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False
    class _Dummy:
        GREEN = ""
        YELLOW = ""
        RESET_ALL = ""
    Fore = _Dummy()
    Style = _Dummy()

VERSION = "1.0"

# --- Константы игры -------------------------------
num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "listen",
               "5": "torch", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink", "0": "exit"}

commands = ["look", "go", "go <direction>", "rest", "listen", "torch", "train",
            "descend", "leaders", "shop", "backpack", "drink potion",
            "buy <item> [count]", "map", "scout", "newgame", "exit"]

MENU = ["Что делаешь? (номер или команда; help — справка)",
        "1 - осмотреться (look)",
        "2 - идти вперёд (go)",
        "3 - отдохнуть (rest)",
        "4 - зажечь факел (torch)",
        "5 - тронуть звёздную карту (listen)",
        "6 - тренировка (train)",
        "7 - спуститься глубже (descend)",
        "8 - таблица лидеров (leaders)",
        "9 - магазин (shop)",
        "10 - рюкзак (backpack)",
        "11 - выпить зелье (drink)",
        "map - карта (map)",
        "scout - обход (scout)",
        "newgame - новый забег (newgame)",
        "0 - выйти из подземелья (exit)"]

# --- Карта и данные подземелья --------------------
MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"],
]

hero_r, hero_c = 4, 2
visited = {(4, 2)}

LOOT = {(1, 1): "старая монета", (2, 3): "пыльное зелье", (3, 3): "камень стража"}
found_loot = set()

DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}


# --- Функции ---------------------------------------

def parse_command(line):
    """Возвращает пару (verb, words): глагол и слова команды.

    Нормализует строку (strip, lower), режет на слова,
    переводит номер в глагол через num_to_verb.
    Пустая команда даёт ("", []).
    """
    cmd = line.strip().lower()
    words = cmd.split()
    if not words:
        return "", []
    verb = words[0]
    if cmd in num_to_verb:
        verb = num_to_verb[cmd]
    return verb, words


def write_save():
    """Собирает состояние забега и пишет его в save.json.

    Кортежи и множества превращает в списки: JSON их не знает.
    Возвращает None. Если герой ещё не создан — ничего не пишет.
    """
    if "hero" not in globals():
        return
    save = {}
    save["hero"] = hero.to_dict()
    save["gold"] = gold_total
    save["actions"] = actions
    save["enemies"] = enemies
    save["position"] = [hero_r, hero_c]
    save["visited"] = [list(p) for p in visited]
    save["loot"] = sorted(found_loot)
    save["max_health"] = max_health
    save["max_stamina"] = max_stamina
    save["ability_bonus"] = ability_bonus
    save["inventory"] = inventory
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.

    Возвращает None: контракт функции — печать, а не данные.
    """
    if not log:
        print("Ты ещё не сражался. Журнал пуст.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Таблица лидеров (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Самый сильный удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.

    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге не было боёв.")


def scout(r, c, seen):
    """Рекурсивный обход карты: сколько комнат доступно из (r, c).

    seen — множество посещённых клеток, одно на весь обход.
    """
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total


def colored(text, color):
    """Возвращает текст в цвете, если colorama доступна, иначе — как есть."""
    if COLOR:
        return color + text + Style.RESET_ALL
    return text


def new_run():
    """Сбрасывает состояние забега к стартовому (для команды newgame).

    Возвращает кортеж (hero, max_health, max_stamina, enemies,
    gold_total, ability_bonus, inventory, actions, hero_r, hero_c,
    visited, found_loot). Настройка героя остаётся прежней:
    newgame начинает новый забег с теми же характеристиками.
    """
    fresh_hero = dungeon.Hero(hero.name, hero.health, hero.strength,
                              hero.agility, hero.endurance)
    return (fresh_hero, fresh_hero.health, fresh_hero.stamina,
            ["призрак астронома", "каменный страж", "пещерный паук", "звёздная тень"],
            0, 0, {}, 0, 4, 2, {(4, 2)}, set())


# --- Заголовок ------------------------------------
title = "ПОДЗЕМЕЛЬЕ: ЗАБЫТАЯ ОБСЕРВАТОРИЯ"
frame = "=" * 38
print(frame)
print(" " + title + " ")
print(f" v{VERSION}")
print(frame)
print()

# --- Загрузка сохранения ---------------------------
loaded = None
if os.path.exists("save.json"):
    print("Найдено сохранение. Продолжить забег? (да/нет)")
    answer = input().strip().lower()
    if answer in ("да", "yes", "д", "y"):
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Сохранение повреждено. Начинаем новый забег.")
            loaded = None

# --- Знакомство, настройка или продолжение --------
if loaded is None:
    print("Как зовут героя?")
    hero_name = input()
    print(f"Добро пожаловать, {hero_name}!")
    print("Ты входишь в подземный зал. Пахнет пылью и старым железом, а над головой в темноте угадывается звёздная карта.")
    print()

    print("Настройка героя.")
    print("Здоровье, сила, ловкость, воля — по одному числу в строке:")
    while True:
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            will = int(input())
            if health <= 0:
                raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
            if strength < 0 or agility < 0 or will < 0:
                raise ValueError("Сила, ловкость и воля не могут быть отрицательными")
            if will > health:
                raise ValueError(f"Воля ({will}) не может быть выше здоровья ({health})")
            break
        except ValueError as e:
            print(f"{e}. Введите все четыре числа заново:")

    hero = dungeon.Hero(hero_name, health, strength, agility, will)
    max_health = health
    max_stamina = hero.stamina

    print(hero)
    print()

    enemies = ["призрак астронома", "каменный страж", "пещерный паук", "звёздная тень"]
    log = []
    gold_total = 0
    ability_bonus = 0
    inventory = {}
    actions = 0
else:
    hero = dungeon.Hero.from_dict(loaded["hero"])
    max_health = loaded.get("max_health", hero.health)
    max_stamina = loaded.get("max_stamina", hero.stamina)
    gold_total = loaded["gold"]
    actions = loaded["actions"]
    enemies = loaded["enemies"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    ability_bonus = loaded.get("ability_bonus", 0)
    inventory = loaded.get("inventory", {})
    log = []
    print(f"Забег продолжен: здоровье {hero.health}, золото {gold_total}, врагов осталось {len(enemies)}.")
    print()

# --- Главный цикл игры -----------------------------
running = True
outcome = "прерывание"
try:
    while running:
        print("\n".join(MENU))
        print()
        line = input()
        verb, words = parse_command(line)
        while verb == "":
            print("Пустая команда. Введи команду или номер.")
            line = input()
            verb, words = parse_command(line)
        match verb:
            case "look":
                print("Ты осматриваешься. Стены увиты ржавыми трубами, а на полу — обрывки карт с созвездиями.")
            case "go":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Ты находишь {item}! Уникальный лут: {len(found_loot)}.")
                        print(f"Ты шагаешь на {words[1]}. Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Нельзя идти на {words[1]}: стена или край карты.")
                else:
                    on_persistence = hero.spend_stamina(2)
                    if on_persistence:
                        print("Сил больше нет — ты идёшь на одном упорстве.")
                    else:
                        print("Ты осторожно идёшь вперёд. Под ногами скрипят старые механизмы.")
            case "rest":
                hero.stamina = hero.stamina + 3
                print("Ты присаживаешься у стены и переводишь дух. Силы понемногу возвращаются.")
            case "torch":
                hero.stamina = hero.stamina - 3
                print("Ты достаёшь огниво и высекаешь искру. Факел вспыхивает, и звёздная карта на потолке оживает.")
            case "listen":
                hero.endurance = hero.endurance + 1
                print("Ты касаешься звёздной карты. Под пальцами — холодный металл, и в груди разгорается воля.")
            case "train":
                strikes = 6
                total_damage = 0
                crit_count = 0
                print("Ты подходишь к старому бронзовому астролябию.")
                print("Когда-то на нём тренировались здешние астрономы — теперь он покрыт пылью и паутиной.")
                print()
                print(f"Наносишь {strikes} ударов.")
                for i in range(1, strikes + 1):
                    hit_damage, crit = hero.strike(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage
                hero.stamina = hero.stamina - 4
                print()
                print(f"Итог: {strikes} ударов, критических ударов: {crit_count}.")
                print(f"Общий урон: {total_damage:.1f}")
                print(f"Средний урон: {total_damage / strikes:.1f}")
            case "descend":
                if not enemies:
                    print("Ты спускаешься глубже, но подземелье пусто. Здесь больше никого нет.")
                else:
                    enemy_name = random.choice(enemies)
                    foe = dungeon.Enemy(enemy_name, dungeon.enemy_stats[enemy_name])
                    rounds, won, loot = dungeon.fight(foe, hero, ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy_name)
                        win_msg = f"{enemy_name.capitalize()} побеждён! В подземелье осталось врагов: {len(enemies)}. Добыча: {loot} золота."
                        print(colored(win_msg, Fore.YELLOW))
                    else:
                        print(f"{enemy_name.capitalize()} одолел тебя...")
                    print(f"Бой: {len(rounds)} раундов.")
            case "leaders":
                print_leaderboard(log)
            case "shop":
                print("Магазин:")
                for name, price in dungeon.prices.items():
                    print(f"{name}: {price} золота")
            case "backpack":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")
            case "drink":
                item = " ".join(words[1:]) or "potion"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет предмета «{item}».")
                else:
                    hero.heal(10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Ты выпиваешь {item}. Здоровье: {hero.health}. Осталось: {inventory.get(item, 0)}.")
            case "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])
                if item == "":
                    print("Купить что? Введи: buy <предмет>.")
                    continue
                if item not in dungeon.prices:
                    print("Такого предмета в магазине нет.")
                    continue
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    print(f"Куплено {qty} {item} за {dungeon.prices[item] * qty} золота. Осталось золота: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {dungeon.prices[item] * qty}, есть {gold_total}.")
            case "map":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))
            case "scout":
                seen = set()
                print(f"Разведка: доступно комнат — {scout(hero_r, hero_c, seen)}.")
            case "newgame":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                (hero, max_health, max_stamina, enemies,
                 gold_total, ability_bonus, inventory, actions,
                 hero_r, hero_c, visited, found_loot) = new_run()
                log = []
                print("Сохранение удалено. Забег начат с чистого листа.")
                continue
            case "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")
            case "exit":
                print("Ты поднимаешься по винтовой лестнице к свету. Обсерватория остаётся позади.")
                write_save()
                print("Прогресс сохранён.")
                outcome = "выход"
                running = False
            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введи 'help'.")
                continue
        if hero.health <= 0:
            print(f"{hero.name} падает без сил. Подземелье забирает ещё одного искателя.")
            if os.path.exists("save.json"):
                os.remove("save.json")
            outcome = "гибель"
            running = False
        if running:
            actions += 1
        print()
        state = f"Здоровье: {hero.health:3d}  Запас сил: {hero.stamina:3d}  Врагов осталось: {len(enemies)}  Золото: {gold_total}"
        print(colored(state, Fore.GREEN))
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
    write_save()
finally:
    print()
    print(frame)
    if "hero" in globals():
        if outcome == "гибель":
            print(f"Ты не дошёл, {hero.name}. Обсерватория осталась без ответа. Действий: {actions}.")
        elif outcome == "выход":
            print(f"Забег окончен, {hero.name}. Ты вынес из тьмы звёздную карту. Действий: {actions}.")
        else:
            print(f"Сеанс прерван, {hero.name}. Звёзды остались ждать. Действий: {actions}.")
        if inventory:
            print("Осталось в рюкзаке:")
            for name, qty in inventory.items():
                print(f"{name}: {qty} шт.")
        else:
            print("Осталось в рюкзаке: ничего.")
        print_run_summary(log)
    else:
        print("Сеанс завершён до создания героя.")
    print(frame)