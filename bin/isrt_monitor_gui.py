from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UI_Server_Monitor(object):
    def setupUi(self, UI_Server_Monitor):
        UI_Server_Monitor.setObjectName("UI_Server_Monitor")
        UI_Server_Monitor.resize(911, 760)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UI_Server_Monitor.setWindowIcon(icon)
        UI_Server_Monitor.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"selection-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(216, 216, 216);")
        self.verticalLayout = QtWidgets.QVBoxLayout(UI_Server_Monitor)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_exec_overview_refresh = QtWidgets.QPushButton(UI_Server_Monitor)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exec_overview_refresh.setFont(font)
        self.btn_exec_overview_refresh.setAutoDefault(False)
        self.btn_exec_overview_refresh.setDefault(False)
        self.btn_exec_overview_refresh.setFlat(False)
        self.btn_exec_overview_refresh.setObjectName("btn_exec_overview_refresh")
        self.verticalLayout.addWidget(self.btn_exec_overview_refresh)
        self.tbl_server_overview = QtWidgets.QTableWidget(UI_Server_Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbl_server_overview.sizePolicy().hasHeightForWidth())
        self.tbl_server_overview.setSizePolicy(sizePolicy)
        self.tbl_server_overview.setMinimumSize(QtCore.QSize(900, 600))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tbl_server_overview.setFont(font)
        self.tbl_server_overview.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.tbl_server_overview.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tbl_server_overview.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tbl_server_overview.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tbl_server_overview.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tbl_server_overview.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tbl_server_overview.setAlternatingRowColors(True)
        self.tbl_server_overview.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_server_overview.setTextElideMode(QtCore.Qt.ElideNone)
        self.tbl_server_overview.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tbl_server_overview.setObjectName("tbl_server_overview")
        self.tbl_server_overview.setColumnCount(7)
        self.tbl_server_overview.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_server_overview.setHorizontalHeaderItem(6, item)
        self.tbl_server_overview.horizontalHeader().setVisible(False)
        self.tbl_server_overview.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_server_overview.horizontalHeader().setDefaultSectionSize(130)
        self.tbl_server_overview.horizontalHeader().setMinimumSectionSize(130)
        self.tbl_server_overview.horizontalHeader().setSortIndicatorShown(True)
        self.tbl_server_overview.horizontalHeader().setStretchLastSection(True)
        self.tbl_server_overview.verticalHeader().setVisible(False)
        self.tbl_server_overview.verticalHeader().setDefaultSectionSize(23)
        self.tbl_server_overview.verticalHeader().setMinimumSectionSize(15)
        self.tbl_server_overview.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tbl_server_overview)

        self.retranslateUi(UI_Server_Monitor)
        QtCore.QMetaObject.connectSlotsByName(UI_Server_Monitor)

    def retranslateUi(self, UI_Server_Monitor):
        _translate = QtCore.QCoreApplication.translate
        UI_Server_Monitor.setWindowTitle(_translate("UI_Server_Monitor", "ISRT Server Monitor"))
        self.btn_exec_overview_refresh.setText(_translate("UI_Server_Monitor", "Refresh Overview"))
        item = self.tbl_server_overview.horizontalHeaderItem(0)
        item.setText(_translate("UI_Server_Monitor", "Alias"))
        item = self.tbl_server_overview.horizontalHeaderItem(1)
        item.setText(_translate("UI_Server_Monitor", "IP-Address-Port"))
        item = self.tbl_server_overview.horizontalHeaderItem(2)
        item.setText(_translate("UI_Server_Monitor", "GameMode"))
        item = self.tbl_server_overview.horizontalHeaderItem(3)
        item.setText(_translate("UI_Server_Monitor", "Status"))
        item = self.tbl_server_overview.horizontalHeaderItem(4)
        item.setText(_translate("UI_Server_Monitor", "Ping"))
        item = self.tbl_server_overview.horizontalHeaderItem(5)
        item.setText(_translate("UI_Server_Monitor", "Map"))
        item = self.tbl_server_overview.horizontalHeaderItem(6)
        item.setText(_translate("UI_Server_Monitor", "Players"))
#import res_rc


