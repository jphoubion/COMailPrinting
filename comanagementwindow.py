from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from ui.comanagementwindow import Ui_CoManagementWindow


class CoManagementWindow(QtWidgets.QMainWindow, Ui_CoManagementWindow):

    def __init__(self, conn, parent=None):
        super(CoManagementWindow, self).__init__(parent)
        self.setupUi(self)