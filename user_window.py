from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc
from enum import Enum

import Database.dao_book_manager as book_manager
import Database.models as models

from error_box import ErrorWindow

from PyQt5.uic import loadUiType

user_ui, base = loadUiType('UserWindow.ui')

class UserWindow(base, user_ui):
    def __init__(self):
        base.__init__(self)
        self.setupUi(self)
        self.buttonHandling()
        self.dbManager = book_manager.BookDBManager()
        self.showBooks()
    
    def setStateChangeFunc(self, showLoginFunc):
        self.showLoginPage = showLoginFunc

    def setUser(self, user):
        self.user = user
        
    def buttonHandling(self):
        self.booksTabBtn.clicked.connect(self.openBooksTab)
        self.userTabBtn.clicked.connect(self.openUserTab)
        self.searchBtn.clicked.connect(self.searchBooks)

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
       

    def openBooksTab(self):
        self.tabWidget.setCurrentIndex(0)
        self.showBooks()

    def openUserTab(self):
        self.showLoginPage()

    def openSettingsTab(self):
        pass

