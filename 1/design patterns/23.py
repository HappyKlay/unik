from abc import ABC, abstractmethod

class ItemVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_cd(self, cd):
        pass
class PriceCalculator(ItemVisitor):
    def visit_book(self, book):
        return book.price * 0.9  # Знижка на книгу 10%

    def visit_cd(self, cd):
        return cd.price * 1.1  # Ціна CD збільшується на 10%
class Item(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
class Book(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)

class CD(Item):
    def __init__(self, price):
        self.price = price

    def accept(self, visitor):
        return visitor.visit_cd(self)
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self, visitor):
        total = 0
        for item in self.items:
            total += item.accept(visitor)
        return total
# Створення об'єктів елементів
book1 = Book(30)
book2 = Book(20)
cd1 = CD(15)

# Створення кошика для покупок та додавання елементів
cart = ShoppingCart()
cart.add_item(book1)
cart.add_item(book2)
cart.add_item(cd1)

# Створення відвідувача для обчислення ціни
price_calculator = PriceCalculator()

# Обчислення загальної вартості
total = cart.calculate_total(price_calculator)
print(f"Total price: {total}")
