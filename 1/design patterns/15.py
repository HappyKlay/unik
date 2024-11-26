from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        """Перевірка наявності наступного елемента"""
        pass
    
    @abstractmethod
    def next(self):
        """Отримання наступного елемента"""
        pass
class BookIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def has_next(self) -> bool:
        return self._index < len(self._collection)

    def next(self):
        if self.has_next():
            book = self._collection[self._index]
            self._index += 1
            return book
        return None
class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass
class BookCollection(Aggregate):
    def __init__(self):
        self._books = []

    def add_book(self, book: str):
        self._books.append(book)

    def create_iterator(self) -> Iterator:
        return BookIterator(self._books)
# Створення колекції книг
book_collection = BookCollection()
book_collection.add_book("Book 1")
book_collection.add_book("Book 2")
book_collection.add_book("Book 3")

# Створення ітератора для колекції
iterator = book_collection.create_iterator()

# Ітерація через колекцію
while iterator.has_next():
    book = iterator.next()
    print(f"Book: {book}")
