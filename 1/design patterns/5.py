class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Якщо екземпляр вже існує, повертаємо його
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value: str):
        if not hasattr(self, 'initialized'):  # Перевірка, щоб уникнути повторної ініціалізації
            self.value = value
            self.initialized = True

    def get_value(self):
        return self.value

    def set_value(self, value: str):
        self.value = value

# Тестування
singleton1 = Singleton("First Instance")
singleton2 = Singleton("Second Instance")

print(singleton1.get_value())  # Виведе: First Instance
print(singleton2.get_value())  # Виведе: First Instance (обидва екземпляри однакові)

# Перевірка, чи це один і той самий екземпляр
print(singleton1 is singleton2)  # Виведе: True
