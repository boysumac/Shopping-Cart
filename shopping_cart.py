

class ShoppingCart:
    def __init__(self) -> None:
        self.items = []

 #calculate total cost of items in cart   
    def cart_product_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
        
    
# Add items to shopping cart and print

    def add_item(self, product):
        self.items.append(product)
        print (f"you have added {product.name} to your cart")

    def remove_items(self):
        self.items.clear()
        print ("You have removed all items from your cart")




    