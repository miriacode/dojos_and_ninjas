from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():
    def __init__(self, data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    #READ
    @classmethod
    def muestra_dojos(cls):
        query = 'SELECT * FROM dojos'
        result = connectToMySQL('dojos_y_ninjas').query_db(query)
        dojos = []
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos

    #READ (ONE)
    @classmethod
    def get_dojo_by_id(cls,data):
        #data = {'id': '1'}
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        result = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        doj = result[0]
        dojo = cls(doj)
        return dojo

    #CREATE
    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_y_ninjas').query_db( query, data )
        print(result)
        return result
