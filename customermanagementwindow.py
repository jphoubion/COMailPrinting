from functools import partial

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlTableModel, QSqlDatabase, QSqlRelationalTableModel, QSqlRelation, QSqlRelationalDelegate, \
    QSqlQuery
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication, QMessageBox, QTableView, QDialog

import sqlmanagement
from ui.customermanagementwindow import Ui_CustomerManagementWindow

class CustomerManagementWindow(QtWidgets.QMainWindow, Ui_CustomerManagementWindow):
    def __init__(self, conn, parent=None):
        super(CustomerManagementWindow, self).__init__(parent)
        self.setupUi(self)

        self.db_connection = conn
        self.parentWindow = parent

        self.setupConnection()

        self.coId = 0

        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("db.sqlite3")
        if not con.open():
            QMessageBox.critical(
                None,
                "COMailPrinting - Erreur !",
                "Erreur DB : %s" % con.lastError().databaseText(),
            )
        else:
            # Populates the table with CUSTOMERS
            self.model = QSqlRelationalTableModel(self)
            self.model.setTable("customers")
            self.tv_customers.setAlternatingRowColors(True)
            self.model.setRelation(3, QSqlRelation("co", "id", "co_name"))
            self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model.setHeaderData(0, Qt.Horizontal, "id")
            self.model.setHeaderData(1, Qt.Horizontal, "Code client")
            self.model.setHeaderData(2, Qt.Horizontal, "Nom")
            self.model.setHeaderData(3, Qt.Horizontal, "C/O")
            self.model.select()
            self.tv_customers.setModel(self.model)
            self.tv_customers.setSortingEnabled(True)
            self.tv_customers.hideColumn(0)
            self.tv_customers.sortByColumn(1, QtCore.Qt.AscendingOrder)
            self.tv_customers.setItemDelegate(QSqlRelationalDelegate())
            self.tv_customers.resizeColumnsToContents()

            # Populates the combobox with C/O
            self.co_model = QSqlTableModel(self)
            self.co_model.setTable('co')
            self.co_model.setSort(1, QtCore.Qt.AscendingOrder)
            column = self.co_model.fieldIndex("co_name")  # gives the index of the "co_name" field in the table
            self.co_model.select()
            self.cbb_co.setModel(self.co_model)
            self.cbb_co.setModelColumn(column)  # set the table column to display in the combobox
            self.cbb_co.currentTextChanged.connect(partial(self.get_coId, self.cbb_co.model(), self.cbb_co.currentText()))




    def setupConnection(self):
        # self.btn_new.clicked.connect(self.newCustomer)
        self.btn_add.clicked.connect(self.addCustomer)
        self.btn_delete.clicked.connect(self.deleteCustomer)
        self.btn_quit.clicked.connect(self.quit)


    def addCustomer(self):
        req = f"""INSERT INTO customers (customer_code, customer_name, co_id) 
                    VALUES ('{self.le_code.text()}','{self.le_name.text()}',{self.coId})"""
        print(req)
        query = QSqlQuery()
        if query.exec(req):
            QMessageBox.information(self, "COMailPrinting - Ajout d'un client", "Client ajouté avec succès !",
                                    QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self, "COMailPrinting - Ajout d'un client",
                                f"Erreur lors de l'ajout !\n\nErreur retournée :\n{query.lastError().databaseText()}")

        self.tv_customers.setModel(self.model)
        self.le_name.setText('')
        self.le_code.setText('')


    def deleteCustomer(self):
        dialog = QMessageBox.question(self,"COMailPrinting - Confirmation de suppression",
                                      "Confirmez-vous la suppression de cet ligne ?",
                                      QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)

        if dialog == QMessageBox.StandardButton.Ok:
            model = self.model
            indices = self.tv_customers.selectionModel().selectedRows()
            for index in sorted(indices):
                model.removeRow(index.row())

            self.tv_customers.setModel(self.model)

    def get_coId(self, pModel, pIndex, test):
        req = f"select id from co where co_name='{test}'"
        query = QSqlQuery(req)
        query.first()
        self.coId = query.value(0)
        print(req, query.value(0))

    def quit(self):
        self.close()

