import sys
# from pprint import pprint
# from openpyxl import Workbook
# from openpyxl.styles import PatternFill, Font, Color
# from openpyxl.utils import get_column_letter


from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QDialog, QFileDialog, QLabel, QMessageBox

from ui.mainwindow import Ui_MainWindow
import comanagementwindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.actionQuitter.triggered.connect(self.quit)
        self.actionGestion.triggered.connect(self.openCOManagementWindow)

        self.COManagementWindow = comanagementwindow.COMainWindow()


    def openCOManagementWindow(self):
        self.COManagementWindow.show()

    def quit(self):
        app.quit()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()