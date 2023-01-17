# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customermanagementwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_CustomerManagementWindow(object):
    def setupUi(self, CustomerManagementWindow):
        if not CustomerManagementWindow.objectName():
            CustomerManagementWindow.setObjectName(u"CustomerManagementWindow")
        CustomerManagementWindow.setWindowModality(Qt.ApplicationModal)
        CustomerManagementWindow.resize(800, 600)
        self.centralwidget = QWidget(CustomerManagementWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        CustomerManagementWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CustomerManagementWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        CustomerManagementWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CustomerManagementWindow)
        self.statusbar.setObjectName(u"statusbar")
        CustomerManagementWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CustomerManagementWindow)

        QMetaObject.connectSlotsByName(CustomerManagementWindow)
    # setupUi

    def retranslateUi(self, CustomerManagementWindow):
        CustomerManagementWindow.setWindowTitle(QCoreApplication.translate("CustomerManagementWindow", u"COMailPrinting - Gestion des clients", None))
    # retranslateUi

