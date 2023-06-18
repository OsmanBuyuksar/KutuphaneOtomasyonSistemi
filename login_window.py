from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

import Database.dao_user_manager as user_manager

from error_box import ErrorWindow

from PyQt5.uic import loadUiType

login_ui, base = loadUiType('LoginWindow.ui')

class LoginWindow(base, login_ui):
    def __init__(self):
        base.__init__(self)
        self.setupUi(self)

        self.dbManager = user_manager.UserDBManager()
        self.buttonHandling()
        self.errorWindow = ErrorWindow()

    def setStateChangeFunc(self, loginOfficerFunc, loginUserFunc):
        self.loginOfficerF = loginOfficerFunc
        self.loginUserF = loginUserFunc

    def buttonHandling(self):
        self.loginBtn.clicked.connect(self.login)

    def login(self):
        name = self.nameLE.text()
        password = self.psswdLE.text()
        user = self.dbManager.login(name, password)
        if user:
            if user.isOfficer():
                self.loginOfficerF()
            else:
                self.loginUserF()
        else:
            self.errorWindow.showError('Şifre veya kullanıcı ismi hatalı')