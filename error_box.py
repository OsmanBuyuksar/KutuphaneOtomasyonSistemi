from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import time

from PyQt5.uic import loadUiType

ui, base = loadUiType('ErrorWindow.ui')

class ErrorWindow(base, ui):
    def __init__(self,):
        base.__init__(self)
        self.setupUi(self)

    def showError(self, errorString):
        self.label.setText(errorString)
        self.show()