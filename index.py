from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from enum import Enum

from login_window import LoginWindow
from user_window import UserWindow
from officer_window import OfficerWindow

class States(Enum):
    logged_out = 1
    logged_as_user = 2
    logged_as_officer = 3
    login = 4
    sign_up = 5

class MainApp:
    def __init__(self):
        self.login = LoginWindow()
        self.userWindow = UserWindow()
        self.officerWindow = OfficerWindow()

        self.login.setStateChangeFunc(self.changeState(States.logged_as_officer), self.changeState(States.logged_as_user))
        self.userWindow.setStateChangeFunc(self.changeState(States.login))
        #self.officerWindow.setStateChangeFunc()

        self.changeState(States.logged_as_user)


    def changeState(self, new_state):
        self.state = new_state

        if self.state == States.logged_as_user:
            self.userWindow.show()
            self.officerWindow.hide()
            self.login.hide()

        elif self.state == States.logged_as_officer:
            self.userWindow.hide()
            self.officerWindow.show()
            self.login.hide()

        elif self.state == States.login:
            self.userWindow.hide()
            self.officerWindow.hide()
            self.login.show()

        
    

def main():
    app = QApplication(sys.argv)
    mainApp = MainApp()
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()