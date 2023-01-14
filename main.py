import os
import sys
if sys.platform == "windows":
    sys.argv += ['-platform', 'windows:darkmode=2']

from functools import partial

from PySide6 import QtWidgets, QtCore

from PySide6.QtWidgets import QDialog, QFileDialog, QLabel, QMessageBox, QComboBox, QPushButton, QTableWidgetItem, \
    QTextEdit, QCompleter, QPlainTextEdit, QLineEdit

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import sqlite3

import sqlmanagement
import msgbox

from importfromxls import ImportFromXls

from ui.mainwindow import Ui_MainWindow
from ui.companymanagementwindow import Ui_CompanyManagementWindow

from companymanagementwindow import CompanyManagementWindow

from printing import Printing


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        #################################################"
        # STARTS SQL CONNECTION
        #################################################"
        self.db_connection, self.cursor = sqlmanagement.setup_connection("db.sqlite3")

        self.setup_connection()

        ##########################
        # Test if DB contents data
        ##########################
        if sqlmanagement.data_exists(self.cursor) is None:
            msgbox.display_msgbox("COMailPrinting - Erreur", QMessageBox.Critical, \
                                  "Aucune donnée actuellement dans la DB.\n"
                                  "Veuillez importer des données et remplir" \
                                  " la table des sociétés !", \
                                   QMessageBox.StandardButton.Ok)
        else:
            ################################
            # Add the first row of the table
            ################################
            self.btn_add_row()
            self.btnAddRow.clicked.connect(self.btn_add_row)
            self.btnPrint.clicked.connect(self.btn_print)

            ################################
            # Load companies list
            ################################
            self.load_companies(self.db_connection)

    def load_companies(self, conn):
        req_companies = sqlmanagement.get_result(conn, "SELECT * FROM companies")
        if len(req_companies) > 0:
            for company in req_companies:
                self.cbb_company.addItem(company[1])

    def setup_connection(self):
        # Connect methods to menu options
        ##################################
        self.actionQuitter.triggered.connect(self.quit)
        # self.actionGestion.triggered.connect(self.openCOManagementWindow)
        self.actionCompanyManagement.triggered.connect(self.openCompanyManagementWindow)

        self.import_from_xls = ImportFromXls()
        self.actionImport_customers.triggered.connect(partial(self.import_from_xls.import_customers, self.db_connection, self.cursor))
        self.actionDropTables.triggered.connect(partial(sqlmanagement.drop_create_tables, self.db_connection, self.cursor))

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
        combo_co.setFixedWidth(200)

        co_list = [' ']
        req_result = sqlmanagement.get_result(self.db_connection, "SELECT * FROM co")
        for co_name in req_result:
            co_list.append(co_name[1])
        combo_co.addItems(co_list)
        combo_co.currentTextChanged.connect(partial(self.get_co_details, te_coordonnees, combo_co.currentText()))

        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 1, combo_co)
        # print(f"NB de CO = {combo_co.count()}")

        ###################################################################################
        # Add combobox for CUSTOMERS on each new line and fill it with customers from JSON
        ###################################################################################
        combo_cust = QComboBox()
        combo_cust.setEditable(True)
        combo_cust.setFixedWidth(200)

        customer_list = [' ']
        req_result = sqlmanagement.get_result(self.db_connection, "SELECT * FROM customers")
        for cust in req_result:
            customer_list.append(cust[1])
        combo_cust.addItems(customer_list)

        combo_cust.currentTextChanged.connect(partial(self.select_co_from_customer, combo_co, combo_cust.currentText()))

        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 0, combo_cust)
        # print(f"NB de CUST = {combo_cust.count()}")
        ###################################################################################
        # Add button to update data about C/O
        ###################################################################################
        btn_update_co = QPushButton("MAJ")
        btn_update_co.clicked.connect(self.update_co)
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 3, btn_update_co)


        ###################################################################################
        # Add button to update data about customer
        ###################################################################################
        btn_update_customer = QPushButton("MAJ")
        btn_update_customer.clicked.connect(self.update_customer)
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 4, btn_update_customer)

        ###################################################################################
        # Add a TextEdit box to set the reference
        ###################################################################################
        te_reference = QLineEdit()
        te_reference.setFixedWidth(150)
        te_reference.setFixedHeight(40)
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 5, te_reference)

        ###################################################################################
        # Add combobox for company on each new line and fill it with companies from JSON and
        # display the current default company
        ###################################################################################
        combo_company = QComboBox()
        req_companies = sqlmanagement.get_result(self.db_connection, "SELECT * FROM companies")
        for company in req_companies:
            combo_company.addItem(company[1])
        combo_company.setCurrentText(self.cbb_company.currentText())
        self.tw_co.setCellWidget(self.tw_co.rowCount()-1, 6, combo_company)

        self.tw_co.resizeColumnsToContents()
        self.tw_co.resizeRowsToContents()
        # self.tw_co.setColumnWidth(3, 290)

    def btn_print(self):
        p = Printing()
        p.PDFFile = Canvas("COMailPrinting.pdf", pagesize=A4)
        p.PDFFile.setFont("Helvetica", 10)
        for row in range(0,self.tw_co.rowCount()):
            # print(self.tw_co.cellWidget(row,0).currentText())
            req_customer = f"SELECT customer_name FROM customers WHERE customer_code='{self.tw_co.cellWidget(row,0).currentText()}'"
            client = sqlmanagement.get_result(self.db_connection,req_customer)[0][0]
            co = f"{self.tw_co.cellWidget(row,1).currentText()}\n{self.tw_co.cellWidget(row,2).toPlainText()}"
            reference = self.tw_co.cellWidget(row,5).text()
            company = self.tw_co.cellWidget(row,6).currentText()
            PDFFile_name = self.tw_co.cellWidget(row,0).currentText()
            p.create_pages(co, client, reference, company)
        p.PDFFile.save() # Save the file on the disk
        QMessageBox.information(self, "Export PDF", "Export du fichier COMailPrinting.pdf terminé !")

    def openCompanyManagementWindow(self):
        company_management_window = CompanyManagementWindow(self.db_connection, self)
        company_management_window.show()

    def select_co_from_customer(self, combo_co, old_customer, customer):
        co_id_from_customer = sqlmanagement.get_result(self.db_connection, f"SELECT co_id FROM customers WHERE customer_code = '{customer}'")

        if customer != " ":
            co_name = sqlmanagement.get_result(self.db_connection, f"SELECT co_name FROM co WHERE id = {co_id_from_customer[0][0]}")

            combo_co.setCurrentText(co_name[0][0])
        else:
            combo_co.setCurrentIndex(0)

    def get_co_details(self, te_box, old_co_name, new_co_name):
        if new_co_name != " ":
            address = sqlmanagement.get_result(self.db_connection,f"SELECT co_address FROM co WHERE co_name = '{new_co_name}'")
            te_box.setPlainText(address[0][0])
        else:
            te_box.setText('')

    def update_co(self):
        print("update co")

    def update_customer(self):
        print("update customer")

    def quit(self):
        app.quit()


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

window = MainWindow()
window.show()
app.exec()