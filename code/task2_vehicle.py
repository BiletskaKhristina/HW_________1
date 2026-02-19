# =========================
# Завдання 2: Наслідування
# =========================
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"
    
    def display_brand(self):  # новий метод
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"

car = Car("Toyota", "Camry", 5)
print(f"[Наслідування] {car.display_info()}")
print(f"[Наслідування] {car.display_brand()}\n")