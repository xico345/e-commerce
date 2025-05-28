# Product Class
class Product:
    def __init__(self, id, name, price, stock, description=""):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.description = description

    def update_stock(self, quantity):
        self.stock -= quantity

    def display_info(self):
        print(f"{self.name} - Price: {self.price} - Stock: {self.stock}")


# ShoppingCart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
            print(f"{quantity} unit(s) of {product.name} added to the cart.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]
            print(f"{product.name} removed from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def display_items(self):
        print("Items in Cart:")
        for product, quantity in self.items.items():
            print(f"{product.name} - Quantity: {quantity}")


# Order Class
class Order:
    def __init__(self, user, items, total):
        self.user = user
        self.items = items
        self.total = total
        self.status = "Pending"

    def process_order(self):
        for product, quantity in self.items.items():
            product.update_stock(quantity)
        self.status = "Processed"
        print("Order processed successfully!")

    def display_details(self):
        print(f"Order for {self.user.name} - Total: {self.total} - Status: {self.status}")


# User Class
class User:
    def __init__(self, id, name, email, address):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)

    def display_info(self):
        print(f"User: {self.name} - Email: {self.email} - Address: {self.address}")