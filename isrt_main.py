#ISRT - Insurgency Sandstorm RCon Tool; 12.10.2020, Sargolin aka @ Madman
#In case of questions: oe@edelmeier.org
#Git: https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-TOOL-and-Mapchanger.git
#v0.2 -Creation of basic structure plus database file
#Database: ./db/isrt_data.db
#Main-program: This File
#Imported classes/functions/libraries:

#Importing required classes and libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, subprocess, shlex, os, requests, platform, query
from rcon import Console


#Execute RCON Command, when called
def rconserver():
    console = Console(host=serverhost, password=rconpassword, port=rconport)
    console.command(rconcommand)
    console.close() 

#Execute Query Command, when called
def queryserver():
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

#Define variables
serverhost = "93.186.198.185"
queryport = 27016
rconport = 27017
rconpassword = "Rfcd2025"
rconcommand = "help"

#Call main functions
rconserver()
queryserver()


