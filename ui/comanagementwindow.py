# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comanagementwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_CoManagementWindow(object):
    def setupUi(self, CoManagementWindow):
        if not CoManagementWindow.objectName():
            CoManagementWindow.setObjectName(u"CoManagementWindow")
        CoManagementWindow.setWindowModality(Qt.ApplicationModal)
        CoManagementWindow.resize(507, 453)
        self.centralwidget = QWidget(CoManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 491, 421))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(self.widget)
        self.le_name.setObjectName(u"le_name")

        self.horizontalLayout.addWidget(self.le_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.widget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout_3.addWidget(self.btn_quit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        CoManagementWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CoManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        CoManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CoManagementWindow)

        QMetaObject.connectSlotsByName(CoManagementWindow)
    # setupUi

    def retranslateUi(self, CoManagementWindow):
        CoManagementWindow.setWindowTitle(QCoreApplication.translate("CoManagementWindow", u"COMailPrinting - Gestion des C/O", None))
        self.label.setText(QCoreApplication.translate("CoManagementWindow", u"Nom du C/O : ", None))
        self.label_2.setText(QCoreApplication.translate("CoManagementWindow", u"Adresse :", None))
        self.btn_add.setText(QCoreApplication.translate("CoManagementWindow", u"Ajouter", None))
        self.btn_delete.setText(QCoreApplication.translate("CoManagementWindow", u"Supprimer", None))
        self.btn_quit.setText(QCoreApplication.translate("CoManagementWindow", u"Quitter", None))
    # retranslateUi

