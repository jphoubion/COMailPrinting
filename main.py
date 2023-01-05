import sys
import json
from functools import partial

# from pprint import pprint
# from openpyxl import Workbook
# from openpyxl.styles import PatternFill, Font, Color
# from openpyxl.utils import get_column_letter


from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon, QIconEngine

from PySide6.QtWidgets import QDialog, QFileDialog, QLabel, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, \
    QTextEdit

from ui.mainwindow import Ui_MainWindow
import comanagementwindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.actionQuitter.triggered.connect(self.quit)
        self.actionGestion.triggered.connect(self.openCOManagementWindow)

        self.COManagementWindow = comanagementwindow.COMainWindow()

        # Chargement du fichier JSON des C/O
        self.data = self.load_data()

        # Ajout de la 1ère ligne de la table
        self.btn_pressed()
        self.btnAddRow.clicked.connect(self.btn_pressed)

    def btn_pressed(self):
        self.tw_co.insertRow(self.tw_co.rowCount())

        te_coordonnees = QTextEdit()
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 1, te_coordonnees)

        combo_co = QComboBox()
        combo_co.addItems(self.data['co'])
        # combo_co.activated.connect(partial(self.get_co_details, combo_co.currentText()))
        combo_co.activated.connect(lambda x: te_coordonnees.setText(self.data['co'][combo_co.currentText()]['adresse']))
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 0, combo_co)

    def load_data(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        # print(data['co'])
        for d in data['co']:
            print(data['co'][d])
            # print(d['co']['adresse'])
        return data

    def get_co_details(self, co_name, idx):
        return self.data['co'][co_name]['adresse']
    def openCOManagementWindow(self):
        self.COManagementWindow.show()

    def quit(self):
        app.quit()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()