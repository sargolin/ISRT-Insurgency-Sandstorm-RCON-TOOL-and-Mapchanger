import sys
import sqlite3
from pathlib import Path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from bin.isrt_monitor_gui import Ui_UI_Server_Monitor
import bin.MonitorQuery as sq

class Worker(QObject):
    starter = pyqtSignal()
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    #server_queried = pyqtSignal(str, str)
    #server_unreachable = pyqtSignal(str)
    def run(self, rowcount, alias_list):
        self.starter.emit()
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()
        counter = 0
        progress_multiplier = int(100/rowcount)
        progress_value = int(progress_multiplier) + int(progress_multiplier)
        while counter <= rowcount:
            server_temp_alias = alias_list[counter]
            self.c.execute("SELECT ipaddress, queryport FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
            monmap_ip = self.c.fetchone()
            self.conn.commit()
            serverhost = monmap_ip[0]
            queryport = monmap_ip[1]
            print(serverhost, queryport)
            try:
                server_info = sq.SourceQuery(serverhost, queryport)
                server_info.disconnect()
                print(server_info.get_info())
                # self.server_queried.emit(server_info.get_info(), server_info.get_rules())
            except Exception:
                print("Error")
                #self.server_unreachable.emit("Offline")
            counter = counter + 1
            progress_value = progress_value + progress_multiplier
        self.finished.emit()


class mongui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        #Gui Setup
        super().__init__(*args, **kwargs)
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()
        self.mogui = Ui_UI_Server_Monitor()
        self.mogui.setupUi(self)
        self.mogui.mon_progress_bar.setValue(0)
        self.mogui.btn_exec_overview_refresh.clicked.connect(self.get_server_data)
        self.mogui.tbl_server_overview.setRowCount(0)
        self.mogui.tbl_server_overview.insertRow(0)
        self.mogui.tbl_server_overview.setColumnWidth(0, 260)
        self.mogui.tbl_server_overview.setItem(0, 0, QtWidgets.QTableWidgetItem("Server Alias"))
        self.mogui.tbl_server_overview.item(0, 0).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(1, 140)
        self.mogui.tbl_server_overview.setItem(0, 1, QtWidgets.QTableWidgetItem("IP-Address:Port"))
        self.mogui.tbl_server_overview.item(0, 1).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(2, 140)
        self.mogui.tbl_server_overview.setItem(0, 2, QtWidgets.QTableWidgetItem("GameMode"))
        self.mogui.tbl_server_overview.item(0, 2).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(3, 50)
        self.mogui.tbl_server_overview.setItem(0, 3, QtWidgets.QTableWidgetItem("Status"))
        self.mogui.tbl_server_overview.item(0, 3).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(4, 50)
        self.mogui.tbl_server_overview.setItem(0, 4, QtWidgets.QTableWidgetItem("Ping"))
        self.mogui.tbl_server_overview.item(0, 4).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(5, 140)
        self.mogui.tbl_server_overview.setItem(0, 5, QtWidgets.QTableWidgetItem("Map"))
        self.mogui.tbl_server_overview.item(0, 5).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(6, 40)
        self.mogui.tbl_server_overview.setItem(0, 6, QtWidgets.QTableWidgetItem("Players"))
        self.mogui.tbl_server_overview.item(0, 6).setBackground(QtGui.QColor(254,254,254))
        self.c.execute("SELECT alias FROM server")
        self.conn.commit()
        for row, form in enumerate(self.c):
            row = row + 1
            self.mogui.tbl_server_overview.insertRow(row)
            for column, item in enumerate(form):
                self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
        self.server_alias_list = self.c.fetchall()

    def get_server_data(self):
        self.mogui.mon_progress_bar.setValue(0)
        self.mogui.btn_exec_overview_refresh.setEnabled(False)
        self.c.execute("SELECT alias FROM server")
        self.server_alias_checklist = self.c.fetchall()
        self.conn.commit()
        if self.server_alias_list != self.server_alias_checklist:
            self.mogui.tbl_server_overview.setRowCount(1)
            self.c.execute("SELECT alias FROM server")
            self.conn.commit()
            for row, form in enumerate(self.c):
                row = row + 1
                self.mogui.tbl_server_overview.insertRow(row)
                for column, item in enumerate(form):
                    self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
            self.mogui.mon_progress_bar.setValue(0)
            self.server_alias_list = self.server_alias_checklist
        self.prepare_list_query()

    def reportProgress(self, n):
        self.mogui.mon_progress_bar.setValue(n)

    def prepare_list_query(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.c.execute("SELECT alias FROM server")
        self.server_alias_checklist = self.c.fetchall()
        self.conn.commit()
        self.alias_list = []
        for server_alias in self.server_alias_checklist:
            value_temp = server_alias[0]
            self.alias_list.append(value_temp)
        
        rowcount = (self.mogui.tbl_server_overview.rowCount() - 2)
        self.thread.started.connect(lambda: self.worker.run(rowcount, self.alias_list))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        # self.worker.server_queried.connect(self.add_)
        
        self.thread.start()

        self.thread.finished.connect(lambda: self.mogui.btn_exec_overview_refresh.setEnabled(True))

    # def add_data_to_table(self):

    #     self.serverhost = serverhost
    #     self.counter = counter
    #     self.resrules = resrules
    #     self.resinfo = resinfo
    #     lighting_val = self.resrules['Day_b']
    #     if lighting_val == "true":
    #         lighting = "Day"
    #     else:
    #         lighting = "Night"
    #     if self.resinfo:
    #         self.mogui.tbl_server_overview.setItem(self.counter, 1, QtWidgets.QTableWidgetItem(self.serverhost +":" + str(self.resinfo['GamePort'])))
    #         self.mogui.tbl_server_overview.setItem(self.counter, 5, QtWidgets.QTableWidgetItem(self.resinfo['Map'] + " (" + lighting + ")"))
    #         self.mogui.tbl_server_overview.setItem(self.counter, 6, QtWidgets.QTableWidgetItem("%i/%i" % (self.resinfo['Players'], self.resinfo['MaxPlayers'])))
    #         self.mogui.tbl_server_overview.setItem(self.counter, 3, QtWidgets.QTableWidgetItem("Online"))
    #         self.mogui.tbl_server_overview.item(self.counter, 3).setBackground(QtGui.QColor(0,254,0))
    #         self.mogui.tbl_server_overview.setItem(self.counter, 4, QtWidgets.QTableWidgetItem(str(self.resinfo['Ping']) + "ms"))
    #         self.mogui.tbl_server_overview.setItem(self.counter, 2, QtWidgets.QTableWidgetItem(self.resrules['GameMode_s']))
    #         if self.resinfo['Ping'] >= 80:
    #             self.mogui.tbl_server_overview.item(self.counter, 4).setBackground(QtGui.QColor(254,85,0))
    #         else:
    #             self.mogui.tbl_server_overview.item(self.counter, 4).setBackground(QtGui.QColor(0,254,0))
    #     else:
    #         self.mogui.tbl_server_overview.setItem(self.counter, 3, QtWidgets.QTableWidgetItem("Offline"))
    #         self.mogui.tbl_server_overview.item(self.counter, 3).setBackground(QtGui.QColor(254,0,0))

    def closeEvent(self, event):
        self.conn.close()
        self.close() 

#Main definitions
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UI_Server_Monitor = QtWidgets.QWidget()
    ui = Ui_UI_Server_Monitor()
    mogui = mongui()
    mogui.show()
    sys.exit(app.exec_())