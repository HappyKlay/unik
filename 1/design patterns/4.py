import copy
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}(color={self.color})"
# Клас Коло
class Circle(Shape):
    def __init__(self, color: str, radius: int):
        super().__init__(color)
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{super().__str__()}, radius={self.radius}"

# Клас Прямокутник
class Rectangle(Shape):
    def __init__(self, color: str, width: int, height: int):
        super().__init__(color)
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{super().__str__()}, width={self.width}, height={self.height}"
# Створення об'єктів і їх копіювання
circle1 = Circle("Red", 10)
circle2 = circle1.clone()  # Копія круга
circle2.color = "Blue"

rectangle1 = Rectangle("Green", 20, 30)
rectangle2 = rectangle1.clone()  # Копія прямокутника
rectangle2.height = 40

# Вивід об'єктів
print(circle1)  # Виведе: Circle(color=Red), radius=10
print(circle2)  # Виведе: Circle(color=Blue), radius=10
print(rectangle1)  # Виведе: Rectangle(color=Green), width=20, height=30
print(rectangle2)  # Виведе: Rectangle(color=Green), width=20, height=40
