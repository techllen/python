import store
import product
Store = store.Store
Product = product.Product

# Test out your classes by creating an instance of the Store and a few instances of the Product class, 
# add those instances to the store instance, and then test out the methods.
whittset_store = Store("Whittset")

women_purses = Product("Catori Scoop Tote",60,"Women")

outdoor_equipments = Product("Ryobi Electric Lawn Mower",299,"electric equipments")

shoes = Product("Timberland",50,"Steel Toe Shoes")

# adding all products
whittset_store.add_product(women_purses).add_product(outdoor_equipments).add_product(shoes)

# printing information for all products
print("*****************BEFORE METHOD APPLIED*************")
for product in whittset_store.list_of_products:
    product.print_info()

# generating id for testing selling method(we cant recall them from database.they will have to
# be fetched from memory)
# id_of_product_to_remove = whittset_store.list_of_products[0].id
id_of_product_to_remove = whittset_store.list_of_products[1].id
# id_of_product_to_remove = whittset_store.list_of_products[2].id

# TESTING THE METHODS
# sell product
whittset_store.sell_product(id_of_product_to_remove)

# updating price
# women_purses.update_price(10,False)

# Checking for inflation
# whittset_store.inflation(10)

# apply clearance
# whittset_store.set_clearance("Women",10)

# printing information for all products after all price changes
print("\n*****************AFTER METHOD APPLIED***************")
for product in whittset_store.list_of_products:
    product.print_info()

