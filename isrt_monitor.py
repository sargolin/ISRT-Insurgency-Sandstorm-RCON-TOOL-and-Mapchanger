from PyQt5 import QtCore, QtGui, QtWidgets
import sys, sqlite3
from pathlib import Path
from bin.isrt_monitor_gui import Ui_UI_Server_Monitor
import bin.SourceQuery as sq

class mongui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        #Gui Setup
        super().__init__(*args, **kwargs)
        self.mogui = Ui_UI_Server_Monitor()
        self.mogui.setupUi(self)

        self.mogui.btn_exec_overview_refresh.clicked.connect(self.get_server_data)

    #Database connection setup
        self.dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(self.dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()

          
        self.fill_server_overview()

    #Fill Alias in the Server Overview
    def fill_server_overview(self):
        self.c.execute("SELECT alias FROM server")
        self.mogui.tbl_server_overview.setRowCount(0)
        self.conn.commit()
        
        for row, form in enumerate(self.c):
            self.mogui.tbl_server_overview.insertRow(row)
            for column, item in enumerate(form):
                self.mogui.tbl_server_overview.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))  

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


    def get_server_data(self):

        
      

        
        rowcount = self.mogui.tbl_server_overview.rowCount()
        for i in range(1, rowcount):
            server_temp_alias = (self.mogui.tbl_server_overview.item(i,0)).text()
            self.c.execute("SELECT ipaddress FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
            monmap_ip = self.c.fetchone()
            self.c.execute("SELECT queryport FROM server where alias=:temp_alias", {'temp_alias': server_temp_alias})
            monmap_qp = self.c.fetchone()
            self.conn.commit()    
            self.serverhost = monmap_ip[0]
            self.queryport = monmap_qp[0]

            self.server_info = sq.SourceQuery(self.serverhost, self.queryport)
            resinfo = self.server_info.get_info()
            if resinfo:
                print(server_temp_alias)
                print(self.serverhost +":" + str(resinfo['GamePort']))
                print(resinfo['Password'])
                print(resinfo['Secure'])
                print(resinfo['Map'])
                print("%i/%i" % (resinfo['Players'], resinfo['MaxPlayers']))
                print(resinfo['Ping'])
                if resinfo['Ping']:
                    print("Status: online")
            else:
                print(server_temp_alias + " ist offline")
            
            resrules = self.server_info.get_rules()
            if resrules:
                print(resrules['GameMode_s'])
                
            else:
                print(server_temp_alias + " ist offline")



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