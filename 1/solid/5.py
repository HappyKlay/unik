from abc import ABC, abstractmethod

# Абстракція для сервісів сповіщення
class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Реалізація для Email
class EmailService(MessageService):
    def send(self, message):
        print(f"Sending email: {message}")


# Реалізація для SMS
class SMSService(MessageService):
    def send(self, message):
        print(f"Sending SMS: {message}")


# Високорівневий модуль залежить від абстракції
class Notification:
    def __init__(self, service: MessageService):
        self.service = service

    def send(self, message):
        self.service.send(message)
