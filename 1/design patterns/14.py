from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class Light:
    def turn_on(self):
        print("The light is ON.")
    
    def turn_off(self):
        print("The light is OFF.")
class TurnOnLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()

class TurnOffLightCommand(Command):
    def __init__(self, light: Light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()
# Створюємо об'єкти
light = Light()
turn_on_command = TurnOnLightCommand(light)
turn_off_command = TurnOffLightCommand(light)

# Створюємо пульт дистанційного керування
remote = RemoteControl()

# Встановлюємо команди
remote.set_command(turn_on_command)
remote.press_button()  # Включаємо світло

remote.set_command(turn_off_command)
remote.press_button()  # Вимикаємо світло
