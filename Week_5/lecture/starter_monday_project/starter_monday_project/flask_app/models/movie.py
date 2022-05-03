from flask_app.config.mysqlconnection import connectToMySQL
# May have to import your app in the future
# Will be linking the other models as needed in lecture

class Movie:
    def __init__(self, data): # data is a dictionary representing a record (row) from your database
        self.id = data["id"] # Column names must match from yhour database
        self.title = data["title"]
        self.genre = data["genre"]
        self.release_date = data["release_date"]
        self.box_office = data["box_office"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.director = None # Placeholder representing a Director

    # Your queries will go here.  "INSERT INTO ...."  These will be class methods
    # @classmethod

    # Future: You will use static methods to perform validations
    # @staticmethod