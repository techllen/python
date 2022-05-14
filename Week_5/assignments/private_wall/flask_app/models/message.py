from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    database_name = 'private_wall_db'

    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender =  data['sender']
        
        
    # this method message entry in the database
    @classmethod
    def save_message(cls,data):
        query = 'INSERT INTO messages (content,sender_id,receiver_id) VALUES(%(content)s,%(sender_id)s,%(receiver_id)s)' 
        message_id = connectToMySQL(Message.database_name).query_db(query,data)
        return message_id
    # this method validates the length of the message
    @staticmethod
    def validate_message(form):
        valid_message = True
        message = form["message"]
        # print(f"message length is {len(message)}")
        # checking for message length validity
        if len(message) < 5:
            flash('- Message content should be at least 5 characters long','message-error')
            valid_message = False
        else:
            valid_message
        return valid_message
    # this method gets all messages that has been sent to me 
    @classmethod
    def get_my_messages(cls,data):
        query = 'SELECT * FROM messages JOIN users ON messages.sender_id = users.id WHERE messages.receiver_id = %(id)s ;' 
        my_messages = connectToMySQL(Message.database_name).query_db(query,data)
        # print(my_messages)
        messages = []
        for message in my_messages:
            message_data = {
                "id": message['id'],
                "content": message['content'],
                "sender_id": message['sender_id'],
                "receiver_id": message['receiver_id'],
                "created_at": message['created_at'],
                "updated_at": message['updated_at'],
                "sender": message['first_name']
                }
            this_message = Message(message_data)
            # print(f"date = {message['created_at']}")
            messages.append(this_message)
        return messages
    # this method deletes messages from database
    @classmethod
    def delete_message(cls,data):
        query = 'DELETE FROM messages WHERE id = %(id)s' 
        my_messages = connectToMySQL(Message.database_name).query_db(query,data)
        
    # this method get all messages from database the user has sent to other people
    @classmethod
    def get_all_sent_messages(cls,data):
        query = 'SELECT * FROM messages WHERE sender_id = %(id)s' 
        sent_messages = connectToMySQL(Message.database_name).query_db(query,data)
        sent_messages_list = []
        for message in sent_messages:
                this_message =  Message(message)
                sent_messages_list.append(this_message)
        return sent_messages_list
        
