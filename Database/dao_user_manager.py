import mysql.connector
from Database.models import User

class UserDBManager():
    def __init__(self):
        self.connection = self.getConnection()
        self.cursor = self.connection.cursor()

    def getConnection(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="db_yazilim_lab"
        )
        return connection
    
    def login(self, name, password):
        self.cursor.execute(f'SELECT * FROM users where name = "{name}" and password = "{password}"')
        result = self.cursor.fetchone()
        if result == None:
            return None
        
        user = User(result[1], result[2], result[3], result[4])
        return user