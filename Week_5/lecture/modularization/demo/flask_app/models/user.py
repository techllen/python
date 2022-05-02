# import connection to mysql
from flask_app.config.mysqlconnection import connectToMySQL
# might have to import other model files
# from flask_app.models import inventory
# might have to import app for Bcrypt
# from flask import Flask

class User:
    # data is a dictionary
     def __init__(self,data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # inventory.Inventory()

@classmethod
def add_item(cls,data):
    query = 'INSERT INTO inventories (price,count) VALUES (%(first_name)s,%(last_name)s);'
    return connectToMySQL('user_schema').query_db(query,data)

# @staticmethod
# use them for validation