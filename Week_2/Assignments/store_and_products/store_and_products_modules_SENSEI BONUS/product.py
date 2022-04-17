import uuid
# Create a Product class with 3 attributes
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
# Autogenerate IDs using Universal unique Identifier
        self.id = (uuid.uuid4().int)
# Add the update_price method to the Product class 
    def update_price(self,percent_change,is_increased):
        if is_increased == True:
            self.price += (self.price*(percent_change/100))
        else:
            self.price -= (self.price*(percent_change/100))
        return self
# Add the print_info method to the Product class
    def print_info(self):
        print(f"Product name: {self.name}\n Product category: {self.category}\n Product price: {self.price}\n Unique Product ID: {self.id}")
        return self
    