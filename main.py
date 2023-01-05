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

        # ComboBox des sociétés
        self.cbb_company.addItems(self.data['societes'])

        # Ajout de la 1ère ligne de la table
        self.btn_pressed()
        self.btnAddRow.clicked.connect(self.btn_pressed)

    def btn_pressed(self):
        self.tw_co.insertRow(self.tw_co.rowCount())

        te_coordonnees = QTextEdit()
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 1, te_coordonnees)

        combo_co = QComboBox()
        combo_co.addItems(self.data['co'])
        combo_co.currentTextChanged.connect(partial(self.get_co_details, te_coordonnees, combo_co.currentText()))
        # combo_co.activated.connect(lambda x: te_coordonnees.setText(self.data['co'][combo_co.currentText()]['adresse']))
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 0, combo_co)

        self.get_co_details(te_coordonnees, combo_co.currentText(), combo_co.currentText())

        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 4, QLabel(self.cbb_company.currentText()))

        self.tw_co.resizeColumnsToContents()

    def load_data(self):
        with open("data.json", "r") as f:
            data = json.load(f)
        # print(data['co'])
        print(data['societes'])
        for d in data['co']:
            print(data['co'][d])
            # print(d['co']['adresse'])
        return data

    def get_co_details(self, te_box, ol_co_name, new_co_name):
        # print(te_box, new_co_name)
        te_box.setText(self.data['co'][new_co_name]['adresse'])
    def openCOManagementWindow(self):
        self.COManagementWindow.show()

    def quit(self):
        app.quit()

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()