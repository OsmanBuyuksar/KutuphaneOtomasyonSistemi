from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc

import db_manager

from PyQt5.uic import loadUiType

ui, base = loadUiType('UserWindow.ui')





class UserWindow(base, ui):
    def __init__(self):
        base.__init__(self)
        self.setupUi(self)
        self.buttonHandling()
        self.dbManager = db_manager.DBManager()
        self.showBooks()
        

    def buttonHandling(self):
        self.booksTabBtn.clicked.connect(self.openBooksTab)
        self.userTabBtn.clicked.connect(self.openUserTab)

    def showBooks(self):
        self.list_books.setRowCount(0)
        books = self.dbManager.getBooks()
        count = 0
        dic = {0: 'isbn', 1: 'isim',2: 'yazar',3: 'tür',4: 'yayım tarihi',5: 'sayfa sayısı',6: 'yayıncı',7: 'kitap numarası'}
        for book in books:
            self.list_books.insertRow(count)
            for i in range(1, 9):
                item = QTableWidgetItem(str(book[i]))
                self.list_books.setItem(count, i-1 ,item)
                
            
            count += 1         
            

    def openBooksTab(self):
        self.tabWidget.setCurrentIndex(0)

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