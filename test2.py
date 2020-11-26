# runs with Python 2.7 and PyQt4
from PyQt5 import QtGui, QtCore
import sys


class App(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setMinimumSize(600,200)

        self.all_data = [["John", True, "01234", 24],
                         ["Joe", False, "05671", 13],
                         ["Johnna", True, "07145", 44] ]

        self.mainbox = QtGui.QWidget(self)
        self.layout = QtGui.QVBoxLayout()
        self.mainbox.setLayout(self.layout)
        self.setCentralWidget(self.mainbox)

        self.table = QtGui.QTableWidget(self)
        self.layout.addWidget(self.table)

        self.button = QtGui.QPushButton('Update',self)
        self.layout.addWidget(self.button)

        self.click_btn_printouts()
        self.button.clicked.connect(self.update)

    def click_btn_printouts(self):

        self.table.setRowCount(len(self.all_data))
        self.tableFields = ["Name", "isSomething", "someProperty", "someNumber"]
        self.table.setColumnCount(len(self.tableFields))
        self.table.setHorizontalHeaderLabels(self.tableFields)
        self.checkbox_list = []
        for i, self.item in enumerate(self.all_data):
            FullName = QtGui.QTableWidgetItem(str(self.item[0]))
            FullName.setFlags(FullName.flags() & ~QtCore.Qt.ItemIsEditable)
            PreviouslyMailed = QtGui.QTableWidgetItem(str(self.item[1]))
            LearnersDate = QtGui.QTableWidgetItem(str(self.item[2]))
            RestrictedDate = QtGui.QTableWidgetItem(str(self.item[3]))

            self.table.setItem(i, 0, FullName)
            self.table.setItem(i, 1, PreviouslyMailed)
            self.table.setItem(i, 2, LearnersDate)
            self.table.setItem(i, 3, RestrictedDate)

        self.changed_items = []
        self.table.itemChanged.connect(self.log_change)

    def log_change(self, item):
        self.table.blockSignals(True)
        item.setBackgroundColor(QtGui.QColor("red"))
        self.table.blockSignals(False)
        self.changed_items.append(item)
        print(item.text(), item.column(), item.row())

    def update(self):
        print("Updating ")
        for item in self.changed_items:
            self.table.blockSignals(True)
            item.setBackgroundColor(QtGui.QColor("white"))
            self.table.blockSignals(False)
            self.writeToDatabase(item)

    def writeToDatabase(self, item):
        text, col, row = item.text(), item.column(), item.row()
        #write those to database with your own code


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    thisapp = App()
    thisapp.show()
    sys.exit(app.exec_())