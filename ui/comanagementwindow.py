# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comanagementwindow.ui'
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
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_CoManagementWindow(object):
    def setupUi(self, CoManagementWindow):
        if not CoManagementWindow.objectName():
            CoManagementWindow.setObjectName(u"CoManagementWindow")
        CoManagementWindow.setWindowModality(Qt.ApplicationModal)
        CoManagementWindow.resize(612, 644)
        self.centralwidget = QWidget(CoManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tw_co = QTableWidget(self.centralwidget)
        if (self.tw_co.columnCount() < 3):
            self.tw_co.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tw_co.setObjectName(u"tw_co")

        self.verticalLayout.addWidget(self.tw_co)

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

        self.te_address = QTextEdit(self.centralwidget)
        self.te_address.setObjectName(u"te_address")
        self.te_address.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.te_address)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_modify = QPushButton(self.centralwidget)
        self.btn_modify.setObjectName(u"btn_modify")

        self.horizontalLayout_3.addWidget(self.btn_modify)

        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.centralwidget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout_3.addWidget(self.btn_quit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        CoManagementWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CoManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        CoManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CoManagementWindow)

        QMetaObject.connectSlotsByName(CoManagementWindow)
    # setupUi

    def retranslateUi(self, CoManagementWindow):
        CoManagementWindow.setWindowTitle(QCoreApplication.translate("CoManagementWindow", u"COMailPrinting - Gestion des C/O", None))
        ___qtablewidgetitem = self.tw_co.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CoManagementWindow", u"id", None));
        ___qtablewidgetitem1 = self.tw_co.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CoManagementWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.tw_co.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CoManagementWindow", u"Adresse", None));
        self.label.setText(QCoreApplication.translate("CoManagementWindow", u"Nom du C/O : ", None))
        self.label_2.setText(QCoreApplication.translate("CoManagementWindow", u"Adresse :", None))
        self.btn_add.setText(QCoreApplication.translate("CoManagementWindow", u"Ajouter", None))
        self.btn_modify.setText(QCoreApplication.translate("CoManagementWindow", u"Modifier", None))
        self.btn_delete.setText(QCoreApplication.translate("CoManagementWindow", u"Supprimer", None))
        self.btn_quit.setText(QCoreApplication.translate("CoManagementWindow", u"Quitter", None))
    # retranslateUi

