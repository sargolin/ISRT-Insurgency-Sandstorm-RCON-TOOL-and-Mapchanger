import sys
import sqlite3
from pathlib import Path
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer, Qt
from bin.isrt_monitor_gui import Ui_UI_Server_Monitor
import bin.MonitorQuery as sq

class Worker(QObject):
    starter = pyqtSignal()
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    server_queried = pyqtSignal(dict, dict, str, int, int)
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
            try:
                server_info = sq.SourceQuery(serverhost, queryport)
                server_info.disconnect()
                info = server_info.get_info()
                rules = server_info.get_rules()
                online = 1
                self.progress.emit(progress_value)
                self.server_queried.emit(info, rules, serverhost, counter, online)
            except Exception:
                online = 0
                info = {}
                rules = {}
                self.server_queried.emit(info, rules, serverhost, counter, online)
            counter = counter + 1
            progress_value = progress_value + progress_multiplier
        progress_value = 100
        self.progress.emit(progress_value)
        self.finished.emit()


class mongui(QtWidgets.QWidget):
    server_query_requested = pyqtSignal(int, list)
    timer_requested = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()
        self.mogui = Ui_UI_Server_Monitor()
        self.mogui.setupUi(self)
        self.mogui.mon_progress_bar.setValue(0)
        self.mogui.tbl_server_overview.setRowCount(0)
        self.mogui.tbl_server_overview.setColumnWidth(0, 250)
        self.mogui.tbl_server_overview.setColumnWidth(1, 130)
        self.mogui.tbl_server_overview.setColumnWidth(2, 130)
        self.mogui.tbl_server_overview.setColumnWidth(3, 150)
        self.mogui.tbl_server_overview.setColumnWidth(4, 50)
        self.mogui.tbl_server_overview.setColumnWidth(5, 74)
        self.mogui.tbl_server_overview.setStyleSheet("padding: 3px;")
        self.mogui.tbl_server_overview.setColumnWidth(6, 50)
        
        self.c.execute("SELECT alias FROM server")
        self.conn.commit()
        for row, form in enumerate(self.c):
            row = row + 1
            self.mogui.tbl_server_overview.insertRow(row)
            for column, item in enumerate(form):
                self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
        self.server_alias_list = self.c.fetchall()
        self.start_timer()

    def start_timer(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_server_data)
        self.timer.start(30000)
        self.get_server_data()

    def get_server_data(self):
        self.mogui.mon_progress_bar.setValue(0)
        self.c.execute("SELECT alias FROM server")
        self.server_alias_checklist = self.c.fetchall()
        self.conn.commit()
        if self.server_alias_list != self.server_alias_checklist:
            self.mogui.tbl_server_overview.setRowCount(1)
            self.c.execute("SELECT alias FROM server")
            self.conn.commit()
            for row, form in enumerate(self.c):
                #row = row +1
                self.mogui.tbl_server_overview.insertRow(row)
                for column, item in enumerate(form):
                    self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
            self.mogui.mon_progress_bar.setValue(0)
            self.server_alias_list = self.server_alias_checklist
        self.c.execute("SELECT alias FROM server")
        self.server_alias_checklist = self.c.fetchall()
        self.conn.commit()
        self.alias_list = []
        for server_alias in self.server_alias_checklist:
            value_temp = server_alias[0]
            self.alias_list.append(value_temp)
        rowcount = (self.mogui.tbl_server_overview.rowCount() - 2)
        self.prepare_list_query(self.alias_list, rowcount)

    def reportProgress(self, n):
        if self.mogui.chkbx_show_progressbar.isChecked():
            self.mogui.mon_progress_bar.setValue(n)
            # if n == 100:
            #     self.timeout = QTimer()
            #     self.timeout.timeout.connect(lambda: self.mogui.mon_progress_bar.setValue(0))
            #     self.timeout.start(1000)

        else:
            self.mogui.mon_progress_bar.setValue(0)
        

    def prepare_list_query(self, alias_list, rowcount):
        self.alias_list = alias_list
        self.rowcount = rowcount
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.start_querying)
        self.server_query_requested.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.progress.connect(self.reportProgress)
        self.worker.server_queried.connect(self.add_data_to_table)
        self.thread.start()

    def start_querying(self):
        self.server_query_requested.emit(self.rowcount, self.alias_list)

    def add_data_to_table(self, n, m, o, p, q):
        self.serverhost = o
        #self.counter = p + 1
        self.counter = p
        self.resrules = m
        self.resinfo = n
        self.online = q
        if self.online == 1:
            lighting_val = self.resrules['Day_b']
            if lighting_val == "true":
                lighting = "Day"
            else:
                lighting = "Night"
            self.mogui.tbl_server_overview.setItem(self.counter, 1, QtWidgets.QTableWidgetItem(self.serverhost +":" + str(self.resinfo['GamePort'])))
            item1 = QtWidgets.QTableWidgetItem(self.resinfo['Map'] + " (" + lighting + ")")
            item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.mogui.tbl_server_overview.setItem(self.counter, 3, item1)
            if self.resinfo['Players'] == 0:
                item2 = QtWidgets.QTableWidgetItem("%i/%i" % (self.resinfo['Players'], self.resinfo['MaxPlayers']))
                item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.mogui.tbl_server_overview.setItem(self.counter, 4, item2)
            else:
                item2 = QtWidgets.QTableWidgetItem("%i/%i" % (self.resinfo['Players'], self.resinfo['MaxPlayers']))
                item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                item2.setFont(QtGui.QFont("MS Shell Dlg 2",weight=QtGui.QFont.Bold))
                self.mogui.tbl_server_overview.setItem(self.counter, 4, item2)
            
            imagelabel = QtWidgets.QLabel()
            imagelabel.setText("")
            imagelabel.setScaledContents(True)
            pixmap = QtGui.QPixmap(":/img/img/online.png")
            picmain = pixmap
            imagelabel.setPixmap(picmain)
            self.mogui.tbl_server_overview.setCellWidget(self.counter, 5, imagelabel)
            
            item4 = QtWidgets.QTableWidgetItem(str(self.resinfo['Ping']) + "ms")
            if self.resinfo['Ping'] >= 80:
                item4 = QtWidgets.QTableWidgetItem(str(self.resinfo['Ping']) + "ms")
                item4.setForeground(QtGui.QColor(190,0,0))
            else:
                item4.setForeground(QtGui.QColor(0,150,0))
            
            item4.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.mogui.tbl_server_overview.setItem(self.counter, 6, item4)
            
            item5 = QtWidgets.QTableWidgetItem(self.resrules['GameMode_s'])
            item5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.mogui.tbl_server_overview.setItem(self.counter, 2, item5)
            
        else:
            self.mogui.tbl_server_overview.setItem(self.counter, 1, QtWidgets.QTableWidgetItem(self.serverhost))
            imagelabel2 = QtWidgets.QLabel()
            imagelabel2.setText("")
            imagelabel2.setScaledContents(True)
            pixmap2 = QtGui.QPixmap(":/img/img/offline.png")
            picmain2 = pixmap2
            imagelabel2.setPixmap(picmain2)
            self.mogui.tbl_server_overview.setCellWidget(self.counter, 5, imagelabel2)

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