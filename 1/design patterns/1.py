from abc import ABC, abstractmethod

# Базовий клас для транспорту
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass
# Клас для автомобіля
class Truck(Transport):
    def deliver(self):
        return "Delivery by truck on the road."

# Клас для корабля
class Ship(Transport):
    def deliver(self):
        return "Delivery by ship via sea."
# Базовий клас із фабричним методом
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        # Використовує фабричний метод для створення транспорту
        transport = self.create_transport()
        return transport.deliver()
# Логістика для наземних перевезень
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

# Логістика для морських перевезень
class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
