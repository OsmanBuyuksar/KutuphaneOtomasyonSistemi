from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc

from PyQt5.uic import loadUiType

ui, base = loadUiType('UserWindow.ui')

class UserWindow(base, ui):
    def __init__(self):
        base.__init__(self)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    uWindow = UserWindow()
    uWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()