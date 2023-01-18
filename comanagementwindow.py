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
        self.db_connecion = conn
        self.parentWindow = parent

        self.setupConnection()
        self.fillTable(self.db_connecion)

    def setupConnection(self):
        self.btn_add.clicked.connect(partial(self.addCo, self.db_connecion, self.le_name, self.te_address))

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

    def addCo(self):
        pass
