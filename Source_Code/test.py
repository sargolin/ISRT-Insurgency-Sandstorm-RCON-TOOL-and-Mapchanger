import sys
from PyQt5 import QtCore, QtWidgets as qtw



#################################################
def count_generator(end):
    starten = 1
    ende = int(end)

    # for i in range(starten, ende):
    #     result = i * 10
    #     yield (result)

    while starten != ende:
        result = starten * 10
        starten += 1
        yield result
    else:
        yield ("Results not available")

#################################################
class Worker(QtCore.QObject):
    counted = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot(str)
    def start_counter(self, zahlend):
        running_counter = count_generator(zahlend)
        #for counter in running_counter:
        for result in running_counter:
            self.counted.emit(str(result))

#################################################
class MainWindow(qtw.QMainWindow):

    counter_requested = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        form = qtw.QWidget()
        self.setCentralWidget(form)
        layout = qtw.QFormLayout()
        form.setLayout(layout)
        self.file_root = qtw.QLineEdit(returnPressed=self.setzahl)
        self.go_button = qtw.QPushButton('Start Counting', clicked=self.setzahl)
        self.results = qtw.QTableWidget(0, 1)
        self.results.setHorizontalHeaderLabels(['Result'])
        self.results.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self.results.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        layout.addRow(qtw.QLabel('Counter'))
        layout.addRow('End Zahl', self.file_root)
        layout.addRow('', self.go_button)
        layout.addRow(self.results)

        # Create a worker object and a thread
        self.worker = Worker()
        self.worker_thread = QtCore.QThread()
        self.worker.counted.connect(self.add_counter_to_table)
        self.counter_requested.connect(self.worker.start_counter)
        # Assign the worker to the thread and start the thread
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        self.show()

    #################################################
    def add_counter_to_table(self, adopted_zahl):
        row = self.results.rowCount()
        self.results.insertRow(row)
        self.results.setItem(row, 0, qtw.QTableWidgetItem(adopted_zahl))
        print(adopted_zahl)

    #################################################
    #Button called diese Funktion
    def setzahl(self):
        zahl = int(self.file_root.text())

        ende = zahl
        self.counter_requested.emit(str(ende))
#############################################################



if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    mw = MainWindow()
    # ui.setupUi(Form)
    # Form.show()
    sys.exit(app.exec_())
