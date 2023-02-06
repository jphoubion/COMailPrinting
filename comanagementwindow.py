from functools import partial

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlRelationalTableModel, QSqlTableModel, QSqlRelation, QSqlDatabase, QSqlRelationalDelegate
from PySide6.QtWidgets import QMainWindow, QLabel, QTextEdit, QApplication, QMessageBox

import sqlmanagement
from ui.comanagementwindow import Ui_CoManagementWindow

class CoManagementWindow(QtWidgets.QMainWindow, Ui_CoManagementWindow):

    def __init__(self, conn, parent=None):
        super(CoManagementWindow, self).__init__(parent)
        self.setupUi(self)

        self.db_connection = conn
        self.parentWindow = parent

        self.setupConnection()

        self.co_id = 0
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
            self.model.setTable("co")
            self.tv_co.setAlternatingRowColors(True)
            # self.model.setRelation(3, QSqlRelation("co", "id", "co_name"))
            self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model.setHeaderData(0, Qt.Horizontal, "id")
            self.model.setHeaderData(1, Qt.Horizontal, "Nom")
            self.model.setHeaderData(2, Qt.Horizontal, "Adresse")
            self.model.select()
            self.tv_co.setModel(self.model)
            self.tv_co.setSortingEnabled(True)
            self.tv_co.hideColumn(0)
            self.tv_co.sortByColumn(1, QtCore.Qt.AscendingOrder)
            # self.tv_co.setItemDelegate(QSqlRelationalDelegate())
            self.tv_co.resizeColumnsToContents()
            self.tv_co.resizeRowsToContents()


    def setupConnection(self):
    # self.btn_new.clicked.connect(self.newCo)
    # self.btn_add.clicked.connect(partial(self.addCo, self.db_connection, self.le_name, self.te_address))
    # self.btn_modify.clicked.connect(partial(self.modifyCo, self.db_connection))
    # self.btn_delete.clicked.connect(partial(self.deleteCo, self.db_connection))
        self.btn_quit.clicked.connect(self.quit)

    # def newCo(self):
    #     self.le_name.setText('')
    #     self.te_address.setText('')
    #
    # def addCo(self, conn, name, address):
    #     req = f"INSERT INTO co (co_name, co_address) VALUES ('{name.text()}', '{address.toPlainText()}')"
    #     print(req)
    #     res_co = sqlmanagement.get_result(conn, req)
    #     conn.commit()
    #
    #     # Adding a row to the table
    #     self.tw_co.insertRow(self.tw_co.rowCount())
    #     self.addCoNameField(name.text())
    #     self.addCoAddressField(address.toPlainText())
    #
    #     self.le_name.clear()
    #     self.te_address.clear()
    #
    # def modifyCo(self, conn):
    #     id = self.tw_co.cellWidget(self.tw_co.currentRow(), 0)
    #     name = self.le_name.text()
    #     address = self.te_address.toPlainText()
    #     req = f"UPDATE co SET co_name = '{name}', co_address = '{address}' WHERE id = {id.text()}"
    #     result = sqlmanagement.get_result(conn, req)
    #     conn.commit()
    #
    #     self.tw_co.cellWidget(self.tw_co.currentRow(), 1).setText(name)
    #     self.tw_co.cellWidget(self.tw_co.currentRow(), 2).setText(address)
    #
    # def deleteCo(self, conn):
    #     id = self.tw_co.cellWidget(self.tw_co.currentRow(), 0)
    #     res_co = sqlmanagement.get_result(conn, \
    #     f"DELETE FROM co WHERE id = {id.text()}")
    #     conn.commit()
    #     self.tw_co.removeRow(self.tw_co.currentRow())
    #
    # def fillFields(self):
    #     self.co_id = self.tw_co.cellWidget(self.tw_co.currentRow(), 0).text()
    #     self.le_name.setText(self.tw_co.cellWidget(self.tw_co.currentRow(), 1).text())
    #     self.te_address.setText(self.tw_co.cellWidget(self.tw_co.currentRow(), 2).text())

    def quit(self):
        self.close()
