# =========================
# Завдання 3: Поліморфізм
# =========================
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    pass  # Метод speak не реалізовано

animals = [Dog(), Cat(), Fish()]
for animal in animals:
    try:
        print(f"[Поліморфізм] {animal.__class__.__name__}: {animal.speak()}")
    except AttributeError:
        print(f"[Поліморфізм] {animal.__class__.__name__} не має методу speak()")