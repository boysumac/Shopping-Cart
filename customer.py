
from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, product):
        self.cart.add_item(product)
        print(f"you have added {product.name} to your cart")

    def view_items_cart(self):
        for item in self.cart.items:
            print(f"{item.name} is in your cart")
        


