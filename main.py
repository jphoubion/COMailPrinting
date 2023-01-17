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
from datetime import datetime

import sqlmanagement

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

        #################################################"
        # SETUP CONNECTION BETWEEN MENU/BUTTON TO FUNCTION
        #################################################"
        self.setup_connection()

        ##########################
        # Test if DB contents data
        ##########################
        if sqlmanagement.data_exists(self.cursor) is None:
            QMessageBox.critical(self, "COMailPrinting - Erreur",\
                                  "Aucune donnée actuellement dans la DB.\n"
                                  "Veuillez importer des données et remplir" \
                                  " la table des sociétés !", \
                                   QMessageBox.StandardButton.Ok)
            # Creates empty tables in the DB
            res = sqlmanagement.drop_create_tables(self.db_connection, self.cursor)
            if res is None:
                # Empty the COMPANIES combobox and disables it
                self.cbb_company.clear()
                self.cbb_company.setEnabled(False)
                # Empty the main table
                self.empty_table()
        else:
            ################################
            # Add the first row of the table
            ################################
            self.btn_add_row()

            ################################
            # Load companies list
            ################################
            self.load_companies(self.db_connection)

    def load_companies(self, conn):
        req_companies = sqlmanagement.get_result(conn, "SELECT * FROM companies")
        if len(req_companies) > 0:
            for company in req_companies:
                self.cbb_company.addItem(company[1])
            self.cbb_company.setEnabled(True)

    def setup_connection(self):
        # Connect methods to menu options
        ##################################
        self.actionQuitter.triggered.connect(self.quit)
        self.actionCompanyManagement.triggered.connect(self.open_company_management_window)
        self.actionImport_customers.triggered.connect(partial(self.import_data, self.db_connection, self.cursor))
        self.actionDropTables.triggered.connect(partial(self.drop_create_tables, self.db_connection, self.cursor))

        # Connect BUTTONS to methods
        #############################
        self.btnAddRow.clicked.connect(self.btn_add_row)
        self.btnDeleteRow.clicked.connect(self.btn_delete_row)
        self.btnEmptyTable.clicked.connect(self.empty_table)
        self.btnPrint.clicked.connect(self.btn_print)

    def import_data(self, conn, cursor):
        import_from_xls = ImportFromXls()
        import_from_xls.import_customers(conn, cursor)

        # Open companies managmement window if combobox is empty
        if self.cbb_company.count() == 0:
            self.open_company_management_window()
        # # Add a row it the table is empty
        # if self.tw_co.rowCount() == 0:
        #     self.btn_add_row()

    def drop_create_tables(self, conn, cursor):
        result = QMessageBox.critical(self, "COMailPrinting - Vidange de la base de données",
                                            "Etes-vous certain de vouloir  vider la base donnée ?\n\n" \
                                            "Il faudra réimporter les clients depuis un fichier XLSX" \
                                            " et recéer réencoder les sociétés émettrices.", \
                                            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if result == QMessageBox.StandardButton.Ok:
            res = sqlmanagement.drop_create_tables(conn, cursor)
            if res is None:
                # Empty the COMPANIES combobox and disables it
                self.cbb_company.clear()
                self.cbb_company.setEnabled(False)
                # Empty the main table
                self.empty_table()
                QMessageBox.information(self, "COMailPrinting - Vidange de la base de données",
                                            "Base de données éffacée !",\
                                            QMessageBox.StandardButton.Ok)

    def empty_table(self):
        self.tw_co.selectRow(0)
        for row in range(0, self.tw_co.rowCount()):
            self.tw_co.removeRow(self.tw_co.currentRow())

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
        # Add combobox for C/O on each new line
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
        # Add combobox for CUSTOMERS on each new line
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

    def btn_delete_row(self):
        self.tw_co.removeRow(self.tw_co.currentRow())

    def btn_print(self):
        p = Printing()
        now = datetime.now()
        PDF_name = f"COMailPrinting - {now.strftime('%d-%m-%Y')}.pdf"
        p.PDFFile = Canvas(PDF_name, pagesize=A4)
        p.PDFFile.setFont("Helvetica", 10)
        ok_for_print = False
        for row in range(0, self.tw_co.rowCount()):
            if self.tw_co.cellWidget(row,0).currentText() != ' ':
                req_customer = f"SELECT customer_name FROM customers WHERE customer_code='{self.tw_co.cellWidget(row,0).currentText()}'"
                client = sqlmanagement.get_result(self.db_connection,req_customer)[0][0]
                co = f"{self.tw_co.cellWidget(row,1).currentText()}\n{self.tw_co.cellWidget(row,2).toPlainText()}"
                reference = self.tw_co.cellWidget(row,5).text()
                company = self.tw_co.cellWidget(row,6).currentText()
                req_company = f"SELECT company_type FROM companies WHERE company_name = '{company}'"
                company_type = sqlmanagement.get_result(self.db_connection,req_company)[0][0]
                # PDFFile_name = self.tw_co.cellWidget(row,0).currentText()
                p.create_pages(co, client, reference, company, company_type)
                ok_for_print = True
            else:
                ok_for_print = False
        if ok_for_print:
            p.PDFFile.save() # Save the file on the disk
            QMessageBox.information(self, "COMailPrinting - Export PDF", f"Export du fichier {PDF_name} terminé !")
        else:
            QMessageBox.warning(self, "COMailPrinting - Export PDF", "Il y a des erreurs dans la table, impossible d'exporter en PDF"\
                              "\n\nVérifiez s'il n'y a pas de zone 'Client' ou 'C/O' vide...", QMessageBox.StandardButton.Ok)

    def open_company_management_window(self):
        company_management_window = CompanyManagementWindow(self.db_connection, self)
        company_management_window.show()

    def select_co_from_customer(self, combo_co, old_customer, customer):
        if customer != " ":
            co_id_from_customer = sqlmanagement.get_result(self.db_connection, f"SELECT co_id FROM customers WHERE customer_code = '{customer}'")
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