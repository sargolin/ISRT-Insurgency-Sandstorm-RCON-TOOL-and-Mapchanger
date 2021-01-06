from PyQt5 import QtCore, QtGui, QtWidgets
import sys, time

#################################################
def count_generator(start, end):
    starten = int(start)
    ende = int(end)
    for item in range(starten, ende):
        yield item

#################################################
class Worker(QtCore.QObject):
    counted = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot(str, str)
    def start_counter(self, start, zahlend):
        running_counter = count_generator(start, zahlend)
        
        for counter in running_counter:
            adopted_zahl = counter * 10
            self.counted.emit(str(adopted_zahl))

#################################################
class MainWindow(QtWidgets.QMainWindow):

    counter_requested = QtCore.pyqtSignal(str, str)

    def setupUi(self, Form):
        # super().__init__()
        Form.setObjectName("Test")
        Form.resize(640, 480)
        self.create_layout()
    def create_layout(self):
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
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.setText("Go!")
        self.pushButton.clicked.connect(self.setzahl)
        self.lineEdit.returnPressed.connect(self.setzahl)

        # Create a worker object and a thread
        self.worker = Worker()
        self.worker_thread = QtCore.QThread()
        self.worker.counted.connect(self.add_counter_to_table)
        self.counter_requested.connect(self.worker.start_counter)
        # Assign the worker to the thread and start the thread
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

    #################################################
    def add_counter_to_table(self, adopted_zahl):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(adopted_zahl))
        print(adopted_zahl)

    #################################################
    #Button called diese Funktion
    def setzahl(self):
        zahl = int(self.lineEdit.text())
        start = 1
        ende = zahl
        self.counter_requested.emit(str(start), str(ende))
#############################################################



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
