#ISRT - Insurgency Sandstorm RCon Tool; 12.10.2020, Sargolin aka @ Madman
#In case of questions: oe@edelmeier.org
#Git: https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-TOOL-and-Mapchanger.git
#v0.2 - Integration of RCOn and QUERY options
#Database: ./db/isrt_data.db
#This is open Source, you may use, copy, modify it as you wish - feel free!

#Add to GUI Class imporeted file in function 'setupUI' - only change this - the rest must be untouched!
#
#In Main:
# from pathlib import Path
#
#In Function:
# icondir = Path(__file__).absolute().parent
# str(icondir / 'img/isrt.ico') so that the icon call reads:
#   icon.addPixmap(QtGui.QPixmap(str(icondir / 'img/isrt.ico')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#

#Importing required classes and libraries
import sys, query, os
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from rcon import Console
from isrt_gui import Ui_MainWindow
from about import Ui_aboutwindow

#PyQt5 About UI
class infogui(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.igui = Ui_aboutwindow()
        self.igui.setupUi(self)

        self.igui.pushButton.clicked.connect(self.closeapp)

    def closeapp(self):
        self.close()


#PyQt5 UI Initialization
class maingui(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)


        self.gui.exitbutton.clicked.connect(self.exitapp)
        self.gui.actionQuit.triggered.connect(self.exitapp)
        self.gui.actionINfo.triggered.connect(self.show_info_app)
        self.gui.submitbutton.clicked.connect(self.showquery)











    def showquery(self):
        self.serverhost = self.gui.entryip.text()
        self.queryport = self.gui.entryqueryport.text()
        setquery = self.queryserver(self.serverhost, self.queryport)
        
        
    def show_info_app(self):
        self.infoapp = None
        if self.infoapp is None:
            self.infoapp = infogui()
        self.infoapp.show()


    def exitapp(self):
        self.close()



#Execute RCON Command, when called
    def rconserver(self):
        console = Console(host=serverhost, password=rconpassword, port=rconport)
        console.command(rconcommand)
        console.close() 



#Execute Query Command, when called
    def queryserver(self, serverhost, queryport):
        self.server = query.Query(self.serverhost, self.queryport)
        self.serverinfo = (self.server.info())
        self.servergamedetails = (self.serverinfo['info'])
        self.serverrules = (self.server.rules())
        self.serverruledetails = (self.serverrules['rules'])
        self.servernetworkdetails = (self.serverinfo['server'])
        self.pwcheck = (self.servergamedetails['server_password_protected'])
        self.vaccheck = (self.servergamedetails['server_vac_secured'])
        self.ranked = (self.serverruledetails['RankedServer_b'])
        self.coop = (self.serverruledetails['Coop_b'])
        self.mods = (self.serverruledetails['Mods_b'])    

        if  self.mods == "true":
            self.servermodcheck = "Yes"
        else:
            self.servermodcheck = "No"  

        if  self.pwcheck == 0:
            self.serverpwcheck = "No"
        else:
            self.serverpwcheck = "Yes"

        if  self.vaccheck == 0:
            self.servervaccheck = "No"
        else:
            self.servervaccheck = "Yes"

        if  self.ranked == "true":
            self.serverrulecheck = "Yes"
        else:
            self.serverrulecheck = "No"

        if  self.coop == "true":
            self.servercoopcheck = "Coop"
        else:
            self.servercoopcheck = "Versus"
        
        if self.servermodcheck == "Yes":
            self.mutatorids = self.serverruledetails['Mutators_s']
        else:
            pass

        self.gui.querywindow.setText(
        str(self.servergamedetails['server_name']) + "\n" + 
        "Gamemode: " + str(self.serverruledetails['GameMode_s']) +  "\n" + 
        "Mode: " + str(self.servercoopcheck) +  "\n" + 
        "Ranked Server: " + str(self.serverrulecheck) +  "\n" + 
        "Server-IP: " + str(self.servernetworkdetails['ip']) + ":" + str(self.servergamedetails['server_port']) +  "\n" + 
        "Query-Port: " + str(self.servernetworkdetails['port']) + "\n" + 
        "Password: " + str(self.serverpwcheck) + "\n" + 
        "VAC-Secured: " + str(self.servervaccheck) + "\n" + 
        "Map: " + str(self.servergamedetails['game_map']) + "\n" + 
        "Players: " + str(self.servergamedetails['players_current']) + "/" + str(self.servergamedetails['players_max']) + "\n" + 
        "Ping: " + str(self.servernetworkdetails['ping']) + "\n" + 
        "Mods: " + str(self.servermodcheck) + " (" + str(self.mutatorids) + ")")







#Call main functions ### saved: #rconserver() #queryserver()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mgui = maingui()
    mgui.show()
    sys.exit(app.exec_())


