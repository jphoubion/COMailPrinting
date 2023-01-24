# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customermanagementwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CustomerManagementWindow(object):
    def setupUi(self, CustomerManagementWindow):
        if not CustomerManagementWindow.objectName():
            CustomerManagementWindow.setObjectName(u"CustomerManagementWindow")
        CustomerManagementWindow.setWindowModality(Qt.ApplicationModal)
        CustomerManagementWindow.resize(822, 798)
        self.centralwidget = QWidget(CustomerManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 801, 751))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.le_code = QLineEdit(self.layoutWidget)
        self.le_code.setObjectName(u"le_code")

        self.horizontalLayout.addWidget(self.le_code)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_name = QLineEdit(self.layoutWidget)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout_2.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(150, 0))
        self.label_3.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cbb_co = QComboBox(self.layoutWidget)
        self.cbb_co.setObjectName(u"cbb_co")

        self.horizontalLayout_4.addWidget(self.cbb_co)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_new = QPushButton(self.layoutWidget)
        self.btn_new.setObjectName(u"btn_new")

        self.horizontalLayout_3.addWidget(self.btn_new)

        self.btn_add = QPushButton(self.layoutWidget)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.layoutWidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.layoutWidget)
        self.btn_quit.setObjectName(u"btn_quit")
        font = QFont()
        font.setBold(False)
        self.btn_quit.setFont(font)
        self.btn_quit.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btn_quit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.tw_customers = QTableWidget(self.layoutWidget)
        if (self.tw_customers.columnCount() < 5):
            self.tw_customers.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_customers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_customers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_customers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_customers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_customers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tw_customers.setObjectName(u"tw_customers")

        self.gridLayout.addWidget(self.tw_customers, 0, 0, 1, 1)

        CustomerManagementWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CustomerManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        CustomerManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CustomerManagementWindow)

        QMetaObject.connectSlotsByName(CustomerManagementWindow)
    # setupUi

    def retranslateUi(self, CustomerManagementWindow):
        CustomerManagementWindow.setWindowTitle(QCoreApplication.translate("CustomerManagementWindow", u"COMailPrinting - Gestion des clients", None))
        self.label.setText(QCoreApplication.translate("CustomerManagementWindow", u"Code client :", None))
        self.label_2.setText(QCoreApplication.translate("CustomerManagementWindow", u"Nom :", None))
        self.label_3.setText(QCoreApplication.translate("CustomerManagementWindow", u"C/O du client :", None))
        self.btn_new.setText(QCoreApplication.translate("CustomerManagementWindow", u"Nouveau", None))
        self.btn_add.setText(QCoreApplication.translate("CustomerManagementWindow", u"Ajouter", None))
        self.btn_delete.setText(QCoreApplication.translate("CustomerManagementWindow", u"Supprimer", None))
        self.btn_quit.setText(QCoreApplication.translate("CustomerManagementWindow", u"Quitter", None))
        ___qtablewidgetitem = self.tw_customers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CustomerManagementWindow", u"id", None));
        ___qtablewidgetitem1 = self.tw_customers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CustomerManagementWindow", u"Code client", None));
        ___qtablewidgetitem2 = self.tw_customers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CustomerManagementWindow", u"Nom", None));
        ___qtablewidgetitem3 = self.tw_customers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CustomerManagementWindow", u"C/O", None));
        ___qtablewidgetitem4 = self.tw_customers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("CustomerManagementWindow", u"idCo", None));
    # retranslateUi

