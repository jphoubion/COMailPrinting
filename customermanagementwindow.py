from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from ui.customermanagementwindow import Ui_CustomerManagementWindow

class CustomerManagementWindow(QtWidgets.QMainWindow, Ui_CustomerManagementWindow):
    def __init__(self, conn, parent=None):
        super(CustomerManagementWindow, self).__init__(parent)
        self.setupUi(self)