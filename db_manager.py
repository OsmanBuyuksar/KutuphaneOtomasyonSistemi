import mysql.connector

class DBManager():
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
    
    def getBooks(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()
    