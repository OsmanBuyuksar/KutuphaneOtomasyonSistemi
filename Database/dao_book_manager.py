import mysql.connector
import Database.models as models

class BookDBManager():
    def __init__(self):
        self.connection = self.getConnection()
        self.cursor = self.connection.cursor()

    def getConnection(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="db_yazilim_lab",
            buffered=True
        )
        return connection
    
    def getCursor(self):
        self.cursor = self.connection.cursor(buffered=True)
        return self.cursor

    def getBooks(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        bookObjList = []
        for b in books:
            bookObj = models.Book(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8])
            bookObjList.append(bookObj)

        return bookObjList
    
    def searchBooks(self, cat, text):
        dic = {'isbn': 'isbn', 'isim': 'name', 'yazar': 'writer', 'tür': 'topic','yayım tarihi': 'date','sayfa sayısı': 'page_count','kitap numarası': 'book_number', 'yayıncı':'publisher'}
        if len(cat) == 0 or len(text) == 0:
            raise Exception('Search category or the text is empty')
        
        self.cursor.execute(f'SELECT * FROM books where {dic[cat]} = "{text}"', )#türkçe karakter olunca hata veriyor

        print(f'SELECT * FROM books where {dic[cat]} = "{text}"')
        books = self.cursor.fetchall()
        bookObjList = []
        for b in books:
            bookObj = models.Book(b[0],b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8])
            bookObjList.append(bookObj)

        return bookObjList

    def addBook(self, isbn, name, writer, topic, date, page_count, book_number, publisher):
        sqlQuery = f"insert into books(isbn, name, writer, topic, date, page_count, book_number, publisher) values ('{isbn}','{name}','{writer}','{topic}','{date}','{page_count}','{book_number}','{publisher}')"
       
        self.cursor.execute(sqlQuery) 
        print(sqlQuery)

        sqlQuery2 = f"select * from books where isbn ='{isbn}' and name ='{name}' and writer = '{writer}' and topic = '{topic}' and date='{date}' and page_count = '{page_count}' and book_number = '{book_number}' and publisher = '{publisher}'"
        self.cursor.execute(sqlQuery2)
        return self.cursor.fetchone()[0]
    
    def deleteBook(self, id):
        sqlQuery = f"delete from books where idbooks= {id}"
        self.cursor.execute(sqlQuery)
        
        sqlQuery2 = f"select * from books where idbooks= {id}"
        self.cursor.execute(sqlQuery2)
        if self.cursor.fetchone() == None:
            return True
        else:
            return False
    #def changeBook(self, id, isbn, name, writer, topic, date, page_count, book_number, publisher):
        #sqlQuery = f"update books set isbn='{isbn}, isbn='{isbn}'"