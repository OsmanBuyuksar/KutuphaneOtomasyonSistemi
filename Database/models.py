class Book:
    def __init__(self, isbn, name, writer, topic, date, page_count, publisher, book_number):
        self.isbn = isbn
        self.name = name
        self.writer = writer
        self.topic = topic
        self.date = date
        self.page_count = page_count
        self.publisher = publisher
        self.book_number = book_number


    def __str__(self):
        return f'ISBN: {self.isbn}, Name: {self.name}, Writer: {self.writer}, Topic: {self.topic}, Date: {self.date}, Page Count: {self.page_count}, Publisher: {self.publisher}, Book Number: {self.book_number}'
    
    def name(self):
        return self.name
    
    def writer(self):  
        return self.writer
    
    def topic(self):
        return self.topic
    
    def date(self):
        return self.date
    
    def page_count(self):
        return self.page_count
    
    def publisher(self):
        return self.publisher
    
    def book_number(self):
        return self.book_number
    
    def isbn(self):
        return self.isbn
    

class User:
    def __init__(self, name, email, password, is_officer):
        self.name = name
        self.email = email
        self.password = password
        self.is_officer = is_officer


    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Password: {self.password}'
    
    def name(self):
        return self.name
    
    def email(self):
        return self.email
    
    def isOfficer(self):
        return self.is_officer


class Borrow:
    def __init__(self, user, book, borrow_date):
        self.user = user
        self.book = book
        self.borrow_date = borrow_date


    def __str__(self):
        return f'User: {self.user}, Book: {self.book}, Borrow Date: {self.borrow_date}, Return Date: {self.return_date}'
    
    def user(self):
        return self.user
    
    def book(self):
        return self.book
    
    def borrow_date(self):
        return self.borrow_date