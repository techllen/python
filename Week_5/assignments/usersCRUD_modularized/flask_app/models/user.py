from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
    # This method retrieves users from database and add them to the array for the view
    @classmethod
    def view_users(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users
    # this method adds users to the database
    @classmethod
    def create_user(cls,data):
        query = 'INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s)'
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
    # this method select only one user from the database
    @classmethod
    def show_one_user(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s'
        single_user = connectToMySQL('users_schema').query_db(query,data)
        return single_user
    # this method update one user in the database
    @classmethod
    def update_user(cls,data):
        query = 'UPDATE users SET first_name = %(first_name)s,last_name = %(last_name)s ,email = %(email)s WHERE id = %(id)s'
        connectToMySQL('users_schema').query_db(query,data)
    # this method delete only one user from the database
    @classmethod
    def delete_user(cls,data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        connectToMySQL('users_schema').query_db(query,data)
