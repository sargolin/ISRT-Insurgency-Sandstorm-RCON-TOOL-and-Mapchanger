from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from isrt_monitor_gui import Ui_UI_Server_Monitor

class mongui(QtWidgets.QWidget):
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        UI_Server_Monitor = QtWidgets.QWidget()
        ui = Ui_UI_Server_Monitor()
        ui.setupUi(UI_Server_Monitor)
        UI_Server_Monitor.show()
        sys.exit(app.exec_())

    #Fill the Server Overview
    def fill_server_overview(self):
        self.c.execute("SELECT * FROM server")
        self.gui.tbl_server_overview.setRowCount(0)
        self.conn.commit()
        
        for row, form in enumerate(self.c):
            self.gui.tbl_server_overview.insertRow(row)
            for column, item in enumerate(form):
                self.gui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))  

        self.gui.tbl_server_overview.insertRow(0)
        self.gui.tbl_server_overview.setItem(0, 0, QtWidgets.QTableWidgetItem("Alias"))
        self.gui.tbl_server_overview.setItem(0, 1, QtWidgets.QTableWidgetItem("IP-Address/Port"))
        self.gui.tbl_server_overview.setItem(0, 2, QtWidgets.QTableWidgetItem("Online"))
        self.gui.tbl_server_overview.setItem(0, 3, QtWidgets.QTableWidgetItem("Map"))
        self.gui.tbl_server_overview.setItem(0, 4, QtWidgets.QTableWidgetItem("Players"))

    def refresh_monitor(self):
        pass

    def closeEvent(self, event):
        self.close() 
