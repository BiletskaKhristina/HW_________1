from abc import ABC, abstractmethod
from random import randint, choice

# =========================
# Завдання 1: Інкапсуляція
# =========================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # приватний атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

# Симуляція операцій
account = BankAccount("Bohdan", 1000)
for _ in range(5):
    account.deposit(randint(50, 200))
    account.withdraw(randint(20, 150))
print(f"[Інкапсуляція] Кінцевий баланс: {account.get_balance()}\n")