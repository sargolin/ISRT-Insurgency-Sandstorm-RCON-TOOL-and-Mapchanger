#ISRT - Insurgency Sandstorm RCon Tool; 12.10.2020, Sargolin aka @ Madman
#In case of questions: oe@edelmeier.org
#Git: https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-TOOL-and-Mapchanger.git
#v0.2 - Integration of RCOn and QUERY options
#Database: ./db/isrt_data.db
#This is open Source, you may use, copy, modify it as you wish - feel free!

#Importing required classes and libraries
import sys, query
from PyQt5.QtWidgets import QMainWindow, QApplication
from rcon import Console
from isrt_gui import Ui_MainWindow


#Define variables
serverhost = "93.186.198.185"
queryport = 27016
rconport = 27017
rconpassword = "Rfcd2025"
rconcommand = "help"




#PyQt5 Widget Setup
class maingui(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)













    #Execute RCON Command, when called
    def rconserver(self):
        console = Console(host=serverhost, password=rconpassword, port=rconport)
        console.command(rconcommand)
        console.close() 



    #Execute Query Command, when called
    def queryserver(self):
        server = query.Query(serverhost, queryport)
        serverinfo = (server.info())
        servergamedetails = (serverinfo['info'])
        serverrules = (server.rules())
        serverruledetails = (serverrules['rules'])
        servernetworkdetails = (serverinfo['server'])
        pwcheck = (servergamedetails['server_password_protected'])
        vaccheck = (servergamedetails['server_vac_secured'])
        ranked = (serverruledetails['RankedServer_b'])
        coop = (serverruledetails['Coop_b'])
        mods = (serverruledetails['Mods_b'])    

        if  mods == "true":
            servermodcheck = "Yes"
        else:
            servermodcheck = "No"  

        if  pwcheck == 0:
            serverpwcheck = "No"
        else:
            serverpwcheck = "Yes"

        if  vaccheck == 0:
            servervaccheck = "No"
        else:
            servervaccheck = "Yes"

        if  ranked == "true":
            serverrulecheck = "Yes"
        else:
            serverrulecheck = "No"

        if  coop == "true":
            servercoopcheck = "Coop"
        else:
            servercoopcheck = "Versus"

        print("Servername: ", servergamedetails['server_name'])
        print("Game: ", servergamedetails['game_description'])
        print("Gamemode: ", serverruledetails['GameMode_s'])
        print("Mode: ", servercoopcheck)
        print("Ranked Server: ", serverrulecheck)
        print("Server-IP: ", servernetworkdetails['ip'], ":", servergamedetails['server_port'])
        print("Query-Port: ", servernetworkdetails['port'])
        print("Password: ", serverpwcheck)
        print("VAC-Secured: ", servervaccheck)
        print("Map: ", servergamedetails['game_map'])
        print("Players: ", servergamedetails['players_current'], "/", servergamedetails['players_max'])
        print("Ping: ", servernetworkdetails['ping'])
        print("Mods: ", servermodcheck)
        if servermodcheck == "Yes":
            print("Mod-IDs: ", serverruledetails['ModList_s'])
            print("Mutators: ", serverruledetails['Mutators_s'])
        else:
            pass

















#Call main functions ### saved: #rconserver() #queryserver()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mgui = maingui()
    mgui.show()
    sys.exit(app.exec_())


