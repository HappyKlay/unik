from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass

    @abstractmethod
    def eject_coin(self, context):
        pass

    @abstractmethod
    def turn_crank(self, context):
        pass

    @abstractmethod
    def dispense(self, context):
        pass
class NoCoinState(State):
    def insert_coin(self, context):
        print("Coin inserted.")
        context.state = context.has_coin_state

    def eject_coin(self, context):
        print("No coin to eject.")
    
    def turn_crank(self, context):
        print("No coin inserted.")

    def dispense(self, context):
        print("No coin inserted.")
    

class HasCoinState(State):
    def insert_coin(self, context):
        print("Coin already inserted.")

    def eject_coin(self, context):
        print("Coin ejected.")
        context.state = context.no_coin_state

    def turn_crank(self, context):
        print("Turned crank.")
        context.state = context.sold_state

    def dispense(self, context):
        print("You need to turn the crank first.")
    

class SoldState(State):
    def insert_coin(self, context):
        print("Please wait, dispensing in progress.")

    def eject_coin(self, context):
        print("Cannot eject coin, already turned the crank.")

    def turn_crank(self, context):
        print("Already turned the crank.")

    def dispense(self, context):
        print("Dispensing item.")
        context.state = context.no_coin_state
class GumballMachine:
    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.sold_state = SoldState()
        
        self.state = self.no_coin_state

    def insert_coin(self):
        self.state.insert_coin(self)

    def eject_coin(self):
        self.state.eject_coin(self)

    def turn_crank(self):
        self.state.turn_crank(self)
        self.state.dispense(self)
# Створення об'єкта автомату
gumball_machine = GumballMachine()

# Стан без монети
gumball_machine.insert_coin()  # Coin inserted.
gumball_machine.turn_crank()   # Turned crank. Dispensing item.
gumball_machine.eject_coin()  # No coin to eject.

# Стан з монетою
gumball_machine.insert_coin()  # Coin already inserted.
gumball_machine.eject_coin()  # Coin ejected.
gumball_machine.turn_crank()  # Turned crank. Dispensing item.
