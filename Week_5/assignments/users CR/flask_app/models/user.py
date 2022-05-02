from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod
    def view_users(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(user)
        return users