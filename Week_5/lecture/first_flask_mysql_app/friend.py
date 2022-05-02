# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our databas
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL('first_flask_MySQL').query_db(query)
        friends = []
        for friend in results:
            friends.append( cls(friend))
        return friends            
    
    @classmethod
    def create_friend(cls,data):
        # prepared statements
        query = 'INSERT INTO friends (first_name,last_name,occupation) VALUES (%(first_name)s,%(last_name)s,%(occupation)s)'

        # data = {
        #     'first_name':'Andre',
        #     'last_name':'Bachwa',
        #     'occupation': 'Teacher'
        # }
        result = connectToMySQL('first_flask_MySQL').query_db(query,data)
        
        return result
    
    @classmethod
    def update_friend(cls):
        query = 'UPDATE friends SET occupation = %(occupation)s  where id = %(id)s'
        
        data = {
            'id':'4',
            'occupation':'Nurse'
        }
        
        connectToMySQL('first_flask_MySQL').query_db(query,data)

        

