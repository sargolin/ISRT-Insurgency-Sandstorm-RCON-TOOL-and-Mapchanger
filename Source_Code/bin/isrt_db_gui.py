# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\source_files\isrt_db_importer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_db_importer_gui(object):
    def setupUi(self, db_importer_gui):
        db_importer_gui.setObjectName("db_importer_gui")
        db_importer_gui.resize(600, 190)
        db_importer_gui.setMinimumSize(QtCore.QSize(600, 190))
        db_importer_gui.setMaximumSize(QtCore.QSize(690, 190))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        db_importer_gui.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(db_importer_gui)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(db_importer_gui)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(db_importer_gui)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(db_importer_gui)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_dbi_select_database = QtWidgets.QToolButton(db_importer_gui)
        self.btn_dbi_select_database.setMinimumSize(QtCore.QSize(135, 0))
        self.btn_dbi_select_database.setStyleSheet("background-color:rgb(228, 228, 228)\n"
"")
        self.btn_dbi_select_database.setObjectName("btn_dbi_select_database")
        self.horizontalLayout_2.addWidget(self.btn_dbi_select_database)
        self.label_dbi_selected_db = QtWidgets.QLabel(db_importer_gui)
        self.label_dbi_selected_db.setMinimumSize(QtCore.QSize(150, 0))
        self.label_dbi_selected_db.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_dbi_selected_db.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_dbi_selected_db.setObjectName("label_dbi_selected_db")
        self.horizontalLayout_2.addWidget(self.label_dbi_selected_db)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(db_importer_gui)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_dbi_import_database = QtWidgets.QPushButton(db_importer_gui)
        self.btn_dbi_import_database.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_dbi_import_database.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_dbi_import_database.setStyleSheet("background-color:rgb(228, 228, 228)\n"
"")
        self.btn_dbi_import_database.setObjectName("btn_dbi_import_database")
        self.horizontalLayout.addWidget(self.btn_dbi_import_database)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_dbg_close = QtWidgets.QPushButton(db_importer_gui)
        self.btn_dbg_close.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_dbg_close.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_dbg_close.setStyleSheet("background-color:rgb(228, 228, 228)\n"
"")
        self.btn_dbg_close.setObjectName("btn_dbg_close")
        self.horizontalLayout.addWidget(self.btn_dbg_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(db_importer_gui)
        QtCore.QMetaObject.connectSlotsByName(db_importer_gui)

    def retranslateUi(self, db_importer_gui):
        _translate = QtCore.QCoreApplication.translate
        db_importer_gui.setWindowTitle(_translate("db_importer_gui", "DB Importer"))
        self.label.setText(_translate("db_importer_gui", "This the first start of ISRT - if you have a database from oder versions, you can import the servers now. If you don\'t want to do that now, you can do that any time later in the Server Manager!"))
        self.label_2.setText(_translate("db_importer_gui", "Step 1 - Select DB (Look for the \"db\" folder in your old ISRT directory)"))
        self.btn_dbi_select_database.setText(_translate("db_importer_gui", "Browse for old Database"))
        self.label_dbi_selected_db.setText(_translate("db_importer_gui", "Selected DB File"))
        self.label_3.setText(_translate("db_importer_gui", "Step 2 - Start importing by hitting the \"Import DB\" Button)"))
        self.btn_dbi_import_database.setText(_translate("db_importer_gui", "Import DB"))
        self.btn_dbg_close.setText(_translate("db_importer_gui", "Close"))
import res_rc
