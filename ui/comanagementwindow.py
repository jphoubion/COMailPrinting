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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_CoManagementWindow(object):
    def setupUi(self, CoManagementWindow):
        if not CoManagementWindow.objectName():
            CoManagementWindow.setObjectName(u"CoManagementWindow")
        CoManagementWindow.setWindowModality(Qt.ApplicationModal)
        CoManagementWindow.resize(614, 668)
        self.centralwidget = QWidget(CoManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
        self.tw_co.setGeometry(QRect(12, 12, 591, 451))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 470, 591, 24))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(self.widget)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout.addWidget(self.le_name)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 500, 591, 102))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.te_address = QTextEdit(self.widget1)
        self.te_address.setObjectName(u"te_address")
        self.te_address.setMinimumSize(QSize(0, 0))
        self.te_address.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_2.addWidget(self.te_address)

        self.widget2 = QWidget(self.centralwidget)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(11, 615, 591, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_new = QPushButton(self.widget2)
        self.btn_new.setObjectName(u"btn_new")

        self.horizontalLayout_3.addWidget(self.btn_new)

        self.btn_add = QPushButton(self.widget2)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_modify = QPushButton(self.widget2)
        self.btn_modify.setObjectName(u"btn_modify")

        self.horizontalLayout_3.addWidget(self.btn_modify)

        self.btn_delete = QPushButton(self.widget2)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.widget2)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout_3.addWidget(self.btn_quit)

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
        self.btn_new.setText(QCoreApplication.translate("CoManagementWindow", u"Nouveau", None))
        self.btn_add.setText(QCoreApplication.translate("CoManagementWindow", u"Ajouter", None))
        self.btn_modify.setText(QCoreApplication.translate("CoManagementWindow", u"Modifier", None))
        self.btn_delete.setText(QCoreApplication.translate("CoManagementWindow", u"Supprimer", None))
        self.btn_quit.setText(QCoreApplication.translate("CoManagementWindow", u"Quitter", None))
    # retranslateUi

