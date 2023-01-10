import sys
sys.argv += ['-platform', 'windows:darkmode=2']
import json
from functools import partial

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon, QIconEngine

from PySide6.QtWidgets import QDialog, QFileDialog, QLabel, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, \
    QTextEdit, QCompleter

from  importfromxls import ImportFromXls

from ui.mainwindow import Ui_MainWindow
import comanagementwindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.import_from_xls = ImportFromXls()
        self.actionQuitter.triggered.connect(self.quit)
        self.actionGestion.triggered.connect(self.openCOManagementWindow)
        self.actionImport_customers.triggered.connect(self.import_from_xls.import_customers)

        self.COManagementWindow = comanagementwindow.COMainWindow()

        self.company_data = self.load_company_data()

        # Chargement du fichier JSON des C/O
        self.co_data = self.load_co_data()

        # Loading customer from JSON
        self.customers_data = self.load_customers_data()

        # ComboBox des sociétés
        self.cbb_company.addItems(self.company_data['companies'])

        # Ajout de la 1ère ligne de la table
        self.btn_pressed()
        self.btnAddRow.clicked.connect(self.btn_pressed)
        #
        # self.tw_co.setColumnWidth(3, 290)
        # print(self.tw_co.columnWidth(3))

    def btn_pressed(self):
        # Adding a row in the table
        self.tw_co.insertRow(self.tw_co.rowCount())

        ###################################################################################
        # Add combobox for CUSTOMERS on each new line and fill it with customers from JSON
        ###################################################################################
        combo_cust = QComboBox()
        combo_cust.setEditable(True)
        combo_cust.setFixedWidth(100)

        customer_list = []
        for cust in self.customers_data:
            customer_list.append(cust)
        combo_cust.addItems(customer_list)

        combo_cust.currentIndexChanged.connect(self.select_co_from_customer)

        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 0, combo_cust)

        ###################################################################################
        # Add field to display C/O info
        ###################################################################################
        te_coordonnees = QTextEdit()
        te_coordonnees.setFixedWidth(200)
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 2, te_coordonnees)
        te_coordonnees.setFixedHeight(50)

        ###################################################################################
        # Add combobox for C/O on each new line and fill it with customers from JSON
        ###################################################################################
        combo_co = QComboBox()
        combo_co.setEditable(True)
        combo_co.setFixedWidth(150)

        co_list = []
        for co_name in self.co_data:
            co_list.append(self.co_data[co_name]['co_name'])
        combo_co.addItems(co_list)
        combo_co.currentTextChanged.connect(partial(self.get_co_details, te_coordonnees, combo_co.currentText()))

        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 1, combo_co)

        ###################################################################################
        # Add button to update data about C/O in JSON file
        ###################################################################################
        btn_update_co = QPushButton("MAJ")
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 5, btn_update_co)
        # Add a combobox on the 1st column and fill it with all C/O from JSON

        # Fill the QTextEdit in with current selected CO address
        # self.get_co_details(te_coordonnees, combo_co.currentText(), combo_co.currentText())

        ###################################################################################
        # Add combobox for company on each new line and fill it with companies from JSON and
        # display the current default company
        ###################################################################################
        combo_company = QComboBox()
        combo_company.addItems(self.company_data["companies"])
        combo_company.setCurrentText(self.cbb_company.currentText())
        # print(combo_company.itemText(0))
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 4, combo_company)

        self.tw_co.resizeColumnsToContents()
        self.tw_co.resizeRowsToContents()
        # self.tw_co.setColumnWidth(3, 290)

    def load_company_data(self):
        with open("companies.json", "r") as f:
            data = json.load(f)
        return data

    def load_co_data(self):
        with open("co.json", "r") as f:
            data = json.load(f)
        # print(data['co'])
        # print(data['companies'])
        # for d in data['co']:
        #     print(data['co'][d])
        # print(d['co']['address'])
        return data

    def load_customers_data(self):
        with open("customers.json","r") as f:
            data = json.load(f)
        return data

    def select_co_from_customer(self):
        print('select co from customer')

    def get_co_details(self, te_box, old_co_name, new_co_name):
        # print(te_box, new_co_name)
        print(new_co_name)
        address = f"{self.co_data[new_co_name]['address']}\n{self.co_data[new_co_name]['cp']} {self.co_data[new_co_name]['city']}".upper()
        te_box.setText(address)


    def openCOManagementWindow(self):
        self.COManagementWindow.show()

    def quit(self):
        app.quit()

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

window = MainWindow()
window.show()
app.exec()