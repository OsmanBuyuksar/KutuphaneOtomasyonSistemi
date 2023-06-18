from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc

import Database.dao_book_manager as book_manager

from PyQt5.uic import loadUiType



officer_ui, base = loadUiType('OfficerWindow.ui')

class OfficerWindow(base, officer_ui):
    def __init__(self):
        base.__init__(self)
        self.setupUi(self)
        
        self.dbManager = book_manager.BookDBManager()
        self.buttonHandling()
        self.showBooks()

    def buttonHandling(self):
        self.addBookBtn.clicked.connect(self.addBook)
        self.bookTabBtn.clicked.connect(self.openBooksTab)

    def openBooksTab(self):
        self.tabWidget.setCurrentIndex(0)
        self.showBooks()
    
    def showBooks(self):
        self.list_books.setRowCount(0)

        books = self.dbManager.getBooks()
        count = 0
        for book in books:
            self.list_books.insertRow(count)
            self.list_books.setItem(count, 0 ,QTableWidgetItem(book.isbn))
            self.list_books.setItem(count, 1 ,QTableWidgetItem(book.name))
            self.list_books.setItem(count, 2 ,QTableWidgetItem(book.writer))
            self.list_books.setItem(count, 3 ,QTableWidgetItem(book.topic))
            self.list_books.setItem(count, 4 ,QTableWidgetItem(book.date))
            self.list_books.setItem(count, 5 ,QTableWidgetItem(book.page_count))
            self.list_books.setItem(count, 6 ,QTableWidgetItem(book.book_number))
            self.list_books.setItem(count, 7 ,QTableWidgetItem(book.publisher))
            count += 1  

    def searchBooks(self):
        self.list_books.setRowCount(0)

        category = self.searchCatCB.currentText()
        searchText = self.searchTextLE.text()
        books = self.dbManager.searchBooks(category, searchText)

        count = 0
        for book in books:
            self.list_books.insertRow(count)
            self.list_books.setItem(count, 0 ,QTableWidgetItem(book.isbn))
            self.list_books.setItem(count, 1 ,QTableWidgetItem(book.name))
            self.list_books.setItem(count, 2 ,QTableWidgetItem(book.writer))
            self.list_books.setItem(count, 3 ,QTableWidgetItem(book.topic))
            self.list_books.setItem(count, 4 ,QTableWidgetItem(book.date))
            self.list_books.setItem(count, 5 ,QTableWidgetItem(book.page_count))
            self.list_books.setItem(count, 6 ,QTableWidgetItem(book.book_number))
            self.list_books.setItem(count, 7 ,QTableWidgetItem(book.publisher))
            count += 1       
       
    def addBook(self):
        isbn = self.isbnLE.text()
        name = self.bookNameLE.text()
        writer = self.writerLE.text()
        topic = self.topicLE.text()
        date = self.dateLE.text()
        page_count = self.pageCountLE.text()
        publisher = self.publisherLE.text()
        bookNo = self.bookNoLE.text()

        self.dbManager.addBook(isbn, name, writer, topic, date, page_count, bookNo, publisher)


