from abc import ABC, abstractmethod
from random import randint, choice

# =========================
# Абстракція через Item
# =========================
class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass

# =========================
# Sword
# =========================
class Sword(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item):
        damage = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= damage
        return f"[Меч] {self.name} завдає {damage} шкоди. {another_item.name} залишилось {another_item.health} HP"

    def sharpening(self):
        self._sharp += 1
        return f"{self.name} підточено. Атака збільшена на 1 одиницю."

# =========================
# Axe
# =========================
class Axe(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power

    def attack(self, another_item):
        damage = self.__attack_power + randint(0, 20)
        another_item.health -= damage
        return f"[Сокира] {self.name} завдає {damage} шкоди. {another_item.name} залишилось {another_item.health} HP"

# =========================
# Bow
# =========================
class Bow(Item):
    def __init__(self, name, attack_power, range_power):
        super().__init__(name)
        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another_item):
        damage = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= damage
        return f"[Лук] {self.name} завдає {damage} шкоди. {another_item.name} залишилось {another_item.health} HP"

    def reload(self):
        self.range_power += 1
        return f"{self.name} перезаряджено. Дальність збільшена на 1."

# =========================
# Ігрова логіка
# =========================
# Створюємо зброю
player_weapon = choice([Sword("Ескалібур", 100), Axe("Кратос", 95), Bow("Арбалет", 80, 10)])
enemy_weapon = choice([Sword("Дракон", 90), Axe("Тор", 85), Bow("Сокіл", 75, 12)])

print(f"Ти обрав: {player_weapon.name}")
print(f"Ворог обрав: {enemy_weapon.name}")

turn = 1
while player_weapon.health > 0 and enemy_weapon.health > 0:
    print(f"\n=== Хід {turn} ===")
    
    # Користувач робить випадкову дію (для прикладу автоматично)
    action = randint(1, 2)  # 1 - атакувати, 2 - підсилити/перезарядити
    if action == 1:
        print(player_weapon.attack(enemy_weapon))
    else:
        if isinstance(player_weapon, Sword):
            print(player_weapon.sharpening())
        elif isinstance(player_weapon, Bow):
            print(player_weapon.reload())
        else:
            print(f"{player_weapon.name} не можна підсилити.")

    # Ворог атакує
    print(enemy_weapon.attack(player_weapon))

    # Перевірка здоров'я
    if player_weapon.health <= 0:
        print(f"\nТи програв! Перемога за {enemy_weapon.name}")
        break
    elif enemy_weapon.health <= 0:
        print(f"\nПеремога за {player_weapon.name}!")
        break

    turn += 1