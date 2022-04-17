# Create a Store class with 2 attributes
from math import prod


class Store:
    def __init__(self,name):
        self.name = name
        self.list_of_products = []
# Add the add_product method to the Store class
    def add_product(self,new_product):
        self.list_of_products.append(new_product)
        return self
# Add the sell_product method to the Store class
    def sell_product(self,id):
        for id in range(0,len(self.list_of_products)):
            product_to_remove = self.list_of_products[id]
        self.list_of_products.remove(product_to_remove)
        print(f"You are about to delete {product_to_remove}")
        return self
# NINJA BONUS: Add the inflation method to the Store class
    def inflation(self,percent_increase):
        for product in self.list_of_products:
            product.update_price(percent_increase,True)
        return self
# NINJA BONUS: Add the set_clearance method to the Store class
    def set_clearance(self,category,percent_discount):
        for product in self.list_of_products:
            if product.category == category:
                product.update_price(percent_discount,False)

# Create a Product class with 3 attributes
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
# Add the update_price method to the Product class 
    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price += (self.price*(percent_change/100))
        else:
            self.price -= (self.price*(percent_change/100))
        return self
# Add the print_info method to the Product class
    def print_info(self):
        print(f"Product name: {self.name}\n Product category: {self.category}\n Product price: {self.price}")
        return self
        
# Test out your classes by creating an instance of the Store and a few instances of the Product class, 
# add those instances to the store instance, and then test out the methods.
whittset_store = Store("Whittset")

women_purses = Product("Catori Scoop Tote",60,"Women")

outdoor_equipments = Product("Ryobi Electric Lawn Mower",299,"electric equipments")

shoes = Product("Timberland",50,"Steel Toe Shoes")

# adding all products
whittset_store.add_product(women_purses).add_product(outdoor_equipments).add_product(shoes)

# sell product
# whittset_store.sell_product(1)

# updating price
# women_purses.update_price(10,False)

# printing information for all products
for product in whittset_store.list_of_products:
    product.print_info()
    
# whittset_store.inflation(10)

whittset_store.set_clearance("Women",10)

# printing information for all products after all price changes
for product in whittset_store.list_of_products:
    product.print_info()
