from config.db import connectToMySQL

class Piezas:
    def __init__(self, data):
        self.id = data["id"]
        self.categorias = data["categorias"]
        self.nombre_habitacion = data["nombre_habitacion"]
        self.imagen = data["imagen"]
        self.descripcion = data["descripcion"]

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