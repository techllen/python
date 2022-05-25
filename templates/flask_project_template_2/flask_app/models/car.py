from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
import re
class Car:
    # initializing database name variable
    database_name = "car_deals"

    def __init__(self,data):
        self.id = data["id"]
        self.price = data["price"]
        self.model = data["model"]
        self.make = data["make"]
        self.year = data["year"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None
        
    # this method saves a car in the database
    @classmethod
    def save_car(cls,data):
        query = "INSERT INTO cars (price,model,make,year,description,user_id) VALUES(%(price)s,%(model)s,%(make)s,%(year)s,%(description)s,%(id)s)" 
        connectToMySQL(Car.database_name).query_db(query,data)
        
    # this method get all cars from the database
    @classmethod
    def get_all_cars_with_users(cls):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id"
        cars = connectToMySQL(Car.database_name).query_db(query)
        cars_from_db = []
        # checking if we found any car
        if len(cars) == 0:
            return []
        else:
        # turning car results to objects
            for car in cars:
                # create a car object
                this_car = cls(car)
                # print(this_car)
                # create dict for user data
                this_user_dict = {
                    "id":car["users.id"],
                    "first_name":car["first_name"],
                    "last_name":car["last_name"],
                    "email":car["email"],
                    "password":car["password"],
                    "created_at":car["users.created_at"],
                    "updated_at":car["users.updated_at"]
                }
                # create a user instance
                this_user = user.User(this_user_dict)
                # link user to the car
                this_car.user = this_user
                cars_from_db.append(this_car)
            # returning list of car objects
            return cars_from_db
        
    # this method get one car from the database
    @classmethod
    def get_one_car_by_id(cls,data):
        query = "SELECT * FROM cars WHERE id = %(id)s"
        car = connectToMySQL(Car.database_name).query_db(query,data)
        # print(car)
        # checking if we found any car
        if len(car) == 0: 
            return None
        else:
            return cls(car[0])
        
    # this method edit car entry in the database
    @classmethod
    def update_car(cls,data):
        query = "UPDATE cars SET price = %(price)s,model = %(model)s,make = %(make)s,year = %(year)s,description = %(description)s WHERE id = %(id)s" 
        connectToMySQL(Car.database_name).query_db(query,data)
        
    #this method gets one car with its user from the database
    @classmethod
    def get_one_car_with_user(cls, data):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id WHERE cars.id = %(id)s;"
        car = connectToMySQL(Car.database_name).query_db(query, data)
        print(f"cars: {car}")
        # checking result has car
        if len(car) == 0:
            return None 
        else:
            # Create the car instance
            this_car = cls(car[0]) 
            #dictionary for the user data
            user_data = {
                "id":car[0]["users.id"],
                "first_name":car[0]["first_name"],
                "last_name":car[0]["last_name"],
                "email":car[0]["email"],
                "password":car[0]["password"],
                "created_at":car[0]["users.created_at"],
                "updated_at":car[0]["users.updated_at"]
            }
            # Creating a user instance
            this_user = user.User(user_data)
            # Link this user to this car
            this_car.user = this_user
            # Return the car - with the user linked
            return this_car
        
    # this method deletes car entry in the database
    @classmethod
    def delete_car(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s" 
        connectToMySQL(Car.database_name).query_db(query,data)
        
    # this method validates car inputs
    @staticmethod
    def validate_car_inputs(car):
        is_valid = True
        # checking if all fields are present
        if len(car['price']) == 0 or len(car['model']) == 0 or len(car['make']) == 0 or len(car['year']) == 0 or len(car['description']) == 0:
            flash("-All fields must be filled","input-error")
            is_valid = False
        # checking if price and year are greater than 0
        # print(type(int(car['price'])))
        # checking for empty strings and 0
        if car['price'] == '' or int(car['price'] == 0 or car['year'] == '' or int(car['year']) == 0):
                flash("-Year and Price Must be Greater than 0","input-error")
                is_valid = False    
        return is_valid
    
    
