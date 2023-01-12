import sys
if sys.platform == "windows":
    sys.argv += ['-platform', 'windows:darkmode=2']


import json
from functools import partial

from PySide6 import QtWidgets, QtCore

from PySide6.QtWidgets import QDialog, QFileDialog, QLabel, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, \
    QTextEdit, QCompleter, QPlainTextEdit

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

from  importfromxls import ImportFromXls

from ui.mainwindow import Ui_MainWindow
import comanagementwindow
from printing import Printing

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.import_from_xls = ImportFromXls()
        self.actionQuitter.triggered.connect(self.quit)
        self.actionGestion.triggered.connect(self.openCOManagementWindow)
        self.actionImport_customers.triggered.connect(partial(self.import_from_xls.import_customers, "w"))
        self.actionAddImportCustomers.triggered.connect(partial(self.import_from_xls.import_customers, "a"))

        self.COManagementWindow = comanagementwindow.COMainWindow()

        self.data_to_print = 'test data'

        self.company_data = self.load_company_data()

        # Chargement du fichier JSON des C/O
        self.co_data = self.load_co_data()

        # Loading customer from JSON
        self.customers_data = self.load_customers_data()

        # ComboBox des sociétés
        self.cbb_company.addItems(self.company_data['companies'])

        # Ajout de la 1ère ligne de la table
        self.btn_add_row()
        self.btnAddRow.clicked.connect(self.btn_add_row)

        self.btnPrint.clicked.connect(self.btn_print)

    def btn_add_row(self):
        # Adding a row in the table
        self.tw_co.insertRow(self.tw_co.rowCount())

        ###################################################################################
        # Add field to display C/O info
        ###################################################################################
        te_coordonnees = QPlainTextEdit()
        te_coordonnees.setFixedWidth(200)
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 2, te_coordonnees)
        te_coordonnees.setFixedHeight(40)

        ###################################################################################
        # Add combobox for C/O on each new line  from JSON
        ###################################################################################
        combo_co = QComboBox()
        combo_co.setEditable(True)
        combo_co.setFixedWidth(150)

        co_list = [' ']
        for co_name in self.co_data:
            co_list.append(self.co_data[co_name]['co_name'])
        combo_co.addItems(co_list)
        combo_co.currentTextChanged.connect(partial(self.get_co_details, te_coordonnees, combo_co.currentText()))

        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 1, combo_co)

        ###################################################################################
        # Add combobox for CUSTOMERS on each new line and fill it with customers from JSON
        ###################################################################################
        combo_cust = QComboBox()
        combo_cust.setEditable(True)
        combo_cust.setFixedWidth(150)

        customer_list = [' ']
        for cust in self.customers_data:
            customer_list.append(cust)
        combo_cust.addItems(customer_list)

        combo_cust.currentTextChanged.connect(partial(self.select_co_from_customer, combo_co, combo_cust.currentText()))

        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 0, combo_cust)

        ###################################################################################
        # Add button to update data about C/O in JSON file
        ###################################################################################
        btn_update_co = QPushButton("MAJ")
        btn_update_co.clicked.connect(self.update_co)
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 3, btn_update_co)


        ###################################################################################
        # Add button to update data about C/O in JSON file
        ###################################################################################
        btn_update_customer = QPushButton("MAJ")
        btn_update_customer.clicked.connect(self.update_customer)
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 4, btn_update_customer)

        ###################################################################################
        # Add a TextEdit box to set the reference
        ###################################################################################
        te_reference = QTextEdit()
        te_reference.setFixedWidth(150)
        te_reference.setFixedHeight(40)
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 5, te_reference)

        ###################################################################################
        # Add combobox for company on each new line and fill it with companies from JSON and
        # display the current default company
        ###################################################################################
        combo_company = QComboBox()
        combo_company.addItems(self.company_data["companies"])
        combo_company.setCurrentText(self.cbb_company.currentText())
        # print(combo_company.itemText(0))
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 6, combo_company)

        self.tw_co.resizeColumnsToContents()
        self.tw_co.resizeRowsToContents()
        # self.tw_co.setColumnWidth(3, 290)

    def btn_print(self):
        p = Printing()
        p.PDFFile = Canvas("COMailPrinting.pdf", pagesize=A4)
        p.PDFFile.setFont("Helvetica", 10)
        for row in range(0,self.tw_co.rowCount()):
            client = self.customers_data[self.tw_co.cellWidget(row,0).currentText()]['name']
            co = f"{self.tw_co.cellWidget(row,1).currentText()}\n{self.tw_co.cellWidget(row,2).toPlainText()}"
            reference = self.tw_co.cellWidget(row,5).toPlainText()
            company = self.tw_co.cellWidget(row,6).currentText()
            PDFFile_name = self.tw_co.cellWidget(row,0).currentText()
            p.create_pages(co, client, reference, company)
        p.PDFFile.save() # Save the file on the disk
        QMessageBox.information(self, "Export PDF", "Export du fichier COMailPrinting.pdf terminé !")

    def load_company_data(self):
        with open("companies.json", "r") as f:
            data = json.load(f)
        return data

    def load_co_data(self):
        with open("co.json", "r") as f:
            data = json.load(f)
        return data

    def load_customers_data(self):
        with open("customers.json","r") as f:
            data = json.load(f)
        return data

    def select_co_from_customer(self, combo_co, old_customer, customer):
        if customer != " ":
            co = self.customers_data[customer]['co']
            co_name = self.co_data[co]['co_name']

            combo_co.setCurrentText(co_name)
        else:
            combo_co.setCurrentIndex(0)

    def get_co_details(self, te_box, old_co_name, new_co_name):
        if new_co_name != " ":
            print(new_co_name)
            address = f"{self.co_data[new_co_name]['address']}\n{self.co_data[new_co_name]['cp']} {self.co_data[new_co_name]['city']}".upper()
            te_box.setPlainText(address)
        else:
            te_box.setText('')

    def update_co(self):
        print("update co")

    def update_customer(self):
        print("update customer")

    def openCOManagementWindow(self):
        self.COManagementWindow.show()

    def quit(self):
        app.quit()

app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

window = MainWindow()
window.show()
app.exec()