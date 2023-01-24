from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication

import sqlmanagement
from ui.customermanagementwindow import Ui_CustomerManagementWindow

class CustomerManagementWindow(QtWidgets.QMainWindow, Ui_CustomerManagementWindow):
    def __init__(self, conn, parent=None):
        super(CustomerManagementWindow, self).__init__(parent)
        self.setupUi(self)

        self.db_connection = conn
        self.parentWindow = parent

        self.setupConnection()
        self.fillTable(self.db_connection)

        self.co_id = ''

    def setupConnection(self):
        self.btn_new.clicked.connect(self.addCustomer)
        self.btn_add.clicked.connect(self.modifiyCustomer)
        self.btn_delete.clicked.connect(self.deleteCustomer)
        self.btn_quit.clicked.connect(self.quit)

        self.tw_customers.cellClicked.connect(self.fillfields)

    def fillTable(self, conn):
        QApplication.setOverrideCursor(Qt.WaitCursor)
        res_customer = sqlmanagement.get_result(conn, "SELECT * FROM co")
        for customer in res_customer:
            # add row to the table
            self.tw_customers.insertRow(self.tw_customers.rowCount())
            self.addCustomerCOIdField(customer[0])
            self.addCustomerCodeField(customer[1])
            self.addCustomerNameField(customer[2])

            self.tw_customers.resizeColumnsToContents()
            self.tw_customers.resizeRowsToContents()

        QApplication.setOverrideCursor(Qt.ArrowCursor)

    def addIdField(self, id):
        te_customer_id = QLabel()
        # te_id.setFixedWidth(0)
        te_customer_id.setText(str(id))
        self.tw_customers.setCellWidget(self.tw_customers.rowCount() - 1, 0, te_customer_id)
        self.tw_customers.hideColumn(0)
        # te_id.setFixedHeight(30)

    def addCustomerCodeField(self):
        lbl_customer_code = QLabel()
        lbl_customer_code.setFixedWidth(200)
        lbl_customer_code.setText("jklqsdjflkdqs")
        self.tw_customers.setCellWidget(self.tw_customers.rowCount()-1, 1, lbl_customer_code)

    def addCustomerNameField(self):
        lbl_customer_name = QLabel()
        lbl_customer_name.setFixedWidth(200)
        lbl_customer_name.setText("qdfqsdfsdqf")
        self.tw_customers.setCellWidget(self.tw_customers.rowCount()-1, 2, lbl_customer_name)

    def addCustomerCOField(self):
        pass

    def addCustomerCOIdField(self):
        pass

    def newCustomer(self):
        """cleaning the customers field to create a new one"""
        pass

    def addCustomer(self):
        pass

    def modifiyCustomer(self):
        pass

    def deleteCustomer(self):
        pass

    def fillfields(self):
        pass

    def quit(self):
        self.close()

