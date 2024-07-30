from config.db import connectToMySQL

class Reservas:
    def __init__(self, data):
        self.id = data["id"]
        self.tipo_habitacion = data["tipo_habitacion"]
        self.fecha_entrada = data["fecha_entrada"]
        self.fecha_salida = data["fecha_salida"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM clientes;"
        results = connectToMySQL('habitaciones').query_db(query)
        gatitos = []
        for result in results:
            gatitos.append(cls(result))
        return gatitos

    @classmethod
    def get_all_filter(cls, search_term):
        query = f"SELECT * FROM gatos WHERE nombre LIKE '%{search_term}%';"
        results = connectToMySQL('habitaciones').query_db(query)
        gatitos = []
        for result in results:
            gatitos.append(cls(result))
        return gatitos

    @classmethod
    def get_gato(cls, id):
        query = "SELECT * FROM gatos WHERE id = " + id + ";"
        results = connectToMySQL('habitaciones').query_db(query)
        gatitos = []
        for result in results:
            gatitos.append(cls(result))
        return gatitos