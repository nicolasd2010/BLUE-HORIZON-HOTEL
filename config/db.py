# un cursor es el objeto que usamos para interactuar con la base de datos
import pymysql.cursors


# esta clase nos darÃ¡ una instancia de una conexiÃ³n a nuestra base de datos
class MySQLConnection:
    def __init__(self, db):
        # cambiar el usuario y la contraseÃ±a segÃºn sea necesario
        connection = pymysql.connect(host = 'database-1.cfjebmevkzwv.us-east-1.rds.amazonaws.com',
                                    user = 'admin', 
                                    password = 'A1s2d3f4g5h6', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establecer la conexiÃ³n a la base de datos
        self.connection = connection
    # el mÃ©todo para consultar la base de datos
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query, data)
                if query.lower().find("insert") >= 0:
                    # las consultas INSERT devolverÃ¡n el NÃšMERO DE ID de la fila insertada
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # las consultas SELECT devolverÃ¡n los datos de la base de datos como una LISTA DE DICCIONARIOS
                    result = cursor.fetchall()
                    return result
                else:
                    # las consultas UPDATE y DELETE no devolverÃ¡n nada
                    self.connection.commit()
            except Exception as e:
                # si la consulta falla, el mÃ©todo devolverÃ¡ FALSE
                print("Something went wrong", e)
                return False
            finally:
                # cerrar la conexiÃ³n
                self.connection.close() 
# connectToMySQL recibe la base de datos que estamos usando y la usa para crear una instancia de MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)