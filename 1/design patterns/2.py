from abc import ABC, abstractmethod

# Абстрактний клас для кнопок
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Абстрактний клас для чекбоксів
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass
# Світла кнопка
class LightButton(Button):
    def render(self):
        return "Rendering a light button"

# Темна кнопка
class DarkButton(Button):
    def render(self):
        return "Rendering a dark button"

# Світлий чекбокс
class LightCheckbox(Checkbox):
    def render(self):
        return "Rendering a light checkbox"

# Темний чекбокс
class DarkCheckbox(Checkbox):
    def render(self):
        return "Rendering a dark checkbox"
# Абстрактна фабрика для створення об'єктів
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
# Фабрика для світлої теми
class LightThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> Checkbox:
        return LightCheckbox()

# Фабрика для темної теми
class DarkThemeFactory(GUIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> Checkbox:
        return DarkCheckbox()
# Функція клієнта
def render_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())

# Використання світлої теми
light_factory = LightThemeFactory()
render_ui(light_factory)
# Виведе:
# Rendering a light button
# Rendering a light checkbox

# Використання темної теми
dark_factory = DarkThemeFactory()
render_ui(dark_factory)
# Виведе:
# Rendering a dark button
# Rendering a dark checkbox
