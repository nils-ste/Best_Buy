class Store:
    """Store class, that manages inventory per store"""
    def __init__(self, products=None):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.products:
            total += product.quantity
        return total

    def get_all_products(self):
        products = []
        for product in self.products:
            if product.active:
                products.append(product)
        return products

    def order(self, shopping_list):
        for product, amount in shopping_list:
            if product not in self.products:
                raise ValueError(f"{product.name} is not sold in this store.")
            if not product.is_active():
                raise ValueError(f"{product.name} is inactive.")
            if amount <= 0:
                raise ValueError(f"Invalid amount for {product.name}: {amount}.")
            if amount > product.get_quantity():
                raise ValueError(
                    f"Not enough stock for {product.name}. "
                    f"Requested {amount}, available {product.get_quantity()}."
                )

        total_price = 0
        for product, amount in shopping_list:
            total_price += product.buy(amount)
        return total_price
