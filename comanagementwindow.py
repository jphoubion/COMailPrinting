from functools import partial

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QTextEdit, QApplication

import sqlmanagement
from ui.comanagementwindow import Ui_CoManagementWindow

class CoManagementWindow(QtWidgets.QMainWindow, Ui_CoManagementWindow):

    def __init__(self, conn, parent=None):
        super(CoManagementWindow, self).__init__(parent)
        self.setupUi(self)

        self.db_connection = conn
        self.parentWindow = parent

        self.setupConnection()
        self.fillTable(self.db_connection)

        self.co_id = ''

    def setupConnection(self):
        self.btn_new.clicked.connect(self.newCo)
        self.btn_add.clicked.connect(partial(self.addCo, self.db_connection, self.le_name, self.te_address))
        self.btn_modify.clicked.connect(partial(self.modifyCo, self.db_connection))
        self.btn_delete.clicked.connect(partial(self.deleteCo, self.db_connection))
        self.btn_quit.clicked.connect(self.quit)

        self.tw_co.cellClicked.connect(self.fillFields)

    def fillTable(self, conn):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        res_co = sqlmanagement.get_result(conn, "SELECT * FROM co")
        for co in res_co:
            # add row to the table
            self.tw_co.insertRow(self.tw_co.rowCount())
            self.addIdField(co[0])
            self.addCoNameField(co[1])
            self.addCoAddressField(co[2])

            self.tw_co.resizeColumnsToContents()
            self.tw_co.resizeRowsToContents()

        QApplication.setOverrideCursor(Qt.ArrowCursor)

    def addIdField(self, id):
        te_id = QLabel()
        # te_id.setFixedWidth(0)
        te_id.setText(str(id))
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 0, te_id)
        self.tw_co.hideColumn(0)
        # te_id.setFixedHeigsht(30)

    def addCoNameField(self, co_name):
        le_name = QLabel()
        le_name.setFixedWidth(200)
        le_name.setText(co_name)
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 1, le_name)

    def addCoAddressField(self, co_address):
        te_address = QLabel()
        te_address.setFixedWidth(300)
        te_address.setText(co_address)
        self.tw_co.setCellWidget(self.tw_co.rowCount() - 1, 2, te_address)
        te_address.setFixedHeight(60)

    def newCo(self):
        self.le_name.setText('')
        self.te_address.setText('')

    def addCo(self, conn, name, address):
        req = f"INSERT INTO co (co_name, co_address) VALUES ('{name.text()}', '{address.toPlainText()}')"
        print(req)
        res_co = sqlmanagement.get_result(conn, req)
        conn.commit()

        # Adding a row to the table
        self.tw_co.insertRow(self.tw_co.rowCount())
        self.addCoNameField(name.text())
        self.addCoAddressField(address.toPlainText())

        self.le_name.clear()
        self.te_address.clear()

    def modifyCo(self, conn):
        id = self.tw_co.cellWidget(self.tw_co.currentRow(), 0)
        name = self.le_name.text()
        address = self.te_address.toPlainText()
        req = f"UPDATE co SET co_name = '{name}', co_address = '{address}' WHERE id = {id.text()}"
        result = sqlmanagement.get_result(conn, req)
        conn.commit()

        self.tw_co.cellWidget(self.tw_co.currentRow(), 1).setText(name)
        self.tw_co.cellWidget(self.tw_co.currentRow(), 2).setText(address)

    def deleteCo(self, conn):
        id = self.tw_co.cellWidget(self.tw_co.currentRow(), 0)
        res_co = sqlmanagement.get_result(conn, \
        f"DELETE FROM co WHERE id = {id.text()}")
        conn.commit()
        self.tw_co.removeRow(self.tw_co.currentRow())

    def fillFields(self):
        self.co_id = self.tw_co.cellWidget(self.tw_co.currentRow(), 0).text()
        self.le_name.setText(self.tw_co.cellWidget(self.tw_co.currentRow(), 1).text())
        self.te_address.setText(self.tw_co.cellWidget(self.tw_co.currentRow(), 2).text())

    def quit(self):
        self.close()
