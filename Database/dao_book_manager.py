import mysql.connector
import Database.models as models

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
        books = self.cursor.fetchall()

        bookObjList = []
        for b in books:
            bookObj = models.Book(b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8])
            bookObjList.append(bookObj)

        return bookObjList
    
    def searchBooks(self, cat, text):
        dic = {'isbn': 'isbn', 'isim': 'name', 'yazar': 'writer', 'tür': 'topic','yayım tarihi': 'date','sayfa sayısı': 'page_count','kitap numarası': 'book_number', 'yayıncı':'publisher'}
        
        loweredText = str.lower(text)
        self.cursor.execute(f'SELECT * FROM books where {dic[cat]} = "{loweredText}"', )#türkçe karakter olunca hata veriyor
        
        print(f'SELECT * FROM books where {dic[cat]} = "{loweredText}"')
        books = self.cursor.fetchall()
        bookObjList = []
        for b in books:
            bookObj = models.Book(b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8])
            bookObjList.append(bookObj)

        return bookObjList
    