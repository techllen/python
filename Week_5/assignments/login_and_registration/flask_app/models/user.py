from select import select
from flask_app.conifg.mysqlconnection import connectToMySQL
class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # this methos creates user entry in the database
    @classmethod
    def register_user(cls,data):
        query = 'INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)' 
        # retrieving the id of created user for session
        user_id = connectToMySQL('log_in_and_registration').query_db(query,data)
        return user_id
    # this method verifies users from our database
    @classmethod
    def verify_user(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user = connectToMySQL('log_in_and_registration').query_db(query,data)
        print(user)
        # checking if we found any user
        if len(user) < 1:
            return False
        return cls(user[0])
        
