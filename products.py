class Product:
    """Product class that manages inventory per item"""
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if type(name) != str or name == "":
            raise TypeError("Name must be a string and cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError(f"Not enough stock for {self.name}. Requested {quantity}, available {self.quantity}.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        total_price = self.price * quantity
        return total_price
