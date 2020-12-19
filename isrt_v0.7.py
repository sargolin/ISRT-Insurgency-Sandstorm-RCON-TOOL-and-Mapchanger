'''
ISRT - Insurgency Sandstorm RCON Tool; 19.11.2020, Madman
In case of questions: isrt@edelmeier.org
Git: https://github.com/olli-e/ISRT-Insurgency-Sandstorm-RCON-Query-Tool
v0.7 - Win-Installer, Update Mechanism, Listplayers Scrumble, Refresh Timer and so on....
Database: ./db/isrt_data.db
This is open Source, you may use, copy, modify it as you wish - feel free!
Thanks to Helsing and Stuermer for the pre-release testing - I appreciate that so much!






------------------------------------------------------------------
Importing required classes and libraries
------------------------------------------------------------------'''
import sys, os, re, sqlite3, time, socket, threading
import bin.SourceQuery as sq
import bin.query as query
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from shutil import copy2
from pathlib import Path
from bin.isrt_gui import Ui_ISRT_Main_Window
from bin.rn_gui import Ui_rn_window
from bin.rcon.console import Console










#PyQt5 Main UI Initialization
'''------------------------------------------------------------------
Release Notes GUI Handler
------------------------------------------------------------------'''
class rngui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        #Gui Setup
        super().__init__(*args, **kwargs)
        self.rngui = Ui_rn_window()
        self.rngui.setupUi(self)
        self.rngui.btn_rn_close.clicked.connect(self.close_rn)

    def close_rn(self):
        #Database connection setup
        dbdir = Path(__file__).absolute().parent
        conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
        c = conn.cursor()
        
        if self.rngui.chkbx_show_rn.isChecked():
            rnsetoff = 0
            c.execute("UPDATE release_info SET show_rn = :rnset", {'rnset' :rnsetoff})
            conn.commit()
            conn.close()
        self.close()

    def closeEvent(self, event):
        self.close() 


















'''------------------------------------------------------------------
Main GUI Handlers
------------------------------------------------------------------'''
class maingui(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        #Gui Setup
        super().__init__(*args, **kwargs)
        self.gui = Ui_ISRT_Main_Window()
        self.gui.setupUi(self)

        #Database connection setup
        self.dbdir = Path(__file__).absolute().parent
        dbdir = Path(__file__).absolute().parent
        self.conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
        self.c = self.conn.cursor()

        #Setup ISRT Monitor Call
        def call_monitor():
            def start_monitor_thread():
                os.system("isrt_monitor.py")
            
            t1 = threading.Thread(target=start_monitor_thread)
            t1.start()

        #Define buttons and menu items including their functionalities
        self.gui.btn_main_exec_query.clicked.connect(self.checkandgoquery)
        self.gui.btn_main_open_server_monitor.clicked.connect(call_monitor)
        self.gui.btn_main_exec_rcon.clicked.connect(self.checkandgorcon)
        self.gui.btn_cust_delete_selected.clicked.connect(self.custom_command_clear_selected)
        self.gui.btn_cust_delete_all.clicked.connect(self.custom_command_clear_all)
        self.gui.btn_save_settings.clicked.connect(self.save_settings)
        self.gui.btn_main_copytoclipboard.clicked.connect(self.copy2clipboard)
        self.gui.btn_main_drcon_changemap.clicked.connect(self.map_changer)
        self.gui.btn_add_cust_command.clicked.connect(self.add_custom_command_manually)
        self.gui.btn_exec_db_backup.clicked.connect(self.create_db_backup)
        self.gui.btn_main_add_server_db.clicked.connect(self.server_add_main)

        #Define entry fields for user input
        self.gui.entry_ip.returnPressed.connect(self.checkandgoquery)
        self.gui.LE_add_custom_command.returnPressed.connect(self.add_custom_command_manually)
        self.gui.entry_queryport.returnPressed.connect(self.checkandgoquery)
        self.gui.entry_rconport.returnPressed.connect(self.checkandgoquery)
        self.gui.entry_rconpw.returnPressed.connect(self.checkandgoquery)
        self.gui.label_button_name_1.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_2.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_3.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_4.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_5.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_6.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_7.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_8.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_9.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_10.returnPressed.connect(self.save_settings)
        self.gui.label_button_name_11.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_1.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_2.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_3.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_4.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_5.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_6.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_7.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_8.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_9.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_10.returnPressed.connect(self.save_settings)
        self.gui.label_command_button_11.returnPressed.connect(self.save_settings)

        #Connect Labels with enter key press
        self.gui.label_rconcommand.returnPressed.connect(self.checkandgorcon)

        #self.gui.entry_refresh_timer.returnPressed.connect(self.checkandgorcon)
        self.gui.server_alias.returnPressed.connect(self.server_add)
        self.gui.server_ip.returnPressed.connect(self.server_add)
        self.gui.server_query.returnPressed.connect(self.server_add)
        self.gui.server_rconport.returnPressed.connect(self.server_add)
        self.gui.server_rconpw.returnPressed.connect(self.server_add)

        #Fill the Dropdown menus
        self.fill_dropdown_server_box()
        self.fill_dropdown_custom_command()
        self.fill_list_custom_command()
        self.get_configuration_from_DB_and_set_settings()

        #Define the server manager tab
        self.gui.btn_server_add.clicked.connect(self.server_add)
        self.gui.btn_server_modify.clicked.connect(self.server_modify)
        self.gui.btn_server_delete.clicked.connect(self.server_delete)

        #Fill the Server dropdown menu
        def assign_server_values(text):
            self.assign_server_values_text = text
            selection = self.assign_server_values_text
            #Get variables for servers to fill dropdpwn            
            self.c.execute("select ipaddress FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selip in extract:
                sel_ipaddress = selip
            self.c.execute("select queryport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selqp in extract:
                sel_queryport = str(selqp)
            self.c.execute("select rconport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selrp in extract:
                sel_rconport = str(selrp)
            self.c.execute("select rconpw FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selrpw in extract:
                sel_rconpw = selrpw                
            self.conn.commit()
            self.gui.server_alias.setText(selection)
            self.gui.server_ip.setText(sel_ipaddress)
            self.gui.server_query.setText(sel_queryport)
            self.gui.server_rconport.setText(sel_rconport)
            self.gui.server_rconpw.setText(sel_rconpw)

        #Assign Server variables for Dropdown menu on selection
        def assign_server_values_list(text):
            self.assign_server_values_list_text = text
            selection = self.assign_server_values_list_text
            self.c.execute("select ipaddress FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selip in extract:
                sel_ipaddress = selip
            self.c.execute("select queryport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selqp in extract:
                sel_queryport = str(selqp)
            self.c.execute("select rconport FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selrp in extract:
                sel_rconport = str(selrp)
            self.c.execute("select rconpw FROM server WHERE alias = (:select_alias)", {'select_alias': selection})
            extract = self.c.fetchone()
            for selrpw in extract:
                sel_rconpw = selrpw                
            self.conn.commit()
            self.gui.entry_ip.setText(sel_ipaddress)
            self.gui.entry_queryport.setText(sel_queryport)
            self.gui.entry_rconport.setText(sel_rconport)
            self.gui.entry_rconpw.setText(sel_rconpw)
            self.checkandgoquery()

        self.gui.dropdown_server_list.activated[str].connect(assign_server_values)

        #Assign custom Commands variables for Dropdown menu
        def assign_custom_commands_values_list(text):
            self.assign_custom_commands_values_list_text = text
            selection = self.assign_custom_commands_values_list_text
            #Handover selected RCON Command
            self.gui.label_rconcommand.setText(selection)

        #Connect execution of selected variables with drop down menu select
        self.gui.dropdown_select_server.activated[str].connect(assign_server_values_list)
        self.gui.dropdown_custom_commands.activated[str].connect(assign_custom_commands_values_list)

        #Set empty saved indicator for configuration window
        self.gui.label_saving_indicator.clear()

        #Call method to define the custom buttons
        self.assign_main_custom_buttons()

        #DB Import Buttons and fields
        self.data_path = None
        self.gui.btn_select_database.clicked.connect(lambda: self.DB_import("select_db"))
        self.gui.btn_add_database.clicked.connect(lambda: self.DB_import("add_db"))
        self.gui.btn_replace_database.clicked.connect(lambda: self.DB_import("replace_db"))

        #Map and option assignment
        self.gui.dropdown_select_travelscenario.activated[str].connect(self.selected_map_switch)






 




            
    '''------------------------------------------------------------------
    Dropdown Menu Handling
    ------------------------------------------------------------------'''            
    #Fill Dropdown Menue for custom commands from scratch
    def fill_dropdown_custom_command(self):
        self.c.execute("select distinct commands FROM cust_commands")
        dh_alias = self.c.fetchall()
        self.gui.dropdown_custom_commands.clear()
        for row in dh_alias:
            self.gui.dropdown_custom_commands.addItems(row)
        self.conn.commit()
    #Fill Dropdown Custom Commands Manager
    def fill_list_custom_command(self):
        self.c.execute("select distinct commands FROM cust_commands")
        dcust_alias = self.c.fetchall()
        self.gui.list_custom_commands_console.clear()
        for row in dcust_alias:
            self.gui.list_custom_commands_console.addItems(row)
        self.conn.commit()
    #Fill Dropdown Menue Server Selection and Serverlist plus TableWidget in Server Manager
    def fill_dropdown_server_box(self):
        self.c.execute("select alias FROM server")
        dd_alias = self.c.fetchall()
        self.gui.dropdown_select_server.clear()
        self.gui.dropdown_server_list.clear()
        for row in dd_alias:
            self.gui.dropdown_select_server.addItems(row)
            self.gui.dropdown_server_list.addItems(row)
        self.conn.commit()

        self.gui.tbl_server_manager.clearSpans()

        self.c.execute("SELECT * FROM server")
        self.gui.tbl_server_manager.setRowCount(0)
        self.conn.commit()
        for row, form in enumerate(self.c):
            self.gui.tbl_server_manager.insertRow(row)
            for column, item in enumerate(form):
                self.gui.tbl_server_manager.setItem(row, column, QtWidgets.QTableWidgetItem(str(item)))  

        self.gui.tbl_server_manager.insertRow(0)
        self.gui.tbl_server_manager.setItem(0, 0, QtWidgets.QTableWidgetItem("Alias"))
        self.gui.tbl_server_manager.item(0, 0).setBackground(QtGui.QColor(254,254,254))
        self.gui.tbl_server_manager.setItem(0, 1, QtWidgets.QTableWidgetItem("IP-Address"))
        self.gui.tbl_server_manager.item(0, 1).setBackground(QtGui.QColor(254,254,254))
        self.gui.tbl_server_manager.setItem(0, 2, QtWidgets.QTableWidgetItem("Query Port"))
        self.gui.tbl_server_manager.item(0, 2).setBackground(QtGui.QColor(254,254,254))
        self.gui.tbl_server_manager.setItem(0, 3, QtWidgets.QTableWidgetItem("RCON Port"))
        self.gui.tbl_server_manager.item(0, 3).setBackground(QtGui.QColor(254,254,254))
        self.gui.tbl_server_manager.setItem(0, 4, QtWidgets.QTableWidgetItem("RCON Password"))
        self.gui.tbl_server_manager.item(0, 4).setBackground(QtGui.QColor(254,254,254))
    #Fill Dropdown Menu for Mapchanging from scratch
    def fill_dropdown_map_box(self):
        self.c.execute("select map_name FROM map_config WHERE modid = '0' ORDER by Map_name")
        dm_alias = self.c.fetchall()
        self.conn.commit() 
        self.gui.dropdown_select_travelscenario.clear()
        for rowmaps in dm_alias:
            self.gui.dropdown_select_travelscenario.addItems(rowmaps)

        if self.mutator_id_list == "None":
            pass
        else:
            if self.mutator_id_list[0]:
                self.gui.dropdown_select_travelscenario.addItem("------Custom Maps------")
                for custom_maps in self.mutator_id_list:
                    self.c.execute("select map_name FROM map_config WHERE modid=:mod_id ORDER by Map_name", {'mod_id':custom_maps})
                    dm2_alias = self.c.fetchone()   
                    self.conn.commit()
                    if dm2_alias != None: 
                        self.gui.dropdown_select_travelscenario.addItems(dm2_alias)
           









    '''------------------------------------------------------------------
    Custom Command Handling
    ------------------------------------------------------------------'''    
    #Add custom command manually
    def add_custom_command_manually(self):
        #Check new RCON commands for validity
        def assess_custom_command_var(new__manual_custom_command):
            self.positive_command_check = 0
            if (new__manual_custom_command.startswith("quit") or
                new__manual_custom_command.startswith("exit") or
                new__manual_custom_command.startswith("listplayers") or 
                new__manual_custom_command.startswith("help") or 
                new__manual_custom_command.startswith("kick") or 
                new__manual_custom_command.startswith("permban") or 
                new__manual_custom_command.startswith("travel") or 
                new__manual_custom_command.startswith("ban") or 
                new__manual_custom_command.startswith("banid") or 
                new__manual_custom_command.startswith("listbans") or 
                new__manual_custom_command.startswith("unban") or 
                new__manual_custom_command.startswith("say") or 
                new__manual_custom_command.startswith("restartround") or 
                new__manual_custom_command.startswith("maps") or 
                new__manual_custom_command.startswith("scenarios") or 
                new__manual_custom_command.startswith("travelscenario") or 
                new__manual_custom_command.startswith("gamemodeproperty") or 
                new__manual_custom_command.startswith("listgamemodeproperties")):
                self.positive_c_command_check = 1
            else:
                self.positive_c_command_check = 0
     
        #Check and assign for positive assesment value and insert or throw error
        new__manual_custom_command = self.gui.LE_add_custom_command.text()
        if new__manual_custom_command:
            assess_custom_command_var(new__manual_custom_command)
            if self.positive_c_command_check == 1:
                self.c.execute("INSERT INTO cust_commands VALUES (:commands)",{'commands': new__manual_custom_command})
                self.conn.commit()
                self.gui.LE_add_custom_command.clear()
            if self.positive_c_command_check == 0:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new__manual_custom_command} is no new valid custom RCON command! \n\n Please try again!")
                msg.exec_()  
        else:
            pass
        self.fill_list_custom_command()
        self.fill_dropdown_custom_command()
    #Clear all Custom Commands
    def custom_command_clear_all(self):
        self.c.execute("DELETE from cust_commands")
        self.gui.list_custom_commands_console.clear()
        self.conn.commit()
        self.fill_list_custom_command()
        self.fill_dropdown_custom_command()
    #Clear selected commands from Custom commands
    def custom_command_clear_selected(self):
        delete_commands = self.gui.list_custom_commands_console.selectedItems()
        if delete_commands:
         for row in delete_commands:
             self.c.execute("DELETE FROM cust_commands WHERE commands=:delcommand", {'delcommand': row.text()})
         else:
             pass
        self.conn.commit()
        self.fill_list_custom_command()
        self.fill_dropdown_custom_command()
    #Define the Custom Buttons in the Main menu
    def assign_main_custom_buttons(self):
        #Get DB variables for custom buttons
        self.c.execute('''select btn1_name, btn1_command, 
                            btn2_name, btn2_command, 
                            btn3_name, btn3_command, 
                            btn4_name, btn4_command, 
                            btn5_name, btn5_command, 
                            btn6_name, btn6_command, 
                            btn7_name, btn7_command, 
                            btn8_name, btn8_command, 
                            btn9_name, btn9_command, 
                            btn10_name, btn10_command, 
                            btn11_name, btn11_command 
                            from configuration''')
        dbconf_cust = self.c.fetchall()
        self.conn.commit()
        dbconf_cust_strip = dbconf_cust[0]
        #Split Tuple and extract buttons names and commands

        self.button1_name = (dbconf_cust_strip[0]) 
        self.button1_command = (dbconf_cust_strip[1]) 
        self.button2_name = (dbconf_cust_strip[2])
        self.button2_command = (dbconf_cust_strip[3])
        self.button3_name = (dbconf_cust_strip[4])
        self.button3_command = (dbconf_cust_strip[5])
        self.button4_name = (dbconf_cust_strip[6])
        self.button4_command = (dbconf_cust_strip[7])
        self.button5_name = (dbconf_cust_strip[8])
        self.button5_command = (dbconf_cust_strip[9])
        self.button6_name = (dbconf_cust_strip[10])
        self.button6_command = (dbconf_cust_strip[11])
        self.button7_name = (dbconf_cust_strip[12])
        self.button7_command = (dbconf_cust_strip[13])
        self.button8_name = (dbconf_cust_strip[14])
        self.button8_command = (dbconf_cust_strip[15])
        self.button9_name = (dbconf_cust_strip[16])
        self.button9_command = (dbconf_cust_strip[17])
        self.button10_name = (dbconf_cust_strip[18])
        self.button10_command = (dbconf_cust_strip[19])
        self.button11_name = (dbconf_cust_strip[20])
        self.button11_command = (dbconf_cust_strip[21])
        #Assign variables (Button names and commands) to custom Buttons
        self.gui.btn_main_drcon_listplayers.setText(self.button1_name)
        self.gui.btn_main_drcon_listplayers_definition.setText(self.button1_name)
        self.gui.btn_main_drcon_listbans.setText(self.button2_name)
        self.gui.btn_main_drcon_listbans_definition.setText(self.button2_name)
        self.gui.btn_main_drcon_listmaps.setText(self.button3_name)
        self.gui.btn_main_drcon_listmaps_definition.setText(self.button3_name)
        self.gui.btn_main_drcon_listscenarios.setText(self.button4_name)
        self.gui.btn_main_drcon_listscenarios_definition.setText(self.button4_name)
        self.gui.btn_main_drcon_restartround.setText(self.button5_name)
        self.gui.btn_main_drcon_restartround_definition.setText(self.button5_name)
        self.gui.btn_main_drcon_showgamemode.setText(self.button6_name)
        self.gui.btn_main_drcon_showgamemode_definition.setText(self.button6_name)
        self.gui.btn_main_drcon_showaidiff.setText(self.button7_name)
        self.gui.btn_main_drcon_showaidiff_definition.setText(self.button7_name)
        self.gui.btn_main_drcon_showsupply.setText(self.button8_name)
        self.gui.btn_main_drcon_showsupply_definition.setText(self.button8_name)
        self.gui.btn_main_drcon_roundlimit.setText(self.button9_name)
        self.gui.btn_main_drcon_roundlimit_definition.setText(self.button9_name)
        self.gui.btn_main_drcon_showroundtime.setText(self.button10_name)
        self.gui.btn_main_drcon_showroundtime_definition.setText(self.button10_name)
        self.gui.btn_main_drcon_help.setText(self.button11_name)
        self.gui.btn_main_drcon_help_2definition.setText(self.button11_name)
        self.gui.btn_main_drcon_listplayers.clicked.connect(lambda: self.direct_rcon_command(self.button1_command))
        self.gui.btn_main_drcon_listbans.clicked.connect(lambda: self.direct_rcon_command(self.button2_command))
        self.gui.btn_main_drcon_listmaps.clicked.connect(lambda: self.direct_rcon_command(self.button3_command))
        self.gui.btn_main_drcon_listscenarios.clicked.connect(lambda: self.direct_rcon_command(self.button4_command))
        self.gui.btn_main_drcon_restartround.clicked.connect(lambda: self.direct_rcon_command(self.button5_command))
        self.gui.btn_main_drcon_showgamemode.clicked.connect(lambda: self.direct_rcon_command(self.button6_command))
        self.gui.btn_main_drcon_showaidiff.clicked.connect(lambda: self.direct_rcon_command(self.button7_command))
        self.gui.btn_main_drcon_showsupply.clicked.connect(lambda: self.direct_rcon_command(self.button8_command))
        self.gui.btn_main_drcon_roundlimit.clicked.connect(lambda: self.direct_rcon_command(self.button9_command))
        self.gui.btn_main_drcon_showroundtime.clicked.connect(lambda: self.direct_rcon_command(self.button10_command))
        self.gui.btn_main_drcon_help.clicked.connect(lambda: self.direct_rcon_command(self.button11_command))









    '''------------------------------------------------------------------
    Query Handling
    ------------------------------------------------------------------'''
    #Check for the IP and Queryport to be correct in syntax and range and go for the query
    def checkandgoquery(self):
        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)$'''
        
        val_localhost = "127.0.0.1"

        if self.gui.entry_ip.text() == val_localhost:
            try:
                qmsg = QtWidgets.QMessageBox()
                qmsg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                qmsg.setIcon(QtWidgets.QMessageBox.Information)
                qmsg.setWindowTitle("ISRT Error Message")
                qmsg.setText("Due to a Windows connection problem, 127.0.0.1\ncannot be used for INS, switching to LAN IP-Address!")
                qmsg.exec_()
                self.serverhost = socket.gethostbyname(socket.getfqdn())
                self.queryport = self.gui.entry_queryport.text()
                self.gui.entry_ip.setText(self.serverhost)
                self.gui.label_output_window.setStyleSheet("border-image:url(:/img/img/rcon-bck.jpg);\n")
                self.queryserver(self.serverhost, self.queryport)
                if self.queryserver:
                    self.get_listplayers_fancy()
            except Exception:
                self.gui.label_output_window.setStyleSheet("border-image:url(:/img/img/offline.jpg);\n")
                self.gui.le_password.setStyleSheet("border-image: url(:/img/img/lock-unchecked.png);")
                self.gui.label_map_view.setStyleSheet("border-image: url(:/map_view/img/maps/map_views.jpg)")
                self.gui.tbl_player_output.setRowCount(0)
                self.gui.le_servername.clear()
                self.gui.le_gamemode.clear()
                self.gui.dropdown_select_travelscenario.clear()
                self.gui.dropdown_select_gamemode.clear()
                self.gui.dropdown_select_lighting.clear()
                self.gui.le_serverip_port.clear()
                self.gui.le_vac.clear()
                self.gui.le_players.clear()
                self.gui.le_ping.clear()
                self.gui.le_map.clear()
                self.gui.le_mods.clear()
        elif (re.search(self.regexip, self.gui.entry_ip.text())):  
            self.serverhost = self.gui.entry_ip.text()
            try:
                if self.gui.entry_queryport.text() and 1 <= int(self.gui.entry_queryport.text()) <= 65535:
                    self.queryport = self.gui.entry_queryport.text()
                    try:
                        self.queryserver(self.serverhost, self.queryport)
                        if self.queryserver:
                            self.get_listplayers_fancy()
                        self.gui.label_output_window.setStyleSheet("border-image:url(:/img/img/rcon-bck.jpg);\n")
                    except Exception:
                        self.gui.le_password.setStyleSheet("border-image: url(:/img/img/lock-unchecked.png);")
                        self.gui.label_map_view.setStyleSheet("border-image: url(:/map_view/img/maps/map_views.jpg)")
                        self.gui.label_output_window.setStyleSheet("border-image:url(:/img/img/offline.jpg);\n")
                        self.gui.tbl_player_output.setRowCount(0)
                        self.gui.dropdown_select_travelscenario.clear()
                        self.gui.dropdown_select_gamemode.clear()
                        self.gui.dropdown_select_lighting.clear()
                        self.gui.le_servername.clear()
                        self.gui.le_gamemode.clear()
                        self.gui.le_serverip_port.clear()
                        self.gui.le_vac.clear()
                        self.gui.le_players.clear()
                        self.gui.le_ping.clear()
                        self.gui.le_map.clear()
                        self.gui.le_mods.clear()
                else:
                    raise ValueError
            except ValueError:
                self.gui.label_output_window.setText(self.gui.entry_queryport.text() + " is no valid Query Port number - please retry!")
        else:  
            self.gui.label_output_window.setText(self.gui.entry_ip.text() + " is no valid IP address - please retry!")  
    #Execute Query Command, when called by checkandgoquery()!
    def queryserver(self, serverhost, queryport):
        self.gui.label_output_window.clear()
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
        self.mods = (self.serverruledetails['Mutated_b'])    
        if  self.mods == "true":
            self.servermodcheck = "Yes"
        else:
            self.servermodcheck = "No"  

        if  self.pwcheck == 0:
            self.gui.le_password.setStyleSheet("border-image: url(:/img/img/lock-unlocked.png);")
        else:
            self.gui.le_password.setStyleSheet("border-image: url(:/img/img/lock-locked.png);")

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
            self.mutatorids = "None"

        self.gui.le_servername.setText(str(self.servergamedetails['server_name']))
        self.gui.le_gamemode.setText(str(self.serverruledetails['GameMode_s']) + " (" + str(self.servercoopcheck) + ")")
        self.gui.le_serverip_port.setText(str(self.servernetworkdetails['ip']) + ":" + str(self.servergamedetails['server_port']))
        self.gui.le_vac.setText(str(self.servervaccheck) + "/" + str(self.serverrulecheck))
        self.gui.le_players.setText(str(self.servergamedetails['players_current']) + "/" + str(self.servergamedetails['players_max']))
        self.gui.le_ping.setText(str(self.servernetworkdetails['ping']))
        self.gui.le_map.setText(str(self.servergamedetails['game_map']))
        self.gui.le_mods.setText(str(self.mutatorids))
        
        
        #Creating a list for mutator-IDs to identify installed maps
        check_modlist = self.serverruledetails.get('ModList_s')
        if check_modlist:
            self.mutator_id_list = (self.serverruledetails['ModList_s'].split(','))
        else:
            self.mutator_id_list = "None"


        #Create Map View Picture based on running map
        def assign_map_view_pic(self):
            map_view_pic = str(self.servergamedetails['game_map'])
            self.c.execute("select map_pic FROM map_config WHERE map_alias=:map_view_result", {'map_view_result': map_view_pic})
            dpmap_alias = self.c.fetchone()
            self.conn.commit()
            if dpmap_alias:
                self.gui.label_map_view.setStyleSheet(f"border-image: url(:map_thumbs/img/maps/thumbs/{dpmap_alias[0]}); background-color: #f0f0f0;background-position: center;background-repeat: no-repeat;")
            else:
                self.gui.label_output_window.setText("No Map Image available - referring to placeholder!") 
                self.gui.label_map_view.setStyleSheet("border-image: url(:/map_view/img/maps/map_views.jpg); background-color: #f0f0f0;background-position: center;background-repeat: no-repeat;")        
        assign_map_view_pic(self)
        self.fill_dropdown_map_box()
    #Get fancy returned Playerlist
    def get_listplayers_fancy(self):
        self.serverhost = self.gui.entry_ip.text()
        self.queryport = self.gui.entry_queryport.text()
        self.server_players = sq.SourceQuery(self.serverhost, int(self.queryport))
        row = 0
        self.gui.tbl_player_output.setRowCount(0)
        if self.server_players.get_players():
            for player in self.server_players.get_players():
                data_id = ("{id}".format(**player))
                data_name = ("{Name}".format(**player))
                data_frags = ("{Frags}".format(**player))
                data_prettyTime = ("{PrettyTime}".format(**player))

                self.gui.tbl_player_output.insertRow(row)
                self.gui.tbl_player_output.setItem(row, 0, QtWidgets.QTableWidgetItem(data_id))
                self.gui.tbl_player_output.setItem(row, 1, QtWidgets.QTableWidgetItem(data_name))
                self.gui.tbl_player_output.setItem(row, 2, QtWidgets.QTableWidgetItem(data_frags))
                self.gui.tbl_player_output.setItem(row, 3, QtWidgets.QTableWidgetItem(data_prettyTime))
                row = row + 1
        else:
            self.gui.label_output_window.setText("No Players online")










    '''------------------------------------------------------------------
    RCON Handling
    ------------------------------------------------------------------'''
    #Map Changer Preparation - Selector
    def selected_map_switch(self):
        self.selected_map = self.gui.dropdown_select_travelscenario.currentText()

        self.c.execute("select map_alias FROM map_config WHERE map_name=:var_selected_map", {'var_selected_map': self.selected_map})
        dsma_alias = self.c.fetchone()
        self.conn.commit() 
        var_selected_map = (dsma_alias[0])

        self.c.execute("select * from map_modes where map_alias=:varselmap", {'varselmap': var_selected_map})        
        dsmam_alias = self.c.fetchall()
        self.conn.commit()
        dsmam_list = (dsmam_alias[0])
        var_dn = dsmam_list[1]
        var_cp = dsmam_list[2]
        var_cp_ins = dsmam_list[3]
        var_cphc = dsmam_list[4]
        var_cphc_ins = dsmam_list[5]
        var_dom = dsmam_list[6]
        var_ffe = dsmam_list[7]
        var_ffw = dsmam_list[8]
        var_fl = dsmam_list[9]
        var_op = dsmam_list[10]
        var_pu = dsmam_list[11]
        var_pu_ins = dsmam_list[12]
        var_ski = dsmam_list[13]
        var_tdm = dsmam_list[14]

        self.gui.dropdown_select_lighting.clear()
        self.gui.dropdown_select_gamemode.clear()

        if var_dn == 10:
            self.gui.dropdown_select_lighting.addItem("Day")
        else:
            var_dn_list = ("Day", "Night")
            self.gui.dropdown_select_lighting.addItems(var_dn_list)
            

        if var_cp == 1:
            self.gui.dropdown_select_gamemode.addItem("CheckPoint Security")
        
        if var_cp_ins == 1:
            self.gui.dropdown_select_gamemode.addItem("CheckPoint Insurgents")

        if var_cphc == 1:
            self.gui.dropdown_select_gamemode.addItem("CheckPoint Hardcore Security")

        if var_cphc_ins == 1:
            self.gui.dropdown_select_gamemode.addItem("CheckPoint Hardcore Insurgents")

        if var_dom == 1:
            self.gui.dropdown_select_gamemode.addItem("Domination")

        if var_ffe == 1:
            self.gui.dropdown_select_gamemode.addItem("Firefight East")

        if var_ffw == 1:
            self.gui.dropdown_select_gamemode.addItem("Firefight West")

        if var_fl == 1:
            self.gui.dropdown_select_gamemode.addItem("Frontline")

        if var_op == 1:
            self.gui.dropdown_select_gamemode.addItem("Outpost")

        if var_pu == 1:
            self.gui.dropdown_select_gamemode.addItem("Push Security")

        if var_pu_ins == 1:
            self.gui.dropdown_select_gamemode.addItem("Push Insurgents")

        if var_ski == 1:
            self.gui.dropdown_select_gamemode.addItem("Skirmish")

        if var_tdm == 1:
            self.gui.dropdown_select_gamemode.addItem("TeamDeathMatch")

        
        self.gui.dropdown_select_gamemode.setCurrentText("CheckPoint Hardcore Security")
        self.gui.dropdown_select_lighting.setCurrentText("Day")
    #Mapchanger
    def map_changer(self):
        #Define required variables
        val_map = self.gui.dropdown_select_travelscenario.currentText()
        val_gamemode = self.gui.dropdown_select_gamemode.currentText()
        val_light = self.gui.dropdown_select_lighting.currentText()
        


        if val_gamemode == "CheckPoint Security":
            val_gamemode = "checkpoint"
        elif val_gamemode == "CheckPoint Insurgents":
            val_gamemode = "checkpoint_ins"
        elif val_gamemode == "CheckPoint Hardcore Security":
            val_gamemode = "checkpointhardcore"
        elif val_gamemode == "CheckPoint Hardcore Insurgents":
            val_gamemode = "checkpointhardcore_ins"
        elif val_gamemode == "Domination":
            val_gamemode = "domination"
        elif val_gamemode == "Firefight East":
            val_gamemode = "firefight_east"
        elif val_gamemode == "Firefight West":
            val_gamemode = "firefight_west"
        elif val_gamemode == "Frontline":
            val_gamemode = "frontline"
        elif val_gamemode == "Outpost":
            val_gamemode = "outpost"
        elif val_gamemode == "Push Security":
            val_gamemode = "push"
        elif val_gamemode == "Push Insurgents":
            val_gamemode = "push_ins"
        elif val_gamemode == "Skirmish":
            val_gamemode = "skirmish"
        elif val_gamemode == "TeamDeathMatch":
            val_gamemode = "teamdeathmath"



        if val_map.startswith("Select") or val_map.startswith("---"):
            self.gui.label_output_window.setText("This is not a valid map, please chose one first!")
        else:
            self.c.execute("select map_alias FROM map_config WHERE map_name=:sql_map_name", {'sql_map_name':val_map})
            val_map_alias = self.c.fetchone()
            val_map_alias_result = (str(val_map_alias[0]))
            query = ("select " + val_gamemode + " FROM map_config WHERE map_alias=:sqlmap_alias")
            self.c.execute(query, {'sqlmap_alias': val_map_alias_result})
            val_travel_alias = self.c.fetchone()
            val_travel_alias_result = (str(val_travel_alias[0]))
            self.conn.commit()

            command = ("travel " + val_map_alias_result + "?Scenario=" + val_travel_alias_result + "?Lighting=" + val_light + "?game=" + val_gamemode)

            if command:
                self.gui.label_rconcommand.setText(command)
            else:
                self.gui.label_output_window.setText("Something went wrong with the Travel command, please check above and report it!")  
            
            self.checkandgoquery()
            self.gui.progressbar_map_changer.setProperty("value", 0)
    #Direct RCON Command handling
    def direct_rcon_command(self, command):
        #Check if an rcon command is passed        
        if command:
            self.gui.label_rconcommand.setText(command)
            self.checkandgorcon()  
        else:
           self.gui.label_output_window.setText("Something went wrong with the RCON command, please report it!")  
    #Check for the format string and go for the rcon command, but only if rcon port and rcon password are given
    def checkandgorcon(self):
        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)$'''

        command_check = self.gui.label_rconcommand.text()

        save_command_check = None
        #Save commands while hitting Submit
        save_command_check = 1
 
        val_localhost = "127.0.0.1"

        if self.gui.entry_ip.text() == val_localhost:
            self.gui.label_output_window.setText("Due to a Windows connection problem, 127.0.0.1 cannot be used currently, please use your LAN IP-Address!")
        else:    
            if self.gui.entry_rconpw.text() and command_check.startswith("quit") or command_check.startswith("exit") or command_check.startswith("help") or command_check.startswith("listplayers") or command_check.startswith("kick") or command_check.startswith("permban") or command_check.startswith("travel") or command_check.startswith("ban") or command_check.startswith("banid") or command_check.startswith("listbans") or command_check.startswith("unban") or command_check.startswith("say") or command_check.startswith("restartround") or command_check.startswith("maps") or command_check.startswith("scenarios") or command_check.startswith("travelscenario") or command_check.startswith("gamemodeproperty") or command_check.startswith("listgamemodeproperties"):
                if (re.search(self.regexip, self.gui.entry_ip.text())):  
                    self.serverhost = self.gui.entry_ip.text()
                    try:
                        if self.gui.entry_rconport.text() and 1 <= int(self.gui.entry_rconport.text()) <= 65535:
                            serverhost = str(self.gui.entry_ip.text())
                            rconpassword = str(self.gui.entry_rconpw.text())
                            rconport = int(self.gui.entry_rconport.text())
                            rconcommand = str(self.gui.label_rconcommand.text())
                            if save_command_check == 1 and command_check:
                                self.c.execute("INSERT INTO cust_commands VALUES (:commands)",{'commands': command_check})
                                self.conn.commit()
                                self.fill_dropdown_custom_command()
                                self.fill_list_custom_command()
                            try:
                                self.rconserver(serverhost, rconpassword,  rconport, rconcommand)
                                self.gui.progressbar_map_changer.setProperty("value", 33)
                                time.sleep(1)
                                self.gui.progressbar_map_changer.setProperty("value", 66)
                                time.sleep(1)
                                self.gui.progressbar_map_changer.setProperty("value", 100)
                                time.sleep(0.1)
                                self.gui.progressbar_map_changer.setProperty("value", 0)
                            except Exception as e: 
                                msg = QtWidgets.QMessageBox()
                                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                                msg.setIcon(QtWidgets.QMessageBox.Critical)
                                msg.setWindowTitle("ISRT Error Message")
                                msg.setText("We encountered and error: \n\n" + str(e) + "\n\nWrong IP, RCON Port, Command or Password?\nThe server may also be down - please check that!")
                                msg.exec_()
                                self.gui.progressbar_map_changer.setProperty("value", 0)
                        else:
                            raise ValueError
                    except ValueError:
                        self.gui.label_output_window.setText(self.gui.entry_rconport.text() + " is no valid RCON Port number - please retry!")
                        self.gui.progressbar_map_changer.setProperty("value", 0)
                else:  
                    self.gui.label_output_window.setText(self.gui.entry_ip.text() + " is no valid IP address - please retry!")       
                    self.gui.progressbar_map_changer.setProperty("value", 0)  
            else:
                self.gui.label_output_window.setText("No RCON Password given or no valid RCON command - please retry!")    
                self.gui.progressbar_map_changer.setProperty("value", 0)
    #Execute RCON Command, when called by checkandgorcon()!
    def rconserver(self, serverhost, rconpassword, rconport, rconcommand):
        if rconcommand.startswith("say") or rconcommand.startswith("Say"):
            self.gui.label_output_window.setText(rconcommand + " command has been sent to the server")
            console = Console(host=serverhost, password=rconpassword, port=rconport)
            commandconsole = (console.command(rconcommand))
        elif rconcommand.startswith("restartround") or rconcommand.startswith("Restartround"):
            self.gui.label_output_window.setText("Round restarted without Team swap!")
            console = Console(host=serverhost, password=rconpassword, port=rconport)
            commandconsole = (console.command(rconcommand)) 
        else:
            console = Console(host=serverhost, password=rconpassword, port=rconport)
            commandconsole = (console.command(rconcommand))
            self.gui.label_output_window.setText(str(commandconsole))
            # '''Test'''
            # print(commandconsole)
            # '''Test'''
        console.close() 









    '''------------------------------------------------------------------
    Server Manager
    ------------------------------------------------------------------'''
    #Add a server to DB
    def server_add(self):
        val_alias = self.gui.server_alias.text()
        val_ipaddress = self.gui.server_ip.text()
        val_queryport = self.gui.server_query.text()
        val_rconport = self.gui.server_rconport.text()
        val_rconpw = self.gui.server_rconpw.text()

        go_addserver_check = 0

        #Check IP
        self.regexip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)$'''

        self.regexport = r'''^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$'''

        if val_alias and val_ipaddress and val_queryport:
            go_addserver_check = 1
        else:
            self.gui.label_db_console.append("At least Alias, IP-Adress and Query Port have to contain a value!")
            go_addserver_check = 0

        if val_ipaddress and (re.search(self.regexip, val_ipaddress)):  
            go_addserver_ipcheck = 1
        else:
            self.gui.label_db_console.setText(val_ipaddress + " is no valid IP address - please check and retry!")
            go_addserver_ipcheck = 0


        if val_queryport and (re.search(self.regexport, val_queryport)):
            go_addserver_qpcheck = 1
        else:
            self.gui.label_db_console.setText(val_queryport + " is no valid Query Port - please check and retry!")
            go_addserver_qpcheck = 0


        if val_rconport:
            if (re.search(self.regexport, val_rconport)):
                pass
            else:
                self.gui.label_db_console.setText(val_rconport + " is no valid RCON Port - please check and retry!")
                go_addserver_check = 0


        self.c.execute("select alias FROM server")
        check_alias = self.c.fetchall()
        self.conn.commit()
        nogocheck = 1                

        for check in check_alias:
            for item in check:
                if item and val_alias == item:
                    go_addserver_check = 0
                    self.gui.label_db_console.append("Alias already exists, please rename it")
                    nogocheck = 0
                else:
                    nogocheck = 1

        if go_addserver_check == 1 and nogocheck == 1 and go_addserver_ipcheck == 1 and go_addserver_qpcheck == 1:
            try:
               
                self.c.execute("INSERT INTO server VALUES (:alias, :ipaddress, :queryport, :rconport, :rconpw)", {'alias': val_alias, 'ipaddress': val_ipaddress, 'queryport': val_queryport, 'rconport': val_rconport, 'rconpw': val_rconpw})
                self.conn.commit()
                self.gui.label_db_console.append("Server inserted successfully into database")
            except sqlite3.Error as error:
                self.gui.label_db_console.append("Failed to insert server into database " + str(error))

        self.fill_dropdown_server_box()
   #Add a server to DB
    def server_add_main(self):
        self.gui.label_output_window.setStyleSheet("border-image:url(:/img/img/rcon-bck.jpg);\n")
        transferalias = self.gui.dropdown_select_server.currentText()
        transferip = self.gui.entry_ip.text()
        transferqport = self.gui.entry_queryport.text()
        transferrport = self.gui.entry_rconport.text()
        transferrpw = self.gui.entry_rconpw.text()

        #Check IP
        self.regextransip = r'''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)\.( 
        25[0-5]|2[0-5][0-9]|[0-1]?[0-9][0-9]?)$'''

        self.regextransport = r'''^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$'''

        go_addserver_check = 0
        go_addserver_ipcheck = 0
        go_addserver_qpcheck = 0

        if transferip and transferqport:
            go_addserver_check = 1
            if transferip and (re.search(self.regextransip, transferip)):  
                go_addserver_ipcheck = 1
                if transferqport and (re.search(self.regextransport, transferqport)):
                    go_addserver_qpcheck = 1
                    if transferqport and (re.search(self.regextransport, transferqport)):
                        go_addserver_qpcheck = 1
                        if transferrport:
                            if (re.search(self.regextransport, transferrport)):
                                pass
                            else:
                                self.gui.label_output_window.append("You entered no valid RCON Port - please check and retry!")
                                go_addserver_check = 0
                    else:
                        self.gui.label_output_window.append("You entered no valid Query Port - please check and retry!")
                        go_addserver_qpcheck = 0
                else:
                    self.gui.label_output_window.append("You entered no valid Query Port - please check and retry!")
                    go_addserver_qpcheck = 0
            else:
                self.gui.label_output_window.append("You entered no valid IP address - please check and retry!")
                go_addserver_ipcheck = 0
        else:
            self.gui.label_output_window.append("At least IP-Adress and Query Port have to contain a value!")
            go_addserver_check = 0

        
        if go_addserver_check == 1 and  go_addserver_ipcheck == 1 and go_addserver_qpcheck == 1:
            self.gui.TabWidget_Main_overall.setCurrentWidget(self.gui.Tab_Server)
            if transferalias == "Select Server":
                transferalias = ""

            self.gui.server_alias.setText(transferalias)
            self.gui.server_ip.setText(transferip)
            self.gui.server_query.setText(transferqport)
            self.gui.server_rconport.setText(transferrport)
            self.gui.server_rconpw.setText(transferrpw)
    #Modify a server in DB
    def server_modify(self):
        val_alias = self.gui.server_alias.text()
        val_ipaddress = self.gui.server_ip.text()
        val_queryport = self.gui.server_query.text()
        val_rconport = self.gui.server_rconport.text()
        val_rconpw = self.gui.server_rconpw.text()

        self.c.execute("select alias FROM server")
        check_m_alias = self.c.fetchall()
        self.conn.commit()
        go2check = 1
        nogo2check = 0

        for check2 in check_m_alias:
            for item2 in check2:
                if val_alias == item2:
                    go2check = 1
                else:
                    nogo2check = 0


        if go2check == 1 and nogo2check == 0:
            if val_ipaddress and val_queryport and val_alias:
                try:
                                
                    self.c.execute("UPDATE server SET ipaddress=:ipaddress, queryport=:queryport, rconport=:rconport, rconpw=:rconpw WHERE alias=:alias", {'ipaddress': val_ipaddress, 'queryport': val_queryport, 'rconport': val_rconport, 'rconpw': val_rconpw, 'alias': val_alias})

                    self.conn.commit()
                    self.gui.label_db_console.append("Server updated successfully in database")


                except sqlite3.Error as error:
                    self.gui.label_db_console.append("Failed to update server in database " + str(error))
                        
            else:
                self.gui.label_db_console.append("At least Alias, IP-Adress and Query Port have to contain a value!")
        else:
            self.gui.label_db_console.append("Update not possible, Server does not exist in Database - try to add it first!")

        self.fill_dropdown_server_box()
    #Delete a Server from DB
    def server_delete(self):
        val_alias = self.gui.server_alias.text()

        if val_alias:
            try:
                self.c.execute("DELETE FROM server WHERE alias=:alias", {'alias': val_alias})
                self.conn.commit()
                self.gui.label_db_console.append("Record deleted successfully from database")

            except sqlite3.Error as error:
                self.gui.label_db_console.append("Failed to delete data from database " + str(error))
                pass

        else:
            self.gui.label_db_console.append("At least Alias has to contain a value!")


        self.fill_dropdown_server_box()
    #Import Database Routines
    def DB_import(self, db_action):
        if db_action == 'select_db':
            db_select_directory = (str(self.dbdir) + '\\db\\')
            self.data_path=QtWidgets.QFileDialog.getOpenFileName(self,'Select Database', db_select_directory, '*.db',)
            self.gui.label_selected_db.setText(self.data_path[0])
        elif db_action == 'add_db':
            if self.data_path and self.data_path[0].endswith(".db"):
                self.gui.label_db_console.setText("Adding Server from " + self.data_path[0] + " to current database")

                #Database connection setup for Importing
                dbimportdir = self.data_path[0]
                connimport = sqlite3.connect(dbimportdir)
                cidb = connimport.cursor()
                cidb.execute("select * FROM server")
                dbimport_result = cidb.fetchall()
                connimport.commit()
                for import_result in dbimport_result:
                    import_server_alias = import_result[0]
                    import_server_ip = import_result[1]
                    import_server_queryport = import_result[2]
                    import_server_rconport = import_result[3]
                    import_server_rconpw = import_result[4]
                    self.c.execute("INSERT INTO server VALUES (:alias, :ipaddress, :queryport, :rconport, :rconpw)", {'alias': import_server_alias, 'ipaddress': import_server_ip, 'queryport': import_server_queryport, 'rconport': import_server_rconport, 'rconpw': import_server_rconpw})
                    self.conn.commit()
                    
                self.gui.label_db_console.setText("Added Server from " + self.data_path[0] + " to current database")
            else:
                self.gui.label_db_console.setText("Please select a database first!")
        elif db_action == 'replace_db':
            if self.data_path and self.data_path[0].endswith(".db"):
                self.gui.label_db_console.setText("Replacing Server from " + self.data_path[0] + " in current database")

                #Database connection setup for Importing
                dbimportdir = self.data_path[0]
                connimport = sqlite3.connect(dbimportdir)
                cidb = connimport.cursor()
                cidb.execute("select * FROM server")
                dbimport_result = cidb.fetchall()
                connimport.commit()

                def showImport_Dialog():
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                    msgBox.setIcon(QtWidgets.QMessageBox.Warning)
                    msgBox.setText("Really replace all servers in the current DB with the imported DB Servers?\n\nConsider creating a backup of the DB file before clicking 'Yes':\n\n" + str(self.dbdir / 'db/isrt_data.db'))
                    msgBox.setWindowTitle("ISRT DB Import Warning")
                    msgBox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                    msgBox.setDefaultButton(QtWidgets.QMessageBox.No)
                    msgBox.buttonClicked.connect(delete_and_import_db)
                    msgBox.exec()

                def delete_and_import_db(i):
                    if i.text() == "&Yes":
                        self.c.execute("DELETE FROM server")
                        self.conn.commit()
                        for import_result in dbimport_result:
                            import_server_alias = import_result[0]
                            import_server_ip = import_result[1]
                            import_server_queryport = import_result[2]
                            import_server_rconport = import_result[3]
                            import_server_rconpw = import_result[4]
                            self.c.execute("INSERT INTO server VALUES (:alias, :ipaddress, :queryport, :rconport, :rconpw)", {'alias': import_server_alias, 'ipaddress': import_server_ip, 'queryport': import_server_queryport, 'rconport': import_server_rconport, 'rconpw': import_server_rconpw})
                            
                        self.conn.commit()
                        self.gui.label_db_console.setText("Replaced Server from " + self.data_path[0] + " in current database")
                        self.gui.label_selected_db.clear()

                    else:
                        self.gui.label_db_console.setText("Import canceled!")
                        self.gui.label_selected_db.clear()


                showImport_Dialog()
                self.data_path = ''

            else:
                self.gui.label_db_console.setText("Please select a database first!")
        
        self.fill_dropdown_server_box()
    #Backup current Server-DB
    def create_db_backup(self):
        #Define a timestamp format for backup
        FORMAT = '%Y%m%d%H%M%S'
        db_backup_directory = (str(self.dbdir) + '/db/')
        db_source_filename = (db_backup_directory + 'isrt_data.db')
        db_backup_filename = (db_backup_directory + datetime.now().strftime(FORMAT) + '_isrt_data.db')
        copy2(str(db_source_filename), str(db_backup_filename))
        
        self.gui.label_db_console.setText("Backup created at: \n" + db_backup_filename)








    '''------------------------------------------------------------------
    Exit App and special Handling Routines
    ------------------------------------------------------------------'''
    #Check status of configuration of refresh trigger
    def get_configuration_from_DB_and_set_settings(self):
        self.c.execute('''select btn1_name, btn1_command, 
                    btn2_name, btn2_command, 
                    btn3_name, btn3_command, 
                    btn4_name, btn4_command, 
                    btn5_name, btn5_command, 
                    btn6_name, btn6_command, 
                    btn7_name, btn7_command, 
                    btn8_name, btn8_command, 
                    btn9_name, btn9_command, 
                    btn10_name, btn10_command, 
                    btn11_name, btn11_command 
                    from configuration''')
        dbbutton_conf = self.c.fetchall()
        self.conn.commit()
        dbbutton_conf_strip = dbbutton_conf[0]
        self.gui.label_button_name_1.setText(dbbutton_conf_strip[0])
        self.gui.label_command_button_1.setText(dbbutton_conf_strip[1])
        self.gui.label_button_name_2.setText(dbbutton_conf_strip[2])
        self.gui.label_command_button_2.setText(dbbutton_conf_strip[3])
        self.gui.label_button_name_3.setText(dbbutton_conf_strip[4])
        self.gui.label_command_button_3.setText(dbbutton_conf_strip[5])
        self.gui.label_button_name_4.setText(dbbutton_conf_strip[6])
        self.gui.label_command_button_4.setText(dbbutton_conf_strip[7])
        self.gui.label_button_name_5.setText(dbbutton_conf_strip[8])
        self.gui.label_command_button_5.setText(dbbutton_conf_strip[9])
        self.gui.label_button_name_6.setText(dbbutton_conf_strip[10])
        self.gui.label_command_button_6.setText(dbbutton_conf_strip[11])
        self.gui.label_button_name_7.setText(dbbutton_conf_strip[12])
        self.gui.label_command_button_7.setText(dbbutton_conf_strip[13])
        self.gui.label_button_name_8.setText(dbbutton_conf_strip[14])
        self.gui.label_command_button_8.setText(dbbutton_conf_strip[15])
        self.gui.label_button_name_9.setText(dbbutton_conf_strip[16])
        self.gui.label_command_button_9.setText(dbbutton_conf_strip[17])
        self.gui.label_button_name_10.setText(dbbutton_conf_strip[18])
        self.gui.label_command_button_10.setText(dbbutton_conf_strip[19])
        self.gui.label_button_name_11.setText(dbbutton_conf_strip[20])
        self.gui.label_command_button_11.setText(dbbutton_conf_strip[21])
        self.c.execute("select quitbox from configuration")
        quitbox_setting = self.c.fetchone()
        self.conn.commit()
        if quitbox_setting[0] == 1:
            self.gui.chkbox_close_question.setChecked(True)
        else:
            self.gui.chkbox_close_question.setChecked(False)
    #Save changed settings
    def save_settings(self):
        #Assign new vairbales for check and update
        new_btn1_name_var = self.gui.label_button_name_1.text()
        new_btn1_command_var = self.gui.label_command_button_1.text()
        new_btn2_name_var = self.gui.label_button_name_2.text()
        new_btn2_command_var = self.gui.label_command_button_2.text()
        new_btn3_name_var = self.gui.label_button_name_3.text()
        new_btn3_command_var = self.gui.label_command_button_3.text()
        new_btn4_name_var = self.gui.label_button_name_4.text()
        new_btn4_command_var = self.gui.label_command_button_4.text()
        new_btn5_name_var = self.gui.label_button_name_5.text()
        new_btn5_command_var = self.gui.label_command_button_5.text()
        new_btn6_name_var = self.gui.label_button_name_6.text()
        new_btn6_command_var = self.gui.label_command_button_6.text()
        new_btn7_name_var = self.gui.label_button_name_7.text()
        new_btn7_command_var = self.gui.label_command_button_7.text()
        new_btn8_name_var = self.gui.label_button_name_8.text()
        new_btn8_command_var = self.gui.label_command_button_8.text()
        new_btn9_name_var = self.gui.label_button_name_9.text()
        new_btn9_command_var = self.gui.label_command_button_9.text()
        new_btn10_name_var = self.gui.label_button_name_10.text()
        new_btn10_command_var = self.gui.label_command_button_10.text()
        new_btn11_name_var = self.gui.label_button_name_11.text()
        new_btn11_command_var = self.gui.label_command_button_11.text()
        
        #Check new RCON commands for validity
        def assess_command_var(new_button_command):
            self.positive_command_check = 0
            if (new_button_command.startswith("exit") or 
                new_button_command.startswith("quit") or 
                new_button_command.startswith("listplayers") or 
                new_button_command.startswith("help") or 
                new_button_command.startswith("kick") or 
                new_button_command.startswith("permban") or 
                new_button_command.startswith("travel") or 
                new_button_command.startswith("ban") or 
                new_button_command.startswith("banid") or 
                new_button_command.startswith("listbans") or 
                new_button_command.startswith("unban") or 
                new_button_command.startswith("say") or 
                new_button_command.startswith("restartround") or 
                new_button_command.startswith("maps") or 
                new_button_command.startswith("scenarios") or 
                new_button_command.startswith("travelscenario") or 
                new_button_command.startswith("gamemodeproperty") or 
                new_button_command.startswith("listgamemodeproperties")):
                self.positive_command_check = 1
            else:
                self.positive_command_check = 0
        
        #Check and update new Button 1 name
        if new_btn1_name_var and self.button1_name != new_btn1_name_var:
            self.c.execute("UPDATE configuration SET btn1_name=:btn1name", {'btn1name': new_btn1_name_var})
            self.conn.commit()
            self.button1_name = new_btn1_name_var
            self.gui.btn_main_drcon_listplayers.setText(new_btn1_name_var)
            self.gui.btn_main_drcon_listplayers_definition.setText(new_btn1_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 1 command
        if new_btn1_command_var and self.button1_command != new_btn1_command_var:
            new_button_command = new_btn1_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn1_command=:btn1command", {'btn1command': new_btn1_command_var})
                self.conn.commit()
                self.button1_command = new_btn1_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn1_command_var} is no valid RCON command for Button 1! \n\n Please try again!")
                msg.exec_()

        #Check and update new Button 2 name
        if new_btn2_name_var and self.button2_name != new_btn2_name_var:
            self.c.execute("UPDATE configuration SET btn2_name=:btn2name", {'btn2name': new_btn2_name_var})
            self.conn.commit()
            self.button2_name = new_btn2_name_var
            self.gui.btn_main_drcon_listbans.setText(new_btn2_name_var)
            self.gui.btn_main_drcon_listbans_definition.setText(new_btn2_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 2 command
        if new_btn2_command_var and self.button2_command != new_btn2_command_var:
            new_button_command = new_btn2_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn2_command=:btn2command", {'btn2command': new_btn2_command_var})
                self.conn.commit()
                self.button2_command = new_btn2_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn2_command_var} is no valid RCON command for Button 2! \n\n Please try again!")
                msg.exec_()    

        #Check and update new Button 3 name
        if new_btn3_name_var and self.button3_name != new_btn3_name_var:
            self.c.execute("UPDATE configuration SET btn3_name=:btn3name", {'btn3name': new_btn3_name_var})
            self.conn.commit()
            self.button3_name = new_btn3_name_var
            self.gui.btn_main_drcon_listmaps.setText(new_btn3_name_var)
            self.gui.btn_main_drcon_listmaps_definition.setText(new_btn3_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 3 command
        if new_btn3_command_var and self.button3_command != new_btn3_command_var:
            new_button_command = new_btn3_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn3_command=:btn3command", {'btn3command': new_btn3_command_var})
                self.conn.commit()
                self.button3_command = new_btn3_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn3_command_var} is no valid RCON command for Button 3! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 4 name
        if new_btn4_name_var and self.button4_name != new_btn4_name_var:
            self.c.execute("UPDATE configuration SET btn4_name=:btn4name", {'btn4name': new_btn4_name_var})
            self.conn.commit()
            self.button4_name = new_btn4_name_var
            self.gui.btn_main_drcon_listscenarios.setText(new_btn4_name_var)
            self.gui.btn_main_drcon_listscenarios_definition.setText(new_btn4_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 4 command
        if new_btn4_command_var and self.button4_command != new_btn4_command_var:
            new_button_command = new_btn4_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn4_command=:btn4command", {'btn4command': new_btn4_command_var})
                self.conn.commit()
                self.button4_command = new_btn4_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn4_command_var} is no valid RCON command for Button 4! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 5 name
        if new_btn5_name_var and self.button5_name != new_btn5_name_var:
            self.c.execute("UPDATE configuration SET btn5_name=:btn5name", {'btn5name': new_btn5_name_var})
            self.conn.commit()
            self.button5_name = new_btn5_name_var
            self.gui.btn_main_drcon_restartround.setText(new_btn5_name_var)
            self.gui.btn_main_drcon_restartround_definition.setText(new_btn5_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 5 command
        if new_btn5_command_var and self.button5_command != new_btn5_command_var:
            new_button_command = new_btn5_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn5_command=:btn5command", {'btn5command': new_btn5_command_var})
                self.conn.commit()
                self.button5_command = new_btn5_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn5_command_var} is no valid RCON command for Button 5! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 6 name
        if new_btn6_name_var and self.button6_name != new_btn6_name_var:
            self.c.execute("UPDATE configuration SET btn6_name=:btn6name", {'btn6name': new_btn6_name_var})
            self.conn.commit()
            self.button6_name = new_btn6_name_var
            self.gui.btn_main_drcon_showgamemode.setText(new_btn6_name_var)
            self.gui.btn_main_drcon_showgamemode_definition.setText(new_btn6_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 6 command
        if new_btn6_command_var and self.button6_command != new_btn6_command_var:
            new_button_command = new_btn6_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn6_command=:btn6command", {'btn6command': new_btn6_command_var})
                self.conn.commit()
                self.button6_command = new_btn6_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn6_command_var} is no valid RCON command for Button 6! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 7 name
        if new_btn7_name_var and self.button7_name != new_btn7_name_var:
            self.c.execute("UPDATE configuration SET btn7_name=:btn7name", {'btn7name': new_btn7_name_var})
            self.conn.commit()
            self.button7_name = new_btn7_name_var
            self.gui.btn_main_drcon_showaidiff.setText(new_btn7_name_var)
            self.gui.btn_main_drcon_showaidiff_definition.setText(new_btn7_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 7 command
        if new_btn7_command_var and self.button7_command != new_btn7_command_var:
            new_button_command = new_btn7_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn7_command=:btn7command", {'btn7command': new_btn7_command_var})
                self.conn.commit()
                self.button7_command = new_btn7_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn7_command_var} is no valid RCON command for Button 7! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 8 name
        if new_btn8_name_var and self.button8_name != new_btn8_name_var:
            self.c.execute("UPDATE configuration SET btn8_name=:btn8name", {'btn8name': new_btn8_name_var})
            self.conn.commit()
            self.button8_name = new_btn8_name_var
            self.gui.btn_main_drcon_showsupply.setText(new_btn8_name_var)
            self.gui.btn_main_drcon_showsupply_definition.setText(new_btn8_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 8 command
        if new_btn8_command_var and self.button8_command != new_btn8_command_var:
            new_button_command = new_btn8_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn8_command=:btn8command", {'btn8command': new_btn8_command_var})
                self.conn.commit()
                self.button8_command = new_btn8_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn8_command_var} is no valid RCON command for Button 8! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 9 name
        if new_btn9_name_var and self.button9_name != new_btn9_name_var:
            self.c.execute("UPDATE configuration SET btn9_name=:btn9name", {'btn9name': new_btn9_name_var})
            self.conn.commit()
            self.button9_name = new_btn9_name_var
            self.gui.btn_main_drcon_roundlimit.setText(new_btn9_name_var)
            self.gui.btn_main_drcon_roundlimit_definition.setText(new_btn9_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 9 command
        if new_btn9_command_var and self.button9_command != new_btn9_command_var:
            new_button_command = new_btn9_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn9_command=:btn9command", {'btn9command': new_btn9_command_var})
                self.conn.commit()
                self.button9_command = new_btn9_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn9_command_var} is no valid RCON command for Button 9! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 10 name
        if new_btn10_name_var and self.button10_name != new_btn10_name_var:
            self.c.execute("UPDATE configuration SET btn10_name=:btn10name", {'btn10name': new_btn10_name_var})
            self.conn.commit()
            self.button10_name = new_btn10_name_var
            self.gui.btn_main_drcon_showroundtime.setText(new_btn10_name_var)
            self.gui.btn_main_drcon_showroundtime_definition.setText(new_btn10_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 10 command
        if new_btn10_command_var and self.button10_command != new_btn10_command_var:
            new_button_command = new_btn10_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn10_command=:btn10command", {'btn10command': new_btn10_command_var})
                self.conn.commit()
                self.button10_command = new_btn10_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn10_command_var} is no valid RCON command for Button 10! \n\n Please try again!")
                msg.exec_()  

        #Check and update new Button 11 name
        if new_btn11_name_var and self.button11_name != new_btn11_name_var:
            self.c.execute("UPDATE configuration SET btn11_name=:btn11name", {'btn11name': new_btn11_name_var})
            self.conn.commit()
            self.button11_name = new_btn11_name_var
            self.gui.btn_main_drcon_help.setText(new_btn11_name_var)
            self.gui.btn_main_drcon_help_2definition.setText(new_btn11_name_var)
            self.gui.label_saving_indicator.setText("Saved!")
        #Check and update new Button 11 command
        if new_btn11_command_var and self.button11_command != new_btn11_command_var:
            new_button_command = new_btn11_command_var
            assess_command_var(new_button_command)
            if self.positive_command_check == 1:
                self.c.execute("UPDATE configuration SET btn11_command=:btn11command", {'btn11command': new_btn11_command_var})
                self.conn.commit()
                self.button11_command = new_btn11_command_var
                self.gui.label_saving_indicator.setText("Saved!")
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowIcon(QtGui.QIcon(".\\img/isrt.ico"))
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle("ISRT Error Message")
                msg.setText(f"Something went wrong: \n\n {new_btn11_command_var} is no valid RCON command for Button 11! \n\n Please try again!")
                msg.exec_()  
        #Refresh the Settings in clicking save!
        self.c.execute("select quitbox from configuration")
        self.conn.commit()
        quitbox_result = self.c.fetchone()
        if self.gui.chkbox_close_question.isChecked():
            check_quitapp = 1
        else:
            check_quitapp = 0
        if quitbox_result[0] != check_quitapp:
            if self.gui.chkbox_close_question.isChecked():
                self.c.execute("UPDATE configuration SET quitbox=1")
                self.conn.commit()
            else:
                self.c.execute("UPDATE configuration SET quitbox=0")
                self.conn.commit()
            self.gui.label_saving_indicator.setText("Saved!")
        self.get_configuration_from_DB_and_set_settings()
    #Copy2Clipboard
    def copy2clipboard(self):
        copyvar = self.gui.label_output_window.text()
        QtWidgets.QApplication.clipboard().setText(copyvar)
    #Exit the App itself in a secure manner 
    def exit_app(self):
        self.c.execute("select quitbox from configuration")
        self.conn.commit()
        quitbox_result = self.c.fetchone()
        if quitbox_result[0] == 1:
            choice = QtWidgets.QMessageBox.warning(self, 'Quit Message!', "Really close the app?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.conn.close() 
                self.close()
            else:
                event.ignore()
        else:
            self.conn.close() 
            self.close()
    #Exit using the break command
    def closeEvent(self, event):
        self.c.execute("select quitbox from configuration")
        self.conn.commit()
        quitbox_result = self.c.fetchone()
        if quitbox_result[0] == 1:
            choice = QtWidgets.QMessageBox.warning(self, 'Quit Message!', "Really close the app?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if choice == QtWidgets.QMessageBox.Yes:
                self.conn.close() 
                self.close()
            else:
                event.ignore()
        else:
            self.conn.close() 
            self.close()





#
#Main program
#
#Call program class
#

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ISRT_Main_Window = QtWidgets.QWidget()
    rn_window = QtWidgets.QWidget()
    mgui = maingui()
    mgui.show()

    #Release Notes Viewer
    dbdir = Path(__file__).absolute().parent
    rn_conn = sqlite3.connect(str(dbdir / 'db/isrt_data.db'))
    rnc = rn_conn.cursor()
    rnc.execute("SELECT show_rn FROM release_info")
    show_rn = rnc.fetchone()
    rn_conn.commit()
    rn_conn.close()

    #Check if Release Notes shall be shown or not
    if show_rn[0] == 1:
        rngui = rngui()
        rngui.show()
    else:
        pass

    sys.exit(app.exec_())

