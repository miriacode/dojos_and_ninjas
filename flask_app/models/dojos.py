from flask_app.config.mysqlconnection import connectToMySQL
#from flask_app.models.ninjas import Ninja

class Dojo():
    def __init__(self, data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #ninjas = Ninja.get_ninjas_by_dojo_id({"dojo_id": id})
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
        #Me busca un salon en base a su id y me regresa una instancia de classroom

        #Consulta en la base de datos el identificador que estuvieramos recibiendo
        query = 'SELECT * FROM dojos WHERE id = %(id)s'
        result = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        # [
        #   {1,DC, (hora), (hora)}
        # ]
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