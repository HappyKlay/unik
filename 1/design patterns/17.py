from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def send(self, message: str, colleague: "Colleague"):
        pass
class ChatRoom(Mediator):
    def __init__(self):
        self.colleagues = []

    def register(self, colleague: "Colleague"):
        self.colleagues.append(colleague)
        colleague.mediator = self

    def send(self, message: str, colleague: "Colleague"):
        for c in self.colleagues:
            if c != colleague:
                c.receive(message)
class Colleague(ABC):
    def __init__(self, name: str):
        self.name = name
        self.mediator = None

    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive(self, message: str):
        pass
class User(Colleague):
    def send(self, message: str):
        print(f"{self.name} sends: {message}")
        self.mediator.send(message, self)

    def receive(self, message: str):
        print(f"{self.name} receives: {message}")
# Створення посередника
chat_room = ChatRoom()

# Створення користувачів
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

# Реєстрація користувачів у чаті
chat_room.register(alice)
chat_room.register(bob)
chat_room.register(charlie)

# Користувачі надсилають повідомлення через посередника
alice.send("Hello, everyone!")
bob.send("Hi, Alice!")
charlie.send("Hey, Bob!")
