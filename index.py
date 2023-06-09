from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc

from PyQt5.uic import loadUiType

ui, base = loadUiType('UserWindow.ui')
print(ui)
print(base)

class UserWindow(base, ui):
    def __init__(self, ui):
        self.base = base()
        self.ui = ui
        self.ui.setupUi(self.base)

    def show(self):
        self.base.show()

def main():
    app = QApplication(sys.argv)
    widget = ui()
    window = base()
    widget.setupUi(window)
    window.show()

    uWindow = UserWindow(ui())
    uWindow.show()
    #window.base.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()