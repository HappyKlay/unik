from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass
class QuickSort(SortStrategy):
    def sort(self, data):
        print("Sorting using QuickSort")
        return sorted(data)  # Симуляція швидкого сортування

class BubbleSort(SortStrategy):
    def sort(self, data):
        print("Sorting using BubbleSort")
        # Реалізація сортування бульбашкою
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data
class SortedList:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
        self.data = []

    def set_strategy(self, strategy: SortStrategy):
        self._strategy = strategy

    def add_data(self, data):
        self.data = data

    def sort(self):
        self.data = self._strategy.sort(self.data)
# Створення контексту з конкретною стратегією сортування
sorted_list = SortedList(QuickSort())

# Додавання даних і сортування
sorted_list.add_data([5, 2, 9, 1, 5, 6])
sorted_list.sort()  # Виведе "Sorting using QuickSort"

# Зміна стратегії на BubbleSort
sorted_list.set_strategy(BubbleSort())
sorted_list.add_data([3, 8, 2, 5, 1])
sorted_list.sort()  # Виведе "Sorting using BubbleSort"
