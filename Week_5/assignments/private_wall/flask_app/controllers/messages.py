from flask_app.config.mysqlconnection import connectToMySQL
class Message:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender = None
        

