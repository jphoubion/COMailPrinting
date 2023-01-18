from functools import partial

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QPlainTextEdit, QLineEdit, QLabel, QMessageBox

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
        self.tw_companies.cellClicked.connect(self.fill_fields)

        self.company_id = ''

    def setupConnection(self):
        self.btn_add.clicked.connect(partial(self.addCompany, self.db_connection, self.le_name, self.le_form))
        self.btn_modify.clicked.connect(partial(self.modifyCompany, self.db_connection))
        self.btn_delete.clicked.connect(partial(self.deleteCompany, self.db_connection))
        self.btn_quit.clicked.connect(self.quit)

    def fillTable(self, conn):
        res_companies = sqlmanagement.get_result(conn, "SELECT * FROM companies")
        for company in res_companies:
            # Adding a row in the table
            self.tw_companies.insertRow(self.tw_companies.rowCount())
            self.addIdField(company[0])
            self.addCompanyNameField(company[1])
            self.addCompanyFormField(company[2])

            self.tw_companies.resizeColumnsToContents()
            self.tw_companies.resizeRowsToContents()

    def addIdField(self, id):
        te_id = QLabel()
        # te_id.setFixedWidth(0)
        te_id.setText(str(id))
        self.tw_companies.setCellWidget(self.tw_companies.rowCount() - 1, 0, te_id)
        self.tw_companies.hideColumn(0)
        # te_id.setFixedHeight(30)

    def addCompanyNameField(self, name):
        te_company_name = QLabel()
        te_company_name.setFixedWidth(200)
        te_company_name.setText(name)
        self.tw_companies.setCellWidget(self.tw_companies.rowCount() - 1, 1, te_company_name)
        te_company_name.setFixedHeight(30)

    def addCompanyFormField(self, form):
        te_company_form = QLabel()
        te_company_form.setFixedWidth(200)
        te_company_form.setText(form)
        self.tw_companies.setCellWidget(self.tw_companies.rowCount() - 1, 2, te_company_form)
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

    def modifyCompany(self, conn):
        name = self.le_name.text()
        form = self.le_form.text()
        req = f"UPDATE companies SET company_name = '{name}', company_type = '{form}' WHERE id = {self.company_id}"
        result = sqlmanagement.get_result(conn, req)
        conn.commit()

    def deleteCompany(self, conn):
        name = self.tw_companies.cellWidget(self.tw_companies.currentRow(),0)
        res_company = sqlmanagement.get_result(conn, \
            f"DELETE FROM companies WHERE company_name = '{name.text()}'")
        conn.commit()
        self.tw_companies.removeRow(self.tw_companies.currentRow())

    def fill_fields(self):
        self.company_id = self.tw_companies.cellWidget(self.tw_companies.currentRow(), 0).text()
        self.le_name.setText(self.tw_companies.cellWidget(self.tw_companies.currentRow(), 1).text())
        self.le_form.setText(self.tw_companies.cellWidget(self.tw_companies.currentRow(), 2).text())

    def quit(self):
        if self.tw_companies.rowCount() == 0:
            result = QMessageBox.question(self, "COMailPrinting - Gestion des sociétés émettrices", \
                                          "Aucune société émettrice n'a été crée.\n\nCeci implique qu'aucun nom"\
                                          " de société ne sera mentionné en signature des courriers !\n\n"\
                                          "Voulez-vous quitter cette fenêtre sans créer de société ?", \
                                          QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Cancel)
            if result == QMessageBox.StandardButton.Ok:
                self.parentWindow.btn_add_row()
                self.close()
        else:
            self.parentWindow.cbb_company.clear()
            self.parentWindow.load_companies(self.db_connection)
            self.parentWindow.cbb_company.setEnabled(True)
            self.parentWindow.btn_add_row()
            self.close()
