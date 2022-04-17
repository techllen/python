import product
Product = product.Product

# Create a Store class with 2 attributes
class Store(Product):
    def __init__(self,name):
        self.name = name
        self.list_of_products = []
# Add the add_product method to the Store class
    def add_product(self,new_product):
        self.list_of_products.append(new_product)
        return self
# Add the sell_product method to the Store class
    def sell_product(self,id):
        for product_id in range(0,len(self.list_of_products)):
            if product_id == id:
                product_to_remove = self.list_of_products[id]
                self.list_of_products.pop(id)
                print(f"\n{product_to_remove.name} got removed from the store\n")
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

