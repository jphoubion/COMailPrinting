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
    QSizePolicy, QSpacerItem, QStatusBar, QTableView,
    QTextEdit, QWidget)

class Ui_CoManagementWindow(object):
    def setupUi(self, CoManagementWindow):
        if not CoManagementWindow.objectName():
            CoManagementWindow.setObjectName(u"CoManagementWindow")
        CoManagementWindow.setWindowModality(Qt.ApplicationModal)
        CoManagementWindow.resize(614, 660)
        self.centralwidget = QWidget(CoManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 591, 621))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tv_co = QTableView(self.widget)
        self.tv_co.setObjectName(u"tv_co")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tv_co.sizePolicy().hasHeightForWidth())
        self.tv_co.setSizePolicy(sizePolicy)
        self.tv_co.setMinimumSize(QSize(0, 420))

        self.gridLayout.addWidget(self.tv_co, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.te_address = QTextEdit(self.widget)
        self.te_address.setObjectName(u"te_address")
        self.te_address.setEnabled(False)
        self.te_address.setMinimumSize(QSize(0, 0))
        self.te_address.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_2.addWidget(self.te_address)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.label)

        self.le_name = QLineEdit(self.widget)
        self.le_name.setObjectName(u"le_name")
        self.le_name.setEnabled(False)

        self.horizontalLayout.addWidget(self.le_name)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_new = QPushButton(self.widget)
        self.btn_new.setObjectName(u"btn_new")
        self.btn_new.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_new)

        self.btn_add = QPushButton(self.widget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_add)

        self.btn_modify = QPushButton(self.widget)
        self.btn_modify.setObjectName(u"btn_modify")
        self.btn_modify.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_modify)

        self.btn_delete = QPushButton(self.widget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btn_delete)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_quit = QPushButton(self.widget)
        self.btn_quit.setObjectName(u"btn_quit")

        self.horizontalLayout_3.addWidget(self.btn_quit)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        CoManagementWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CoManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        CoManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CoManagementWindow)

        QMetaObject.connectSlotsByName(CoManagementWindow)
    # setupUi

    def retranslateUi(self, CoManagementWindow):
        CoManagementWindow.setWindowTitle(QCoreApplication.translate("CoManagementWindow", u"COMailPrinting - Gestion des C/O", None))
        self.label_2.setText(QCoreApplication.translate("CoManagementWindow", u"Adresse :", None))
        self.label.setText(QCoreApplication.translate("CoManagementWindow", u"Nom du C/O : ", None))
        self.btn_new.setText(QCoreApplication.translate("CoManagementWindow", u"Nouveau", None))
        self.btn_add.setText(QCoreApplication.translate("CoManagementWindow", u"Ajouter", None))
        self.btn_modify.setText(QCoreApplication.translate("CoManagementWindow", u"Modifier", None))
        self.btn_delete.setText(QCoreApplication.translate("CoManagementWindow", u"Supprimer", None))
        self.btn_quit.setText(QCoreApplication.translate("CoManagementWindow", u"Quitter", None))
    # retranslateUi

