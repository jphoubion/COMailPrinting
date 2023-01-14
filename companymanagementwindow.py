from functools import partial

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit, QLineEdit, QLabel

from ui.companymanagementwindow import Ui_CompanyManagementWindow

import sqlmanagement

class CompanyManagementWindow(QtWidgets.QMainWindow, Ui_CompanyManagementWindow):

    def __init__(self, conn, parent=None):
        super(CompanyManagementWindow, self).__init__(parent)
        self.setupUi(self)
        self.db_connection = conn
        self.parentWindow = parent
        self.setupConnection()

        self.fillTable(self.db_connection)

    def setupConnection(self):
        self.btn_add.clicked.connect(partial(self.addCompany, self.db_connection, self.le_name, self.le_form))
        self.btn_delete.clicked.connect(partial(self.deleteCompany, self.db_connection))
        self.btn_quit.clicked.connect(self.quit)

    def fillTable(self, conn):
        res_companies = sqlmanagement.get_result(conn, "SELECT * FROM companies")
        for company in res_companies:
            # Adding a row in the table
            self.tw_companies.insertRow(self.tw_companies.rowCount())
            self.addCompanyNameField(company[1])
            self.addCompanyFormField(company[2])
            self.tw_companies.resizeColumnsToContents()
            self.tw_companies.resizeRowsToContents()

    def addCompanyNameField(self, name):
        te_company_name = QLabel()
        te_company_name.setFixedWidth(200)
        te_company_name.setText(name)
        self.tw_companies.setCellWidget(self.tw_companies.rowCount() - 1, 0, te_company_name)
        te_company_name.setFixedHeight(30)

    def addCompanyFormField(self, form):
        te_company_form = QLabel()
        te_company_form.setFixedWidth(200)
        te_company_form.setText(form)
        self.tw_companies.setCellWidget(self.tw_companies.rowCount() - 1, 1, te_company_form)
        te_company_form.setFixedHeight(30)
    def addCompany(self, conn, name, form):
        res_company = sqlmanagement.get_result(conn, \
                    f"INSERT INTO companies (company_name, company_type) VALUES ('{name.text()}','{form.text()}')")
        conn.commit()

        # Adding a row in the table
        self.tw_companies.insertRow(self.tw_companies.rowCount())
        self.addCompanyNameField(name.text())
        self.addCompanyFormField(form.text())

        self.le_name.clear()
        self.le_form.clear()

    def deleteCompany(self, conn):
        name = self.tw_companies.cellWidget(self.tw_companies.currentRow(),0)
        res_company = sqlmanagement.get_result(conn, \
            f"DELETE FROM companies WHERE company_name = '{name.text()}'")
        conn.commit()
        self.tw_companies.removeRow(self.tw_companies.currentRow())

    def quit(self):
        self.parentWindow.cbb_company.clear()
        self.parentWindow.load_companies(self.db_connection)
        self.close()