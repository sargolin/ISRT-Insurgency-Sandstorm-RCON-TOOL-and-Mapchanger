# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\about_gui_v0.4.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(360, 267)
        font = QtGui.QFont()
        font.setPointSize(10)
        about_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\img/isrt.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about_window.setWindowIcon(icon)
        self.aboutbody = QtWidgets.QLabel(about_window)
        self.aboutbody.setGeometry(QtCore.QRect(20, 10, 321, 191))
        self.aboutbody.setObjectName("aboutbody")
        self.btn_about_close = QtWidgets.QPushButton(about_window)
        self.btn_about_close.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.btn_about_close.setObjectName("btn_about_close")

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "About ISRT"))
        self.aboutbody.setText(_translate("about_window", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ISRT v0.4.2</span></p><p align=\"center\">Insurgency Sandstorm RCON/Query Tool</p><p align=\"center\">Created by Madman</p><p align=\"center\">Support: <a href=\"mailto:isrt@edelmeier.org\"><span style=\" text-decoration: underline; color:#0000ff;\">isrt@edelmeier.org</span></a></p><p align=\"center\"><a href=\"https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-TOOL-and-Mapchanger\"><span style=\" text-decoration: underline; color:#0000ff;\">GitHub</span></a></p><p align=\"center\">GNU/Public License Software </p></body></html>"))
        self.btn_about_close.setText(_translate("about_window", "Close"))
