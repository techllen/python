# import connection to mysql
from flask_app.config.mysqlconnection import connectToMySQL
# might have to import other model files
# might have to import app for Bcrypt
# from flask import Flask

class Inventory:
    # data is a dictionary
     def __init__(self,data):
        self.price = data['price']
        self.count = data['count']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        #self.user = non or self users

@classmethod
def add_item(cls,data):
    query = 'INSERT INTO inventories (price,count) VALUES (%(price)s,%(count)s);'
    return connectToMySQL('inventory_schema').query_db(query,data)

# @staticmethod
# use them for validation