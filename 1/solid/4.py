from abc import ABC, abstractmethod

# Інтерфейс для друку
class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

# Інтерфейс для сканування
class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

# Інтерфейс для факсу
class Fax(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass
