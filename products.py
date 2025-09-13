class Product:
    """Product class that manages inventory per item."""

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not isinstance(name, str) or name == "":
            raise TypeError("Name must be a string and cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

    def get_quantity(self):
        """Return the current quantity."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity; deactivate the product if it reaches zero."""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a human-readable representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buy a given quantity; update stock and return total price."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if quantity > self.quantity:
            raise ValueError(
                f"Not enough stock for {self.name}. "
                f"Requested {quantity}, available {self.quantity}."
            )

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()

        total_price = self.price * quantity
        return total_price
