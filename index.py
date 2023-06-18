from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc

import Database.dao_book_manager as book_manager
import Database.models as models
import Database.dao_user_manager as user_manager

from PyQt5.uic import loadUiType

ui, base = loadUiType('UserWindow.ui')





class UserWindow(base, ui):
    def __init__(self):
        base.__init__(self)
        self.setupUi(self)
        self.buttonHandling()
        self.dbManager = book_manager.DBManager()
        self.showBooks()
        

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
            for i in range(1, 9):
                item = QTableWidgetItem(str(book[i]))
                self.list_books.setItem(count, i-1 ,item)

            count += 1         

    def searchBooks(self):
        self.list_books.setRowCount(0)
        #QComboBox.text
        #QLineEdit.text
        category = self.searchCatCB.currentText()
        searchText = self.searchTextLE.text()
        books = self.dbManager.searchBooks(category, searchText)
        count = 0
        for book in books:
            self.list_books.insertRow(count)
            for i in range(1, 9):
                item = QTableWidgetItem(str(book[i]))
                self.list_books.setItem(count, i-1 ,item)

            count += 1         
       

    def openBooksTab(self):
        self.tabWidget.setCurrentIndex(0)
        self.showBooks()

    def openUserTab(self):
        pass

    def openSettingsTab(self):
        pass




    

def main():
    app = QApplication(sys.argv)
    uWindow = UserWindow()
    uWindow.show()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()