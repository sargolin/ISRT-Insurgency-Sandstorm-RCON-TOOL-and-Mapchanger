# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mvp_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 561)
        MainWindow.setMinimumSize(QtCore.QSize(588, 561))
        MainWindow.setMaximumSize(QtCore.QSize(588, 561))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.terminalwindows = QtWidgets.QLabel(self.centralwidget)
        self.terminalwindows.setGeometry(QtCore.QRect(10, 220, 564, 301))
        self.terminalwindows.setMinimumSize(QtCore.QSize(564, 301))
        self.terminalwindows.setMaximumSize(QtCore.QSize(564, 301))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.terminalwindows.setFont(font)
        self.terminalwindows.setAutoFillBackground(True)
        self.terminalwindows.setFrameShape(QtWidgets.QFrame.Box)
        self.terminalwindows.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.terminalwindows.setText("")
        self.terminalwindows.setWordWrap(True)
        self.terminalwindows.setObjectName("terminalwindows")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(11, 221, 561, 298))
        self.scrollArea.setMinimumSize(QtCore.QSize(561, 298))
        self.scrollArea.setMaximumSize(QtCore.QSize(561, 298))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 296))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 190, 563, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_rconcommand = QtWidgets.QLineEdit(self.layoutWidget)
        self.label_rconcommand.setMinimumSize(QtCore.QSize(480, 20))
        self.label_rconcommand.setMaximumSize(QtCore.QSize(480, 20))
        self.label_rconcommand.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_rconcommand.setObjectName("label_rconcommand")
        self.horizontalLayout_2.addWidget(self.label_rconcommand)
        self.rconsubmitbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.rconsubmitbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rconsubmitbutton.setObjectName("rconsubmitbutton")
        self.horizontalLayout_2.addWidget(self.rconsubmitbutton)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 563, 172))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.entryip = QtWidgets.QLineEdit(self.layoutWidget1)
        self.entryip.setObjectName("entryip")
        self.verticalLayout.addWidget(self.entryip)
        self.entryqueryport = QtWidgets.QLineEdit(self.layoutWidget1)
        self.entryqueryport.setObjectName("entryqueryport")
        self.verticalLayout.addWidget(self.entryqueryport)
        self.entryrconport = QtWidgets.QLineEdit(self.layoutWidget1)
        self.entryrconport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entryrconport.setObjectName("entryrconport")
        self.verticalLayout.addWidget(self.entryrconport)
        self.entryrconpw = QtWidgets.QLineEdit(self.layoutWidget1)
        self.entryrconpw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entryrconpw.setObjectName("entryrconpw")
        self.verticalLayout.addWidget(self.entryrconpw)
        self.submitbutton = QtWidgets.QPushButton(self.layoutWidget1)
        self.submitbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitbutton.setObjectName("submitbutton")
        self.verticalLayout.addWidget(self.submitbutton)
        self.exitbutton = QtWidgets.QPushButton(self.layoutWidget1)
        self.exitbutton.setObjectName("exitbutton")
        self.verticalLayout.addWidget(self.exitbutton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.querywindow = QtWidgets.QLabel(self.layoutWidget1)
        self.querywindow.setMinimumSize(QtCore.QSize(420, 170))
        self.querywindow.setMaximumSize(QtCore.QSize(420, 170))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.querywindow.setFont(font)
        self.querywindow.setAutoFillBackground(True)
        self.querywindow.setFrameShape(QtWidgets.QFrame.Box)
        self.querywindow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.querywindow.setText("")
        self.querywindow.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.querywindow.setObjectName("querywindow")
        self.horizontalLayout.addWidget(self.querywindow)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.scrollArea.raise_()
        self.terminalwindows.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 588, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionINfo = QtWidgets.QAction(MainWindow)
        self.actionINfo.setObjectName("actionINfo")
        self.menuFile.addAction(self.actionQuit)
        self.menu.addAction(self.actionINfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Insurgency Sandstorm RCON Tool - ISRT"))
        self.label_rconcommand.setText(_translate("MainWindow", "help"))
        self.label_rconcommand.setPlaceholderText(_translate("MainWindow", "RCon Command"))
        self.rconsubmitbutton.setText(_translate("MainWindow", "Submit RCON"))
        self.entryip.setText(_translate("MainWindow", "93.186.198.185"))
        self.entryip.setPlaceholderText(_translate("MainWindow", "IP-Adress"))
        self.entryqueryport.setText(_translate("MainWindow", "27016"))
        self.entryqueryport.setPlaceholderText(_translate("MainWindow", "Query Port"))
        self.entryrconport.setText(_translate("MainWindow", "27017"))
        self.entryrconport.setPlaceholderText(_translate("MainWindow", "RCON Port"))
        self.entryrconpw.setText(_translate("MainWindow", "Rfcd2025"))
        self.entryrconpw.setPlaceholderText(_translate("MainWindow", "RCON Password"))
        self.submitbutton.setText(_translate("MainWindow", "Query Server"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionINfo.setText(_translate("MainWindow", "About"))
        self.actionINfo.setShortcut(_translate("MainWindow", "Ctrl+I"))
