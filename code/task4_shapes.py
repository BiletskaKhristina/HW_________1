from abc import ABC, abstractmethod
from random import randint

# Абстрактний клас Item задає загальний інтерфейс для всіх типів зброї
class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        """Кожна зброя повинна реалізувати свій метод атаки"""
        pass

# Конкретні реалізації зброї наслідують Item
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

class Axe(Item):
    def __init__(self, name, attack_power):
        super().__init__(name)
        self.__attack_power = attack_power

    def attack(self, another_item):
        damage = self.__attack_power + randint(0, 20)
        another_item.health -= damage
        return f"[Сокира] {self.name} завдає {damage} шкоди. {another_item.name} залишилось {another_item.health} HP"

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
        return f"{self.name} збільшив дальність до {self.range_power}"


# Приклад використання абстракції
S = Sword("Ескалібур", 100)
A = Axe("Кратос", 95)
B = Bow("Арбалет", 80, 10)

# Список всіх зброї демонструє абстракцію:
weapons = [S, A, B]
for weapon in weapons:
    # Неможливо створити об'єкт Item напряму
    # а виклик attack() залежить від конкретного типу зброї
    print(weapon.attack(B))