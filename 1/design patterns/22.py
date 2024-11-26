from abc import ABC, abstractmethod

class DrinkTemplate(ABC):
    # Шаблонний метод, що задає загальний алгоритм
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    # Абстрактні методи, які мають бути реалізовані в підкласах
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    # Конкретні методи, які можна залишити незмінними
    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")
class Tea(DrinkTemplate):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")
class Coffee(DrinkTemplate):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")
# Створення об'єктів конкретних класів
tea = Tea()
coffee = Coffee()

# Приготування напоїв за допомогою шаблонного методу
print("Making tea:")
tea.prepare_recipe()

print("\nMaking coffee:")
coffee.prepare_recipe()
