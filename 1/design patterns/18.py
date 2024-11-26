class Memento:
    def __init__(self, state: str):
        self.state = state
class Editor:
    def __init__(self):
        self.state = ""

    def write(self, text: str):
        self.state += text

    def create_memento(self) -> Memento:
        return Memento(self.state)

    def restore(self, memento: Memento):
        self.state = memento.state

    def get_state(self) -> str:
        return self.state
class Caretaker:
    def __init__(self):
        self.mementos = []

    def save_memento(self, memento: Memento):
        self.mementos.append(memento)

    def get_memento(self, index: int) -> Memento:
        return self.mementos[index]
# Створення редактора та доглядача
editor = Editor()
caretaker = Caretaker()

# Редагування тексту
editor.write("Hello, ")
caretaker.save_memento(editor.create_memento())

editor.write("world!")
caretaker.save_memento(editor.create_memento())

# Виведення поточного стану
print("Current state:", editor.get_state())  # "Hello, world!"

# Відкат до попереднього стану
editor.restore(caretaker.get_memento(0))
print("State after undo:", editor.get_state())  # "Hello, "
