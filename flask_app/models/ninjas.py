from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojos import Dojo


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
        dojo = Dojo.get_dojo_by_id({"id": data['dojo_id']})
        self.dojo = dojo
    

    #READ (ALL)
    @classmethod
    def muestra_ninjas(cls):
        query = "SELECT * FROM ninjas"
        results = connectToMySQL('dojos_y_ninjas').query_db(query)
        ninjas = []

        #VINCULANDO NINJAS CON DOJOS
        for n in results:
            ninj = cls(n)
            data = {
                "id": ninj.dojo_id
            }
            returnedDojo = Dojo.get_dojo_by_id(data)
            ninj.dojo = returnedDojo
            ninjas.append(cls(n))
        return ninjas

    #CREATE
    @classmethod
    def guardar(cls, formulario):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"
        result = connectToMySQL('dojos_y_ninjas').query_db(query, formulario)
        return result

    #READ
    @classmethod
    def get_ninjas_by_dojo_id(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        ninjas =[]
        print(results)
        for n in results:
            ninj = cls(n)
            data = {
                "id": ninj.dojo_id
            }
            returnedDojo = Dojo.get_dojo_by_id(data)
            ninj.dojo = returnedDojo
            ninjas.append(cls(n))
        
        return ninjas
    
