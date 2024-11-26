from abc import ABC, abstractmethod

class SupportHandler(ABC):
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle_request(self, request: str):
        pass
class Level1Support(SupportHandler):
    def handle_request(self, request: str):
        if request == "Basic issue":
            print("Level 1 support handling basic issue.")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("No one can handle this request.")

class Level2Support(SupportHandler):
    def handle_request(self, request: str):
        if request == "Intermediate issue":
            print("Level 2 support handling intermediate issue.")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("No one can handle this request.")

class Level3Support(SupportHandler):
    def handle_request(self, request: str):
        if request == "Advanced issue":
            print("Level 3 support handling advanced issue.")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("No one can handle this request.")
# Створюємо обробників
level1 = Level1Support()
level2 = Level2Support()
level3 = Level3Support()

# Пов'язуємо їх у ланцюг
level1.set_next(level2).set_next(level3)

# Клієнт відправляє запит
requests = ["Basic issue", "Intermediate issue", "Advanced issue", "Critical issue"]

for request in requests:
    print(f"Handling request: {request}")
    level1.handle_request(request)
    print("-" * 40)
