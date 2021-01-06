from PyQt5 import QtCore, QtGui, QtWidgets

def count_generator(end):
        for item in range(0, end):
            yield item


class Worker(QtCore.QObject):
    counted = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot(str)
    def start_counter(self, zahlend):
        hash_gen = count_generator(zahl)
        for path, sha1_hash in hash_gen:
            self.hashed.emit(path, sha1_hash)

class MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, Form):
        Form.setObjectName("Test")
        Form.resize(640, 480)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.setText("Go!")
        self.pushButton.clicked.connect(self.setzahl)

    def setzahl(self):
        zahl = int(self.lineEdit.text())
        resulting_generator = count_generator(zahl)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
