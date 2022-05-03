from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    # this method retrieves all the dojos
    @classmethod
    def view_dojos(cls):
        query = 'SELECT * FROM dojos'
        dojos = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojo_list = []
        for dojo in dojos:
            dojo_list.append(dojo)
        return dojo_list
    # this method create a new dojo entry in the dojos table
    @classmethod
    def save_dojo(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s)'
        new_dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return new_dojo_id
    # this method retrieves all ninjas present in a specific dojo
    @classmethod
    def show_ninjas(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        # print(results)
        dojo = cls(results[0])
        for dojo_result in results:
            ninja_data = {
                'id' : data['id'],
                'first_name' : dojo_result['first_name'],
                'last_name' : dojo_result['last_name'],
                'age' : dojo_result['age'],
                'dojo_id' : dojo_result['dojo_id'],
                'created_at' : dojo_result['created_at'],
                'updated_at' : dojo_result['updated_at']
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

        