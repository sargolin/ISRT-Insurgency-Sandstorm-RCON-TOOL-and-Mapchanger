#ISRT - Insurgency Sandstorm RCon Tool; 12.10.2020, Sargolin aka @ Madman
#In case of questions: oe@edelmeier.org
#Git: https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-TOOL-and-Mapchanger.git
#v0.1.1 - Integration of RCON and QUERY options
#Database: ./db/isrt_data.db
#This is open Source, you may use, copy, modify it as you wish - feel free!

#Importing required classes and libraries
import sys, query, os, re
from PyQt5 import QtCore, QtGui, QtWidgets
from rcon import Console
from isrt_gui import Ui_MainWindow
from about_gui import Ui_aboutwindow
import socket

#
#Start definition of Classes, Functions/Methods and variables/attributes
#

#PyQt5 About UI
class infogui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.igui = Ui_aboutwindow()
        self.igui.setupUi(self)

        self.igui.pushButton.clicked.connect(self.closeapp)

    def closeapp(self):
        self.close()


#PyQt5 UI Initialization
class maingui(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        #Define buttons and menu items uincluding their functionalities
        self.gui.exitbutton.clicked.connect(self.exitapp)
        self.gui.actionQuit.triggered.connect(self.exitapp)
        self.gui.actionINfo.triggered.connect(self.show_info_app)
        self.gui.submitbutton.clicked.connect(self.checkandgoquery)
        self.gui.rconsubmitbutton.clicked.connect(self.checkandgorcon)


#Check for the format string and go for the rcon command, but only if rcon port and rcon password are given
    def checkandgorcon(self):
        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

        if (re.search(self.regexip, self.gui.entryip.text())):  
            self.serverhost = self.gui.entryip.text()
            try:
                if self.gui.entryrconport.text() and 1 <= int(self.gui.entryrconport.text()) <= 65535:
                    serverhost = str(self.gui.entryip.text())
                    rconpassword = str(self.gui.entryrconpw.text())
                    rconport = int(self.gui.entryrconport.text())
                    rconcommand = str(self.gui.label_rconcommand.text())   
                    try:
                        self.rconserver(serverhost, rconpassword,  rconport, rconcommand)
                    except Exception as e: 
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setWindowTitle("ISRT Error Message")
                        msg.setText("Something went wrong: \n\n" + str(e) + "\n\nWrong IP, Port or Password?")
                        msg.exec_()
                else:
                    raise ValueError
            except ValueError:
                self.gui.terminalwindows.setText(self.gui.entryrconport.text() + " is no valid Port number - please retry!")
        else:  
            self.gui.terminalwindows.setText(self.gui.entryip.text() + " is no valid IP address - please retry!")         
        
        
        
#Check for the IP and Queryport to be correct in syntax and range and go for the query
    def checkandgoquery(self):
        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

        if (re.search(self.regexip, self.gui.entryip.text())):  
            self.serverhost = self.gui.entryip.text()
            try:
                if self.gui.entryqueryport.text() and 1 <= int(self.gui.entryqueryport.text()) <= 65535:
                    self.queryport = self.gui.entryqueryport.text()
                    try:
                        self.queryserver(self.serverhost, self.queryport)
                    except Exception as f: 
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                        msg.setIcon(QtWidgets.QMessageBox.Critical)
                        msg.setWindowTitle("ISRT Error Message")
                        msg.setText("Something went wrong: \n\n" + str(f) + "\n\nWrong IP or Port?")
                        msg.exec_()
                else:
                    raise ValueError
            except ValueError:
                self.gui.querywindow.setText(self.gui.entryqueryport.text() + " is no valid Port number - please retry!")
        else:  
            self.gui.querywindow.setText(self.gui.entryip.text() + " is no valid IP address - please retry!")  


#Show the About Windows
    def show_info_app(self):
        self.infoapp = None
        if self.infoapp is None:
            self.infoapp = infogui()
        self.infoapp.show()


#Exit the App itself
    def exitapp(self):
        self.close()


#Execute RCON Command, when called by checkandgorcon()!
    def rconserver(self, serverhost, rconpassword, rconport, rconcommand):
        console = Console(host=serverhost, password=rconpassword, port=rconport)
        commandconsole = (console.command(rconcommand))

        self.gui.terminalwindows.setText(str(commandconsole))
        console.close() 


#Execute Query Command, when called by checkandgoquery()!
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

#
#Call main functions ### saved: #rconserver() #queryserver()
#
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mgui = maingui()
    mgui.show()
    sys.exit(app.exec_())


