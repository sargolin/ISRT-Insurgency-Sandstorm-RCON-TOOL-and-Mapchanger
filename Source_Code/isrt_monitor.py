from PyQt5 import QtCore, QtGui, QtWidgets
import sys, sqlite3, time
from pathlib import Path
from bin.isrt_monitor_gui import Ui_UI_Server_Monitor
import bin.MonitorQuery as sq

#Prepare Main GUI of Server Monitor
class mongui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        #Gui Setup
        super().__init__(*args, **kwargs)
        self.mogui = Ui_UI_Server_Monitor()
        self.mogui.setupUi(self)
        #Define Method Calls to execute on script call
        self.fill_overview_headers()
        self.get_aliases()
        self.mogui.mon_progress_bar.setValue(0)
        #Define Refresh Button
        self.mogui.btn_exec_overview_refresh.clicked.connect(self.get_server_data)
    #Create Row 0 and Headers
    def fill_overview_headers(self):
        self.mogui.tbl_server_overview.setRowCount(0)
        self.mogui.tbl_server_overview.insertRow(0)
        self.mogui.tbl_server_overview.setColumnWidth(0, 200)
        self.mogui.tbl_server_overview.setItem(0, 0, QtWidgets.QTableWidgetItem("Server Alias"))
        self.mogui.tbl_server_overview.item(0, 0).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(1, 140)
        self.mogui.tbl_server_overview.setItem(0, 1, QtWidgets.QTableWidgetItem("IP-Address:Port"))
        self.mogui.tbl_server_overview.item(0, 1).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(2, 140)
        self.mogui.tbl_server_overview.setItem(0, 2, QtWidgets.QTableWidgetItem("GameMode"))
        self.mogui.tbl_server_overview.item(0, 2).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(3, 80)
        self.mogui.tbl_server_overview.setItem(0, 3, QtWidgets.QTableWidgetItem("Status"))
        self.mogui.tbl_server_overview.item(0, 3).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(4, 80)
        self.mogui.tbl_server_overview.setItem(0, 4, QtWidgets.QTableWidgetItem("Ping"))
        self.mogui.tbl_server_overview.item(0, 4).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(5, 140)
        self.mogui.tbl_server_overview.setItem(0, 5, QtWidgets.QTableWidgetItem("Map"))
        self.mogui.tbl_server_overview.item(0, 5).setBackground(QtGui.QColor(254,254,254))
        self.mogui.tbl_server_overview.setColumnWidth(6, 40)
        self.mogui.tbl_server_overview.setItem(0, 6, QtWidgets.QTableWidgetItem("Players"))
        self.mogui.tbl_server_overview.item(0, 6).setBackground(QtGui.QColor(254,254,254))
    #Get Headers from DB and fill in Row 0
    def get_aliases(self):
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()
        self.c.execute("SELECT alias FROM server")
        self.conn.commit()
        for row, form in enumerate(self.c):
            row = row + 1
            self.mogui.tbl_server_overview.insertRow(row)
            for column, item in enumerate(form):
                self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))
        self.mogui.mon_progress_bar.setValue(0)
        self.c.execute("SELECT alias FROM server")
        self.conn.commit()
        self.server_alias_list = self.c.fetchall()
        self.conn.close()
    #Query Servers from Aliases and push data into table
    def get_server_data(self):
        #Database startup
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()
        self.c.execute("SELECT alias FROM server")
        self.conn.commit()
        self.server_alias_checklist = self.c.fetchall()
        #check if anything changed in the server manager
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
        else:
            pass
        #Define Executor for polling the Servrs
        def execute_list_query(self):
            rowcount = self.mogui.tbl_server_overview.rowCount()
            i = 1
            progress_multiplier = int(100/rowcount)
            progress_value = int(progress_multiplier) + int(progress_multiplier)
            while i <= (rowcount - 1):
                self.mogui.mon_progress_bar.setValue(progress_value)
                server_temp_alias = (self.mogui.tbl_server_overview.item(i,0)).text()
                self.c.execute("SELECT ipaddress FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
                monmap_ip = self.c.fetchone()
                self.c.execute("SELECT queryport FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
                monmap_qp = self.c.fetchone()
                self.conn.commit()
                serverhost = monmap_ip[0]
                queryport = monmap_qp[0]
                try:
                    self.server_info = sq.SourceQuery(serverhost, queryport)
                    resinfo = self.server_info.get_info()
                    resrules = self.server_info.get_rules()
                    lighting_val = resrules['Day_b']
                    if lighting_val == "true":
                        lighting = "Day"
                    else:
                        lighting = "Night"
                    self.server_info.disconnect()
                    if resinfo:
                        self.mogui.tbl_server_overview.setItem(i, 1, QtWidgets.QTableWidgetItem(serverhost +":" + str(resinfo['GamePort'])))
                        self.mogui.tbl_server_overview.setItem(i, 5, QtWidgets.QTableWidgetItem(resinfo['Map'] + " (" + lighting + ")"))
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
                    self.mogui.tbl_server_overview.setItem(i, 3, QtWidgets.QTableWidgetItem("Offline"))
                    self.mogui.tbl_server_overview.item(i, 3).setBackground(QtGui.QColor(254,0,0))
                    self.server_info.disconnect()
                i = i + 1
                progress_value = progress_value + progress_multiplier
        #Execute the Executor  
        execute_list_query(self)
        #Set Progress Bar
        self.mogui.mon_progress_bar.setValue(100)
        self.conn.close()
        time.sleep(0.3)
        self.mogui.mon_progress_bar.setValue(0)
    #Handle the Close Event
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