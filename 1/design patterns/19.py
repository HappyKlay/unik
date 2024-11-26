from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float, humidity: float, pressure: float):
        pass
class Subject(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass
class WeatherStation(Subject):
    def __init__(self):
        self._observers = []
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def register(self, observer: Observer):
        self._observers.append(observer)

    def remove(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify()
class WeatherDisplay(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, temperature: float, humidity: float, pressure: float):
        print(f"{self.name} - Current conditions: {temperature}°C, {humidity}% humidity, {pressure} hPa pressure")
# Створення спостережуваного об'єкта та спостерігачів
weather_station = WeatherStation()

display1 = WeatherDisplay("Display 1")
display2 = WeatherDisplay("Display 2")

# Реєстрація спостерігачів
weather_station.register(display1)
weather_station.register(display2)

# Оновлення вимірів і сповіщення спостерігачів
weather_station.set_measurements(25.0, 60, 1012)

# Виведення:
# Display 1 - Current conditions: 25.0°C, 60% humidity, 1012 hPa pressure
# Display 2 - Current conditions: 25.0°C, 60% humidity, 1012 hPa pressure
