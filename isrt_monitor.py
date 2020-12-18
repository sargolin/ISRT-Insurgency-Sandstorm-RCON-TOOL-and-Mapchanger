from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess
import sys, sqlite3, threading, time
from pathlib import Path
from bin.isrt_monitor_gui import Ui_UI_Server_Monitor
import bin.SourceQuery2 as sq

class mongui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        #Gui Setup
        super().__init__(*args, **kwargs)
        self.mogui = Ui_UI_Server_Monitor()
        self.mogui.setupUi(self)
        #Define Refresh Button
        self.mogui.btn_exec_overview_refresh.clicked.connect(self.get_server_data)
        #Database connection setup
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()
        #Define Method Calls to execute on script call
        self.fill_overview_headers()

        
    #Fill Alias in the Server Overview
    def fill_overview_headers(self):
        self.mogui.tbl_server_overview.setRowCount(0)
        self.mogui.tbl_server_overview.insertRow(0)
        self.mogui.tbl_server_overview.setItem(0, 0, QtWidgets.QTableWidgetItem("Alias"))
        self.mogui.tbl_server_overview.item(0, 0).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setItem(0, 1, QtWidgets.QTableWidgetItem("IP-Address:Port"))
        self.mogui.tbl_server_overview.item(0, 1).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setItem(0, 2, QtWidgets.QTableWidgetItem("GameMode"))
        self.mogui.tbl_server_overview.item(0, 2).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setItem(0, 3, QtWidgets.QTableWidgetItem("Status"))
        self.mogui.tbl_server_overview.item(0, 3).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setItem(0, 4, QtWidgets.QTableWidgetItem("Ping"))
        self.mogui.tbl_server_overview.item(0, 4).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setItem(0, 5, QtWidgets.QTableWidgetItem("Map"))
        self.mogui.tbl_server_overview.item(0, 5).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setItem(0, 6, QtWidgets.QTableWidgetItem("Players"))
        self.mogui.tbl_server_overview.item(0, 6).setBackground(QtGui.QColor(254,254,254))
        QtCore.QTimer.singleShot(10, self.get_aliases)
        

    def get_aliases(self):
        def execute(self):
            #Execute DB query
            self.c.execute("SELECT alias FROM server")
            self.conn.commit()
            
            for row, form in enumerate(self.c):
                row = row + 1
                self.mogui.tbl_server_overview.insertRow(row)
                for column, item in enumerate(form):
                    self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
        # QtCore.QTimer.singleShot(10, self.get_server_data)

        self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
        self.p.start("python3", ['execute'])


    def get_server_data(self):
      
        def executor(alias, host, qport):
            try:
                self.server_info = sq.SourceQuery(host, qport)
                resinfo = self.server_info.get_info()
                resrules = self.server_info.get_rules()
                self.server_info.disconnect()
                if resinfo:
                    self.mogui.tbl_server_overview.setItem(i, 1, QtWidgets.QTableWidgetItem(host +":" + str(resinfo['GamePort'])))
                    self.mogui.tbl_server_overview.setItem(i, 5, QtWidgets.QTableWidgetItem(resinfo['Map']))
                    self.mogui.tbl_server_overview.setItem(i, 6, QtWidgets.QTableWidgetItem("%i/%i" % (resinfo['Players'], resinfo['MaxPlayers'])))
                    self.mogui.tbl_server_overview.setItem(i, 3, QtWidgets.QTableWidgetItem("Online"))
                    self.mogui.tbl_server_overview.item(i, 3).setBackground(QtGui.QColor(0,254,0))
                    self.mogui.tbl_server_overview.setItem(i, 4, QtWidgets.QTableWidgetItem(str(resinfo['Ping']) + "ms"))
                    self.mogui.tbl_server_overview.setItem(i, 2, QtWidgets.QTableWidgetItem(resrules['GameMode_s']))
                    if resinfo['Ping'] >= 80:
                        self.mogui.tbl_server_overview.item(i, 4).setBackground(QtGui.QColor(254,85,0))
                    else:
                        self.mogui.tbl_server_overview.item(i, 4).setBackground(QtGui.QColor(0,254,0))
                else:
                    self.mogui.tbl_server_overview.setItem(i, 3, QtWidgets.QTableWidgetItem("Offline"))
                    self.mogui.tbl_server_overview.item(i, 3).setBackground(QtGui.QColor(254,0,0))

            except Exception:
                print(f"Error on {alias}")
                self.mogui.tbl_server_overview.setItem(i, 3, QtWidgets.QTableWidgetItem("Offline"))
                self.mogui.tbl_server_overview.item(i, 3).setBackground(QtGui.QColor(254,0,0))
                self.server_info.disconnect()
            


        #rowcount = self.mogui.tbl_server_overview.rowCount()
        i = 1 
        
        while i <= 4:
            server_temp_alias = (self.mogui.tbl_server_overview.item(i,0)).text()
            self.c.execute("SELECT ipaddress FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
            monmap_ip = self.c.fetchone()
            self.c.execute("SELECT queryport FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
            monmap_qp = self.c.fetchone()
            self.conn.commit()
            serverhost = monmap_ip[0]
            queryport = monmap_qp[0]
            threadnumber = ("t" + str(i))
            threadnumber =  threading.Thread(target=(executor(server_temp_alias, serverhost, queryport)))
            threadnumber.start()
            i = i + 1
            
            


            


    def refresh_monitor(self):
        self.fill_server_overview()

    def closeEvent(self, event):
        self.close() 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    UI_Server_Monitor = QtWidgets.QWidget()
    ui = Ui_UI_Server_Monitor()
    mogui = mongui()
    mogui.show()
    sys.exit(app.exec_())