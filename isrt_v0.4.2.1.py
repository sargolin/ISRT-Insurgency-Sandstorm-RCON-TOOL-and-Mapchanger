#ISRT - Insurgency Sandstorm RCon Tool; 12.10.2020, Sargolin aka @ Madman
#In case of questions: oe@edelmeier.org
#Git: https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-TOOL-and-Mapchanger.git
#v0.4.2 - Integration further functionalities and database integration
#Database: ./db/isrt_data.db
#This is open Source, you may use, copy, modify it as you wish - feel free!

#
#Add to GUI Classes - only change this - the rest must be untouched!
#
# In definition part:
#
# from pathlib import Path
# icondir = Path(__file__).absolute().parent
#
# In Class, Function setupUI:
# 
# icon.addPixmap(QtGui.QPixmap(str(icondir / 'img/isrt.ico')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
# self.output_window_background.setPixmap(QtGui.QPixmap(str(icondir / '.\\img/isrt-bck.png')))
#   

#Importing required classes and libraries
import sys, query, os, re, sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from rcon import Console
from pathlib import Path
from gui.isrt_gui import Ui_main_window
from gui.about_gui import Ui_about_window
from gui.help_gui import Ui_help_window
from gui.server_gui import Ui_server_window

#Start definition of Classes, Functions/Methods and variables/attributes
#
#PyQt5 About UI
class about_gui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agui = Ui_about_window()
        self.agui.setupUi(self)

        self.agui.btn_about_close.clicked.connect(self.closeapp)

    def closeapp(self):
        self.close()

#PyQt5 Help UI
class help_gui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hgui = Ui_help_window()
        self.hgui.setupUi(self)

        self.hgui.btn_help_close.clicked.connect(self.closeapp)

    def closeapp(self):
        self.close()

#PyQt5 UI Initialization
class maingui(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gui = Ui_main_window()
        self.gui.setupUi(self)


        #Define buttons and menu items including their functionalities
        self.gui.menu_action_quit.triggered.connect(self.exit_app)
        self.gui.menu_action_about.triggered.connect(self.show_about_app)
        self.gui.menu_action_help.triggered.connect(self.show_help_app)
        self.gui.btn_refresh_list.clicked.connect(self.fill_dropdown_box)
        self.gui.menu_action_server.triggered.connect(self.show_server_app)
        self.gui.btn_main_exec_query.clicked.connect(self.checkandgoquery)
        self.gui.btn_main_exec_rcon.clicked.connect(self.checkandgorcon)
        self.gui.btn_main_rcon_help.clicked.connect(self.show_help_app)


        self.fill_dropdown_box()

        def assign_server_values_list(text):
            self.assign_server_values_list_text = text
            selection = self.assign_server_values_list_text
            
            conn = sqlite3.connect('db/isrt_data.db')
            c = conn.cursor()

            c.execute("select ipaddress FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selip in extract:
                sel_ipaddress = selip

            c.execute("select queryport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selqp in extract:
                sel_queryport = str(selqp)

            c.execute("select rconport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selrp in extract:
                sel_rconport = str(selrp)

            c.execute("select rconpw FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selrpw in extract:
                sel_rconpw = selrpw                

            conn.commit()
            conn.close()

            self.gui.entry_ip.setText(sel_ipaddress)
            self.gui.entry_queryport.setText(sel_queryport)
            self.gui.entry_rconport.setText(sel_rconport)
            self.gui.entry_rconpw.setText(sel_rconpw)
            self.checkandgoquery()

        self.gui.dropdown_select_server.activated[str].connect(assign_server_values_list)

    #Fill Dropdown Menue from scratch
    def fill_dropdown_box(self):
        #Connect to database
        dbdir = Path(__file__).absolute().parent
        conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
        c = conn.cursor()
        c.execute("select alias FROM server")
        dd_alias = c.fetchall()
        
        self.gui.dropdown_select_server.clear()

        for row in dd_alias:
            self.gui.dropdown_select_server.addItems(row)

        conn.commit()
        conn.close()    

    #Check for the format string and go for the rcon command, but only if rcon port and rcon password are given
    def checkandgorcon(self):
        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

        if self.gui.entry_rconpw.text():
            if (re.search(self.regexip, self.gui.entry_ip.text())):  
                self.serverhost = self.gui.entry_ip.text()
                try:
                    if self.gui.entry_rconport.text() and 1 <= int(self.gui.entry_rconport.text()) <= 65535:
                        serverhost = str(self.gui.entry_ip.text())
                        rconpassword = str(self.gui.entry_rconpw.text())
                        rconport = int(self.gui.entry_rconport.text())
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
                    self.gui.label_output_window.setText(self.gui.entry_rconport.text() + " is no valid Port number - please retry!")
            else:  
                self.gui.label_output_window.setText(self.gui.entry_ip.text() + " is no valid IP address - please retry!")         
        else:
            self.gui.label_output_window.setText("No RCON Password given - please retry!")    

    #Check for the IP and Queryport to be correct in syntax and range and go for the query
    def checkandgoquery(self):
        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''

        if (re.search(self.regexip, self.gui.entry_ip.text())):  
            self.serverhost = self.gui.entry_ip.text()
            try:
                if self.gui.entry_queryport.text() and 1 <= int(self.gui.entry_queryport.text()) <= 65535:
                    self.queryport = self.gui.entry_queryport.text()
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
                self.gui.label_output_window.setText(self.gui.entry_queryport.text() + " is no valid Port number - please retry!")
        else:  
            self.gui.label_output_window.setText(self.gui.entry_ip.text() + " is no valid IP address - please retry!")  

    #Show the About Window
    def show_about_app(self):
        self.about_app = None
        if self.about_app is None:
            self.about_app = about_gui()
        self.about_app.show()

    #Show the Help Window
    def show_help_app(self):
        self.help_app = None
        if self.help_app is None:
            self.help_app = help_gui()
        self.help_app.show()

    #Show the Server Management Window
    def show_server_app(self):
        self.serverapp = None
        if self.serverapp is None:
            self.serverapp = server_gui()
        self.serverapp.show()

    #Execute RCON Command, when called by checkandgorcon()!
    def rconserver(self, serverhost, rconpassword, rconport, rconcommand):
        if rconcommand.startswith("say") or rconcommand.startswith("Say") or rconcommand.startswith("SAY"):
            console = Console(host=serverhost, password=rconpassword, port=rconport)
            self.gui.label_output_window.setText("Say Commands do not provide a feedback, but are sent nevertheless correctly if no error is thrown!")
        else:
            console = Console(host=serverhost, password=rconpassword, port=rconport)
            commandconsole = (console.command(rconcommand))
            self.gui.label_output_window.setText(str(commandconsole))
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
        
        if self.servermodcheck == "true":
            self.mutatorids = self.serverruledetails['Mutators_s']
        else:
            self.mutatorids = "None"

        self.gui.le_servername.setText(str(self.servergamedetails['server_name']))
        self.gui.le_gamemode.setText(str(self.serverruledetails['GameMode_s']))
        self.gui.le_servermode.setText(str(self.servercoopcheck))
        self.gui.le_serverip_port.setText(str(self.servernetworkdetails['ip']) + ":" + str(self.servergamedetails['server_port']))
        self.gui.le_vac.setText(str(self.servervaccheck))
        self.gui.le_ranked.setText(str(self.serverrulecheck))
        self.gui.le_password.setText(str(self.serverpwcheck))
        self.gui.le_players.setText(str(self.servergamedetails['players_current']) + "/" + str(self.servergamedetails['players_max']))
        self.gui.le_ping.setText(str(self.servernetworkdetails['ping']))
        self.gui.le_map.setText(str(self.servergamedetails['game_map']))
        self.gui.le_mods.setText(str(self.mutatorids))

    #Exit the App itself
    def exit_app(self):
        self.close()

#PyQt5 Server Management UI
class server_gui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sgui = Ui_server_window()
        self.sgui.setupUi(self)

        self.sgui.btn_server_add.clicked.connect(self.server_add)
        self.sgui.btn_server_delete.clicked.connect(self.server_delete)
        
        self.create_dropdown()
        

        def assign_server_values(text):
            dbdir = Path(__file__).absolute().parent
            self.assign_server_values_text = text
            selection = self.assign_server_values_text
            
            conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
            c = conn.cursor()

            c.execute("select ipaddress FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selip in extract:
                sel_ipaddress = selip

            c.execute("select queryport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selqp in extract:
                sel_queryport = str(selqp)

            c.execute("select rconport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selrp in extract:
                sel_rconport = str(selrp)

            c.execute("select rconpw FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = c.fetchone()
            for selrpw in extract:
                sel_rconpw = selrpw                

            conn.commit()
            conn.close()

            self.sgui.server_alias.setText(selection)
            self.sgui.server_ip.setText(sel_ipaddress)
            self.sgui.server_query.setText(sel_queryport)
            self.sgui.server_rconport.setText(sel_rconport)
            self.sgui.server_rconpw.setText(sel_rconpw)

        self.sgui.dropdown_server_list.activated[str].connect(assign_server_values)

    #Create the Dropdown Menu
    def create_dropdown(self):
        #Connect to database
        dbdir = Path(__file__).absolute().parent
        conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
        c = conn.cursor()
        c.execute("select alias FROM server")
        dd_alias = c.fetchall()
        
        self.sgui.dropdown_server_list.clear()

        for row in dd_alias:
            self.sgui.dropdown_server_list.addItems(row)

        conn.commit()
        conn.close()

    #Add a server to DB
    def server_add(self):
        val_alias = self.sgui.server_alias.text()
        val_ipaddress = self.sgui.server_ip.text()
        val_queryport = self.sgui.server_query.text()
        val_rconport = self.sgui.server_rconport.text()
        val_rconpw = self.sgui.server_rconpw.text()

        #Connect to database
        dbdir = Path(__file__).absolute().parent
        conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
        c = conn.cursor()

        c.execute("select alias FROM server")
        check_alias = c.fetchone()
        
        if check_alias:
            for check in check_alias:
                if val_alias == check:
                    self.sgui.label_db_console.append("Alias already exists, please rename it")
                else:
                    if val_ipaddress and val_queryport and val_alias:
                        try:
                            #Connect to database
                            
                            c.execute("INSERT INTO server VALUES (:alias, :ipaddress, :queryport, :rconport, :rconpw)", {'alias': val_alias, 'ipaddress': val_ipaddress, 'queryport': val_queryport, 'rconport': val_rconport, 'rconpw': val_rconpw})
                            conn.commit()
                            self.sgui.label_db_console.append("Record inserted successfully into database")

                            conn.close()

                        except sqlite3.Error as error:
                            self.sgui.label_db_console.append("Failed to insert data into database " + str(error))
                            pass

                        finally:
                            if (conn):
                                conn.close()
            
                    else:
                        self.sgui.label_db_console.append("At least Alias, IP-Adress and Query Port have to contain a value!")
        else:
            if val_ipaddress and val_queryport and val_alias:
                try:
                    #Connect to database
                    
                    c.execute("INSERT INTO server VALUES (:alias, :ipaddress, :queryport, :rconport, :rconpw)", {'alias': val_alias, 'ipaddress': val_ipaddress, 'queryport': val_queryport, 'rconport': val_rconport, 'rconpw': val_rconpw})
                    conn.commit()
                    self.sgui.label_db_console.append("Record inserted successfully into database")

                    conn.close()

                except sqlite3.Error as error:
                    self.sgui.label_db_console.append("Failed to insert data into database " + str(error))
                    pass

                finally:
                    if (conn):
                        conn.close()
    
            else:
                self.sgui.label_db_console.append("At least Alias, IP-Adress and Query Port have to contain a value!")
        self.create_dropdown()
        
        conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
        c = conn.cursor()

        conn.commit()
        conn.close()
        refresh_dropdown_box()

    #Delete a Server from DB
    def server_delete(self):
        val_ipaddress = self.sgui.server_ip.text()
        val_queryport = self.sgui.server_query.text()
        val_alias = self.sgui.server_alias.text()

        if val_ipaddress and val_queryport:
            try:
                #Connect to database
                dbdir = Path(__file__).absolute().parent
                conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
                c = conn.cursor()
                
                c.execute("DELETE FROM server WHERE alias = :alias and ipaddress = :ipaddress and queryport = :queryport", {'alias': val_alias, 'ipaddress': val_ipaddress, 'queryport': val_queryport})
                conn.commit()
                self.sgui.label_db_console.append("Record deleted successfully from database")

                c.close()

            except sqlite3.Error as error:
                self.sgui.label_db_console.append("Failed to delete data from database " + str(error))
                pass

            finally:
                if (conn):
                    conn.close()

        else:
            self.sgui.label_db_console.append("At least IP-Adress and Query Port have to contain a value!")


        refresh_dropdown_box()
        self.create_dropdown()

    #Action on CloseEvent - Update Main list
    def closeEvent(self, event):
        refresh_dropdown_box()

 
#Main program
#
#Call program class
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mgui = maingui()
    mgui.show()
    #Ensure Update of DropDown Menu in maingui while switching between guis
    def refresh_dropdown_box():
        mgui.fill_dropdown_box()
    sys.exit(app.exec_())


