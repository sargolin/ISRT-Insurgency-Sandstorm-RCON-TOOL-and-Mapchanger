# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\isrt_main_v0.3.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
icondir = Path(__file__).absolute().parent

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 534)
        MainWindow.setMinimumSize(QtCore.QSize(585, 534))
        MainWindow.setMaximumSize(QtCore.QSize(585, 534))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStatusTip("")
        self.centralwidget.setObjectName("centralwidget")
        self.le_servername = QtWidgets.QLineEdit(self.centralwidget)
        self.le_servername.setGeometry(QtCore.QRect(158, 13, 411, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_servername.setFont(font)
        self.le_servername.setAutoFillBackground(False)
        self.le_servername.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_servername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_servername.setReadOnly(True)
        self.le_servername.setObjectName("le_servername")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(468, 40, 101, 126))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.le_vac = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_vac.setFont(font)
        self.le_vac.setAutoFillBackground(False)
        self.le_vac.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_vac.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_vac.setReadOnly(True)
        self.le_vac.setObjectName("le_vac")
        self.verticalLayout_3.addWidget(self.le_vac)
        self.le_ranked = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_ranked.setFont(font)
        self.le_ranked.setAutoFillBackground(False)
        self.le_ranked.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_ranked.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_ranked.setReadOnly(True)
        self.le_ranked.setObjectName("le_ranked")
        self.verticalLayout_3.addWidget(self.le_ranked)
        self.le_password = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_password.setFont(font)
        self.le_password.setAutoFillBackground(False)
        self.le_password.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_password.setReadOnly(True)
        self.le_password.setObjectName("le_password")
        self.verticalLayout_3.addWidget(self.le_password)
        self.le_players = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_players.setFont(font)
        self.le_players.setAutoFillBackground(False)
        self.le_players.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_players.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_players.setReadOnly(True)
        self.le_players.setObjectName("le_players")
        self.verticalLayout_3.addWidget(self.le_players)
        self.le_ping = QtWidgets.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_ping.setFont(font)
        self.le_ping.setAutoFillBackground(False)
        self.le_ping.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_ping.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_ping.setReadOnly(True)
        self.le_ping.setObjectName("le_ping")
        self.verticalLayout_3.addWidget(self.le_ping)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 40, 71, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 64, 71, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 90, 71, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 120, 71, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 143, 71, 20))
        self.label_10.setObjectName("label_10")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(16, 13, 135, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.entryip = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryip.setObjectName("entryip")
        self.verticalLayout.addWidget(self.entryip)
        self.entryqueryport = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryqueryport.setObjectName("entryqueryport")
        self.verticalLayout.addWidget(self.entryqueryport)
        self.submitbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.submitbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.submitbutton.setObjectName("submitbutton")
        self.verticalLayout.addWidget(self.submitbutton)
        self.entryrconport = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryrconport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entryrconport.setObjectName("entryrconport")
        self.verticalLayout.addWidget(self.entryrconport)
        self.entryrconpw = QtWidgets.QLineEdit(self.layoutWidget)
        self.entryrconpw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entryrconpw.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.entryrconpw.setObjectName("entryrconpw")
        self.verticalLayout.addWidget(self.entryrconpw)
        self.rconsubmitbutton = QtWidgets.QPushButton(self.layoutWidget)
        self.rconsubmitbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rconsubmitbutton.setObjectName("rconsubmitbutton")
        self.verticalLayout.addWidget(self.rconsubmitbutton)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(244, 40, 141, 126))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_gamemode = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_gamemode.setFont(font)
        self.le_gamemode.setAutoFillBackground(False)
        self.le_gamemode.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_gamemode.setText("")
        self.le_gamemode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_gamemode.setReadOnly(True)
        self.le_gamemode.setObjectName("le_gamemode")
        self.verticalLayout_2.addWidget(self.le_gamemode)
        self.le_servermode = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_servermode.setFont(font)
        self.le_servermode.setAutoFillBackground(False)
        self.le_servermode.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_servermode.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_servermode.setReadOnly(True)
        self.le_servermode.setObjectName("le_servermode")
        self.verticalLayout_2.addWidget(self.le_servermode)
        self.le_serverip_port = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_serverip_port.setFont(font)
        self.le_serverip_port.setAutoFillBackground(False)
        self.le_serverip_port.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_serverip_port.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_serverip_port.setReadOnly(True)
        self.le_serverip_port.setObjectName("le_serverip_port")
        self.verticalLayout_2.addWidget(self.le_serverip_port)
        self.le_mods = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_mods.setFont(font)
        self.le_mods.setAutoFillBackground(False)
        self.le_mods.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_mods.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_mods.setReadOnly(True)
        self.le_mods.setObjectName("le_mods")
        self.verticalLayout_2.addWidget(self.le_mods)
        self.le_map = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.le_map.setFont(font)
        self.le_map.setAutoFillBackground(False)
        self.le_map.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.le_map.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_map.setReadOnly(True)
        self.le_map.setObjectName("le_map")
        self.verticalLayout_2.addWidget(self.le_map)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(394, 40, 68, 121))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(14, 180, 558, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_rconcommand = QtWidgets.QLineEdit(self.layoutWidget3)
        self.label_rconcommand.setMinimumSize(QtCore.QSize(530, 21))
        self.label_rconcommand.setMaximumSize(QtCore.QSize(530, 21))
        self.label_rconcommand.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_rconcommand.setObjectName("label_rconcommand")
        self.horizontalLayout.addWidget(self.label_rconcommand)
        self.rconhelpbutton = QtWidgets.QPushButton(self.layoutWidget3)
        self.rconhelpbutton.setMinimumSize(QtCore.QSize(20, 23))
        self.rconhelpbutton.setMaximumSize(QtCore.QSize(20, 23))
        self.rconhelpbutton.setBaseSize(QtCore.QSize(0, 0))
        self.rconhelpbutton.setObjectName("rconhelpbutton")
        self.horizontalLayout.addWidget(self.rconhelpbutton)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(13, 212, 561, 281))
        self.scrollArea.setMinimumSize(QtCore.QSize(561, 281))
        self.scrollArea.setMaximumSize(QtCore.QSize(561, 281))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.terminalwindows = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.terminalwindows.setEnabled(True)
        self.terminalwindows.setMinimumSize(QtCore.QSize(559, 278))
        self.terminalwindows.setMaximumSize(QtCore.QSize(559, 5000))
        self.terminalwindows.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.terminalwindows.setStyleSheet("")
        self.terminalwindows.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.terminalwindows.setText("")
        self.terminalwindows.setPixmap(QtGui.QPixmap(".\\img/isrt-bck.png"))
        self.terminalwindows.setScaledContents(True)
        self.terminalwindows.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.terminalwindows.setWordWrap(True)
        self.terminalwindows.setObjectName("terminalwindows")
        self.verticalLayout_5.addWidget(self.terminalwindows)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 585, 21))
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
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionQuit)
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionINfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Insurgency Sandstorm RCON Tool - ISRT"))
        MainWindow.setStatusTip(_translate("MainWindow", "ISRT Insurgency Sandstorm RCON/Query Tool"))
        self.le_servername.setStatusTip(_translate("MainWindow", "Servername"))
        self.le_servername.setPlaceholderText(_translate("MainWindow", "Servername"))
        self.le_vac.setStatusTip(_translate("MainWindow", "VAC Secured"))
        self.le_vac.setPlaceholderText(_translate("MainWindow", "VAC Secured"))
        self.le_ranked.setStatusTip(_translate("MainWindow", "Ranked Server"))
        self.le_ranked.setPlaceholderText(_translate("MainWindow", "Ranked Server"))
        self.le_password.setStatusTip(_translate("MainWindow", "Passworded Server"))
        self.le_password.setPlaceholderText(_translate("MainWindow", "Passworded Server"))
        self.le_players.setStatusTip(_translate("MainWindow", "Players"))
        self.le_players.setPlaceholderText(_translate("MainWindow", "Players"))
        self.le_ping.setStatusTip(_translate("MainWindow", "Ping"))
        self.le_ping.setPlaceholderText(_translate("MainWindow", "Ping"))
        self.label_6.setText(_translate("MainWindow", "Gamemode:"))
        self.label_7.setText(_translate("MainWindow", "Servermode:"))
        self.label_8.setText(_translate("MainWindow", "IP + Port:"))
        self.label_9.setText(_translate("MainWindow", "Mods:"))
        self.label_10.setText(_translate("MainWindow", "Map:"))
        self.entryip.setStatusTip(_translate("MainWindow", "IP Address of the server"))
        self.entryip.setText(_translate("MainWindow", "93.186.198.185"))
        self.entryip.setPlaceholderText(_translate("MainWindow", "Query IP-Address"))
        self.entryqueryport.setStatusTip(_translate("MainWindow", "Query Port of the server"))
        self.entryqueryport.setText(_translate("MainWindow", "27016"))
        self.entryqueryport.setPlaceholderText(_translate("MainWindow", "Query Port"))
        self.submitbutton.setStatusTip(_translate("MainWindow", "Execute a query command to the defined server"))
        self.submitbutton.setText(_translate("MainWindow", "Query Server"))
        self.entryrconport.setStatusTip(_translate("MainWindow", "RCON Port of the server"))
        self.entryrconport.setText(_translate("MainWindow", "27017"))
        self.entryrconport.setPlaceholderText(_translate("MainWindow", "RCON Port"))
        self.entryrconpw.setStatusTip(_translate("MainWindow", "RCON Password of the server"))
        self.entryrconpw.setText(_translate("MainWindow", ""))
        self.entryrconpw.setPlaceholderText(_translate("MainWindow", "RCON Password"))
        self.rconsubmitbutton.setStatusTip(_translate("MainWindow", "Execute the below defined RCon command"))
        self.rconsubmitbutton.setText(_translate("MainWindow", "Submit RCON"))
        self.le_gamemode.setStatusTip(_translate("MainWindow", "Gamemode"))
        self.le_gamemode.setPlaceholderText(_translate("MainWindow", "Gamemode"))
        self.le_servermode.setStatusTip(_translate("MainWindow", "Servermode"))
        self.le_servermode.setPlaceholderText(_translate("MainWindow", "Servermode"))
        self.le_serverip_port.setStatusTip(_translate("MainWindow", "Server-IP+Port"))
        self.le_serverip_port.setPlaceholderText(_translate("MainWindow", "Server-IP + Gameport"))
        self.le_mods.setStatusTip(_translate("MainWindow", "Servermods"))
        self.le_mods.setPlaceholderText(_translate("MainWindow", "Mods"))
        self.le_map.setStatusTip(_translate("MainWindow", "Map"))
        self.le_map.setPlaceholderText(_translate("MainWindow", "Map"))
        self.label.setText(_translate("MainWindow", "VAC Secured:"))
        self.label_2.setText(_translate("MainWindow", "Ranked:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_4.setText(_translate("MainWindow", "Players:"))
        self.label_5.setText(_translate("MainWindow", "Ping:"))
        self.label_rconcommand.setStatusTip(_translate("MainWindow", "Enter RCon commands"))
        self.label_rconcommand.setText(_translate("MainWindow", "help"))
        self.label_rconcommand.setPlaceholderText(_translate("MainWindow", "RCon Command"))
        self.rconhelpbutton.setStatusTip(_translate("MainWindow", "Show RCON help and list available commands"))
        self.rconhelpbutton.setText(_translate("MainWindow", "?"))
        self.terminalwindows.setStatusTip(_translate("MainWindow", "ISRT - Insurgency Sandstorm RCON/Query Tool"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menu.setTitle(_translate("MainWindow", "?"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "File Menu"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionINfo.setText(_translate("MainWindow", "About"))
        self.actionINfo.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionHelp.setText(_translate("MainWindow", "Rcon Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help Menu"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
