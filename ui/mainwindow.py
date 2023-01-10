# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(988, 579)
        MainWindow.setStyleSheet(u"")
        self.actionGestion = QAction(MainWindow)
        self.actionGestion.setObjectName(u"actionGestion")
        self.actionQuitter = QAction(MainWindow)
        self.actionQuitter.setObjectName(u"actionQuitter")
        self.actionImport_customers = QAction(MainWindow)
        self.actionImport_customers.setObjectName(u"actionImport_customers")
        self.actionImport_CO_depuis_XLSX = QAction(MainWindow)
        self.actionImport_CO_depuis_XLSX.setObjectName(u"actionImport_CO_depuis_XLSX")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tw_co = QTableWidget(self.centralwidget)
        if (self.tw_co.columnCount() < 7):
            self.tw_co.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font = QFont()
        font.setBold(False)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tw_co.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tw_co.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tw_co.setObjectName(u"tw_co")
        self.tw_co.setGeometry(QRect(10, 40, 871, 481))
        self.btnAddRow = QPushButton(self.centralwidget)
        self.btnAddRow.setObjectName(u"btnAddRow")
        self.btnAddRow.setGeometry(QRect(890, 40, 80, 23))
        self.btnAddRow.setStyleSheet(u"")
        self.btnAddRow_2 = QPushButton(self.centralwidget)
        self.btnAddRow_2.setObjectName(u"btnAddRow_2")
        self.btnAddRow_2.setGeometry(QRect(890, 70, 80, 23))
        self.btnAddRow_3 = QPushButton(self.centralwidget)
        self.btnAddRow_3.setObjectName(u"btnAddRow_3")
        self.btnAddRow_3.setGeometry(QRect(890, 100, 80, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 241, 21))
        self.cbb_company = QComboBox(self.centralwidget)
        self.cbb_company.setObjectName(u"cbb_company")
        self.cbb_company.setGeometry(QRect(260, 10, 171, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 988, 22))
        self.menufichier = QMenu(self.menubar)
        self.menufichier.setObjectName(u"menufichier")
        self.menuImport = QMenu(self.menubar)
        self.menuImport.setObjectName(u"menuImport")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menufichier.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menufichier.addSeparator()
        self.menufichier.addAction(self.actionQuitter)
        self.menuImport.addAction(self.actionImport_customers)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGestion.setText(QCoreApplication.translate("MainWindow", u"Gestion", None))
        self.actionQuitter.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.actionImport_customers.setText(QCoreApplication.translate("MainWindow", u"Import clients depuis XLSX", None))
        self.actionImport_CO_depuis_XLSX.setText(QCoreApplication.translate("MainWindow", u"Import CO depuis XLSX", None))
        ___qtablewidgetitem = self.tw_co.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Client", None));
        ___qtablewidgetitem1 = self.tw_co.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C/O", None));
        ___qtablewidgetitem2 = self.tw_co.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Coordonn\u00e9es C/O", None));
        ___qtablewidgetitem3 = self.tw_co.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"R\u00e9f\u00e9rences", None));
        ___qtablewidgetitem4 = self.tw_co.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Soc. emettrice", None));
        ___qtablewidgetitem5 = self.tw_co.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"MAJ C/O", None));
        ___qtablewidgetitem6 = self.tw_co.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MAJ Client", None));
        self.btnAddRow.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.btnAddRow_2.setText(QCoreApplication.translate("MainWindow", u"Copier", None))
        self.btnAddRow_3.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Soci\u00e9t\u00e9 \u00e9metrice du courrier par d\u00e9faut:", None))
        self.menufichier.setTitle(QCoreApplication.translate("MainWindow", u"fichier", None))
        self.menuImport.setTitle(QCoreApplication.translate("MainWindow", u"Import", None))
    # retranslateUi

