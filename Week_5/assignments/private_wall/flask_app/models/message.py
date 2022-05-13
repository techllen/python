from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    database_name = 'private_wall_db'

    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender = None
        
    # this method message entry in the database
    @classmethod
    def save_message(cls,data):
        query = 'INSERT INTO messages (content,sender_id,receiver_id) VALUES(%(content)s,%(sender_id)s,%(receiver_id)s)' 
        message_id = connectToMySQL(Message.database_name).query_db(query,data)
        return message_id
    
    @staticmethod
    def message_is_valid(message):
        print(f"message length is {len(message)}")
        if len(message) < 5:
            flash('- Message content should be at least 5 characters long','message-error')
            return False
        else:
            return True
