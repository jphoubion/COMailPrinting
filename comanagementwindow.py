import sys

from PySide6 import QtWidgets, QtCore
from ui.comanagementwindow import Ui_COManagementWindow

class COMainWindow(QtWidgets.QMainWindow, Ui_COManagementWindow):
    def __init__(self):
        super(COMainWindow, self).__init__()
        self.setupUi(self)


# app = QtWidgets.QApplication(sys.argv)
#
# window = COMainWindow()
# window.show()
# app.exec()