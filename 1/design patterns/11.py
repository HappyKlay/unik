from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self, x: int, y: int):
        pass
class Circle(Shape):
    def __init__(self, color: str):
        self.color = color  # Спільна властивість, що не змінюється
    def draw(self, x: int, y: int):
        print(f"Drawing a {self.color} circle at ({x}, {y})")
class ShapeFactory:
    def __init__(self):
        self._circles = {}  # Словник для зберігання існуючих кругів

    def get_circle(self, color: str) -> Shape:
        if color not in self._circles:
            self._circles[color] = Circle(color)  # Створюємо новий колір, якщо його ще не існує
        return self._circles[color]
# Створюємо фабрику об'єктів
factory = ShapeFactory()

# Отримуємо об'єкти через фабрику
circle1 = factory.get_circle("Red")
circle2 = factory.get_circle("Green")
circle3 = factory.get_circle("Red")  # Цей об'єкт вже існує, буде повернуто існуючий "Red" круг

# Малюємо кола
circle1.draw(1, 2)
circle2.draw(3, 4)
circle3.draw(5, 6)

# Перевіряємо, чи circle1 і circle3 це один об'єкт
print(circle1 is circle3)  # True, оскільки обидва це один об'єкт "Red"
