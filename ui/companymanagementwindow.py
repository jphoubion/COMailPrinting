# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'companymanagementwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CompanyManagementWindow(object):
    def setupUi(self, CompanyManagementWindow):
        if not CompanyManagementWindow.objectName():
            CompanyManagementWindow.setObjectName(u"CompanyManagementWindow")
        CompanyManagementWindow.setWindowModality(Qt.ApplicationModal)
        CompanyManagementWindow.resize(509, 456)
        self.centralwidget = QWidget(CompanyManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tw_companies = QTableWidget(self.centralwidget)
        if (self.tw_companies.columnCount() < 2):
            self.tw_companies.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_companies.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_companies.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tw_companies.setObjectName(u"tw_companies")

        self.gridLayout.addWidget(self.tw_companies, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(self.centralwidget)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_form = QLineEdit(self.centralwidget)
        self.le_form.setObjectName(u"le_form")

        self.horizontalLayout_2.addWidget(self.le_form)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.centralwidget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout_3.addWidget(self.btn_quit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        CompanyManagementWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CompanyManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        CompanyManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CompanyManagementWindow)

        QMetaObject.connectSlotsByName(CompanyManagementWindow)
    # setupUi

    def retranslateUi(self, CompanyManagementWindow):
        CompanyManagementWindow.setWindowTitle(QCoreApplication.translate("CompanyManagementWindow", u"Gestion des soci\u00e9t\u00e9s", None))
        ___qtablewidgetitem = self.tw_companies.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CompanyManagementWindow", u"Nom", None));
        ___qtablewidgetitem1 = self.tw_companies.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CompanyManagementWindow", u"Forme jur.", None));
        self.label.setText(QCoreApplication.translate("CompanyManagementWindow", u"Nom de la soci\u00e9t\u00e9 :", None))
        self.label_2.setText(QCoreApplication.translate("CompanyManagementWindow", u"Forme juridique :", None))
        self.btn_add.setText(QCoreApplication.translate("CompanyManagementWindow", u"Ajouter", None))
        self.btn_delete.setText(QCoreApplication.translate("CompanyManagementWindow", u"Supprimer", None))
        self.btn_quit.setText(QCoreApplication.translate("CompanyManagementWindow", u"Quitter", None))
    # retranslateUi

