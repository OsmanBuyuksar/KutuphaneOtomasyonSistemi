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
    
    def searchBooks(self, cat, text):
        dic = {'isbn': 'isbn', 'isim': 'name', 'yazar': 'writer', 'tür': 'topic','yayım tarihi': 'date','sayfa sayısı': 'page_count','kitap numarası': 'book_number', 'yayıncı':'publisher'}
        loweredText = str.lower(text)
        print(f'SELECT * FROM books where {dic[cat]} = "{loweredText}"')
        self.cursor.execute(f'SELECT * FROM books where {dic[cat]} = "{loweredText}"', )#türkçe karakter olunca hata veriyor
        return self.cursor.fetchall()
    