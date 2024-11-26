from abc import ABC, abstractmethod

# Базовий інтерфейс для всіх компонентів
class Text(ABC):
    @abstractmethod
    def render(self):
        pass
class PlainText(Text):
    def __init__(self, text: str):
        self.text = text

    def render(self):
        return self.text
class TextDecorator(Text):
    def __init__(self, text_component: Text):
        self._text_component = text_component

    def render(self):
        return self._text_component.render()
# Декоратор для форматування тексту жирним
class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{self._text_component.render()}</b>"

# Декоратор для форматування тексту курсивом
class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{self._text_component.render()}</i>"
# Створюємо простий текст
plain_text = PlainText("Hello, world!")

# Декоруємо текст жирним
bold_text = BoldDecorator(plain_text)

# Декоруємо жирний текст курсивом
italic_bold_text = ItalicDecorator(bold_text)

# Виводимо результат
print(italic_bold_text.render())  # Виведе: <i><b>Hello, world!</b></i>
