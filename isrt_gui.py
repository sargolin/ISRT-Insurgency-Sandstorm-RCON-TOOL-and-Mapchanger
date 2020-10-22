# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mvp.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.terminalwindows = QtWidgets.QLabel(self.centralwidget)
        self.terminalwindows.setGeometry(QtCore.QRect(10, 200, 611, 231))

        font = QtGui.QFont()
        font.setPointSize(6)

        self.terminalwindows.setFont(font)
        self.terminalwindows.setAutoFillBackground(True)
        self.terminalwindows.setFrameShape(QtWidgets.QFrame.Box)
        self.terminalwindows.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.terminalwindows.setText("")
        self.terminalwindows.setWordWrap(True)
        self.terminalwindows.setObjectName("terminalwindows")


        self.querywindow = QtWidgets.QLabel(self.centralwidget)
        self.querywindow.setGeometry(QtCore.QRect(10, 50, 301, 141))

        font = QtGui.QFont()
        font.setPointSize(6)

        self.querywindow.setFont(font)
        self.querywindow.setAutoFillBackground(True)
        self.querywindow.setFrameShape(QtWidgets.QFrame.Box)
        self.querywindow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.querywindow.setText("")
        self.querywindow.setObjectName("querywindow")

        self.label_rconcommand = QtWidgets.QLineEdit(self.centralwidget)
        self.label_rconcommand.setGeometry(QtCore.QRect(320, 90, 301, 71))
        self.label_rconcommand.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_rconcommand.setObjectName("label_rconcommand")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 552, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.entryip = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryip.setObjectName("entryip")
        self.horizontalLayout.addWidget(self.entryip)

        self.entryqueryport = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryqueryport.setObjectName("entryqueryport")
        self.horizontalLayout.addWidget(self.entryqueryport)

        self.entryrconport = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryrconport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entryrconport.setObjectName("entryrconport")
        self.horizontalLayout.addWidget(self.entryrconport)

        self.entryrconpw = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryrconpw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entryrconpw.setObjectName("entryrconpw")
        self.horizontalLayout.addWidget(self.entryrconpw)

        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(400, 50, 158, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.submitbutton = QtWidgets.QPushButton(self.layoutWidget1)
        self.submitbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitbutton.setObjectName("submitbutton")
        self.horizontalLayout_2.addWidget(self.submitbutton)

        self.exitbutton = QtWidgets.QPushButton(self.layoutWidget1)
        self.exitbutton.setObjectName("exitbutton")
        self.horizontalLayout_2.addWidget(self.exitbutton)

        self.submitbutton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.submitbutton_2.setGeometry(QtCore.QRect(404, 167, 121, 23))
        self.submitbutton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitbutton_2.setObjectName("submitbutton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Insurgency Sandstorm RCON Tool - ISRT v0-1"))
        self.label_rconcommand.setPlaceholderText(_translate("MainWindow", "RCon Command"))
        self.entryip.setPlaceholderText(_translate("MainWindow", "IP-Adress"))
        self.entryqueryport.setPlaceholderText(_translate("MainWindow", "Query Port"))
        self.entryrconport.setPlaceholderText(_translate("MainWindow", "RCON Port"))
        self.entryrconpw.setPlaceholderText(_translate("MainWindow", "RCON Password"))
        self.submitbutton.setText(_translate("MainWindow", "Submit"))
        self.exitbutton.setText(_translate("MainWindow", "Exit"))
        self.submitbutton_2.setText(_translate("MainWindow", "Submit RCON"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionINfo.setText(_translate("MainWindow", "About"))
