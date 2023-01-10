# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cocreationwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(475, 317)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.lbl_nomco = QLabel(self.centralwidget)
        self.lbl_nomco.setObjectName(u"lbl_nomco")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_nomco.sizePolicy().hasHeightForWidth())
        self.lbl_nomco.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lbl_nomco)

        self.le_com_co = QLineEdit(self.centralwidget)
        self.le_com_co.setObjectName(u"le_com_co")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_com_co.sizePolicy().hasHeightForWidth())
        self.le_com_co.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.le_com_co)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.lbl_coordonnees = QLabel(self.centralwidget)
        self.lbl_coordonnees.setObjectName(u"lbl_coordonnees")

        self.horizontalLayout_2.addWidget(self.lbl_coordonnees)

        self.te_coordonnees = QTextEdit(self.centralwidget)
        self.te_coordonnees.setObjectName(u"te_coordonnees")

        self.horizontalLayout_2.addWidget(self.te_coordonnees)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lbl_last_update = QLabel(self.centralwidget)
        self.lbl_last_update.setObjectName(u"lbl_last_update")

        self.horizontalLayout_3.addWidget(self.lbl_last_update)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 475, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cr\u00e9er / Mettre \u00e0 jour un C/O", None))
        self.lbl_nomco.setText(QCoreApplication.translate("MainWindow", u"Nom C/O", None))
        self.lbl_coordonnees.setText(QCoreApplication.translate("MainWindow", u"Coordonn\u00e9es", None))
        self.lbl_last_update.setText(QCoreApplication.translate("MainWindow", u"Date de derni\u00e8re mise \u00e0 jour", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
    # retranslateUi

