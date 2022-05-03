from flask_app.config.mysqlconnection import connectToMySQL
# May have to import your app in the future
# Will be linking the other models as needed in lecture

class Director:
    def __init__(self, data): # data is a dictionary representing a record (row) from your database
        self.id = data["id"] # Column names must match from yhour database
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.birthdate = data["birthdate"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.movies = [] # Placeholder representing a bunch of Movies

    # Your queries will go here.  "INSERT INTO ...."  These will be class methods
    # @classmethod

    # Future: You will use static methods to perform validations
    # @staticmethod
