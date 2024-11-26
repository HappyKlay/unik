class Car:
    def __init__(self):
        self.make = None
        self.model = None
        self.engine = None
        self.wheels = 0

    def __str__(self):
        return f"Car(make={self.make}, model={self.model}, engine={self.engine}, wheels={self.wheels})"
from abc import ABC, abstractmethod

class CarBuilder(ABC):
    @abstractmethod
    def set_make(self, make: str):
        pass

    @abstractmethod
    def set_model(self, model: str):
        pass

    @abstractmethod
    def set_engine(self, engine: str):
        pass

    @abstractmethod
    def set_wheels(self, wheels: int):
        pass

    @abstractmethod
    def get_result(self) -> Car:
        pass
class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_make(self, make: str):
        self.car.make = make

    def set_model(self, model: str):
        self.car.model = model

    def set_engine(self, engine: str):
        self.car.engine = engine

    def set_wheels(self, wheels: int):
        self.car.wheels = wheels

    def get_result(self) -> Car:
        return self.car
class Director:
    def __init__(self, builder: CarBuilder):
        self.builder = builder

    def construct_sports_car(self):
        self.builder.set_make("Porsche")
        self.builder.set_model("911")
        self.builder.set_engine("V6 Twin Turbo")
        self.builder.set_wheels(4)

    def construct_basic_car(self):
        self.builder.set_make("Toyota")
        self.builder.set_model("Corolla")
        self.builder.set_engine("Inline-4")
        self.builder.set_wheels(4)
# Побудова спортивного автомобіля
builder = SportsCarBuilder()
director = Director(builder)
director.construct_sports_car()
sports_car = builder.get_result()
print(sports_car)
# Виведе: Car(make=Porsche, model=911, engine=V6 Twin Turbo, wheels=4)

# Побудова базового автомобіля
builder = SportsCarBuilder()
director = Director(builder)
director.construct_basic_car()
basic_car = builder.get_result()
print(basic_car)
# Виведе: Car(make=Toyota, model=Corolla, engine=Inline-4, wheels=4)
