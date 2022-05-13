from select import select
import this
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
class User:
    database_name = 'log_in_and_registration'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.messages = []
    # this methos creates user entry in the database
    @classmethod
    def register_user(cls,data):
        query = 'INSERT INTO users (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)' 
        # retrieving the id of created user for session
        user_id = connectToMySQL(User.database_name).query_db(query,data)
        return user_id
    # this method verifies users from our database
    @classmethod
    def verify_user(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        user = connectToMySQL(User.database_name).query_db(query,data)
        # print(user)
        # checking if we found any user
        if len(user) < 1:
            return False
        return cls(user[0])
    # this method get all users from our database
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        users = connectToMySQL(User.database_name).query_db(query)
        users_to_display = []
        # checking if we found any user
        if len(users) < 1:
            return False
        else:
        # turning user results to objects
            for user in users:
                this_user = cls(user)
                # print(this_user)
                users_to_display.append(this_user)
            # returning list of user objects
            return users_to_display
    
    # this method get one user from the database
    @classmethod
    def get_one_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        user = connectToMySQL(User.database_name).query_db(query,data)
        # print(user)
        # checking if we found any user
        if len(user) < 1:
            return False
        return cls(user[0])
    # this method flashed error messages only when invalid credentials have been entered in registration
    @staticmethod
    def user_validation(user):
        is_valid = True
        # regex to check for names validity
        name_regex = re.compile(r'^[a-zA-Z]')
        # regex to check for email validity
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # regex for password validity 
        password_regex = re.compile(r'^[a-zA-Z0-9]')
        # checking if First Name - letters only, at least 2 characters
        if not (name_regex.match(user['first_name']) and len(user['first_name'])>=2) :
            flash('- First name must be letters only and at least 2 letters','register-error')
            is_valid = False
        # checking if Last Name - letters only, at least 2 characters
        if not (name_regex.match(user['last_name']) and len(user['last_name'])>=2):
            # flash message and its category
            flash('- Last name must be letters only and at least 2 letters','register-error')
            is_valid = False
        # chacking for email format validity
        if not email_regex.match(user['email']):
            # flash message and its category
            flash('- Please enter a valid email address example:name@example.com','register-error')
            is_valid = False
        # checking for password validity 8 characters
        if not (len(user['password'])>=8):
            # flash message and its category
            flash('- Password must be at least 8 characters','register-error')
            is_valid = False
        # checking for match btn password and password confirmation field
        if not user['password'] == user['confirmed_password']:
            # flash message and its category
            flash('- Entered password must be the same as confirmed password','register-error')
            is_valid = False
        return is_valid
    # this method flashed error messages only when invalid credentials have been entered on logging in
    @staticmethod
    def user_login_validation(invalid_message):
        # flash invalid email message if email was not found
        if invalid_message == 'email_not_found':
            # flash message and its category
            flash('- User is not found,Please enter a valid email address example:name@example.com','login-error')
            is_valid = False
        # flash invalid password message if the password is incorrect
        if invalid_message == 'password_not_correct':
            # flash message and its category
            flash('- Password is not correct','login-error')
            
    
