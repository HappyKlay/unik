class DishSelector:
    def select_dish(self):
        print("Selecting a dish from the menu...")
class PaymentProcessor:
    def process_payment(self, amount: float):
        print(f"Processing payment of {amount}...")
class DeliveryService:
    def arrange_delivery(self):
        print("Arranging delivery of the food...")
class FoodOrderFacade:
    def __init__(self):
        self.dish_selector = DishSelector()
        self.payment_processor = PaymentProcessor()
        self.delivery_service = DeliveryService()

    def place_order(self, amount: float):
        print("Placing an order...")
        self.dish_selector.select_dish()
        self.payment_processor.process_payment(amount)
        self.delivery_service.arrange_delivery()
        print("Order placed successfully!")
# Клієнт працює через фасад
food_order = FoodOrderFacade()
food_order.place_order(20.50)
