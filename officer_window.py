from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import icons_rc
from enum import Enum


from login_window import LoginWindow
from user_window import UserWindow

import Database.dao_book_manager as book_manager
import Database.models as models
import Database.dao_user_manager as user_manager

from error_box import ErrorWindow

from PyQt5.uic import loadUiType



officer_ui, base = loadUiType('OfficerWindow.ui')

class OfficerWindow(base, officer_ui):
    x = 1