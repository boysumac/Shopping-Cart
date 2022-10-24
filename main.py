
from shopping_cart import ShoppingCart
from customer import Customer
from product import Product

my_customer = Customer("Jacque")

#identify items
blueberries = Product ("Blueberries", 5.99, "fruit")
milk = Product("Milk", 3.99, "dairy")
rice = Product("Rice", 1.99, "grain")

# print customer name
print(f"The customer is {my_customer.name}")    

#add items to cart
my_customer.add_to_cart(blueberries)
my_customer.add_to_cart(milk)
my_customer.add_to_cart(rice)

#calculate total cost
total_cost = my_customer.cart.cart_product_total()
print(f"Total cost of groceries for {my_customer.name} is $ {total_cost}")

# empty shopping cart
my_customer.cart.remove_items()
my_customer.view_items_cart()