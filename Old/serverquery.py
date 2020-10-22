#ISRT Tool, Basic program code, Python

#Importing neccessary libraries and modules
import query

#Execute query and assign dict to variables
def getdata():
    global server, pwcheck, vaccheck, mutators, ranked, coop, versus, mods, servernetworkdetails, serverinfo, servergamedetails, serverrules, serverruledetails
    server = query.Query('93.186.198.185', 27016)
    serverinfo = (server.info())
    servergamedetails = (serverinfo['info'])
    serverrules = (server.rules())
    serverruledetails = (serverrules['rules'])
    servernetworkdetails = (serverinfo['server'])
    pwcheck = (servergamedetails['server_password_protected'])
    vaccheck = (servergamedetails['server_vac_secured'])
    mutators = (servergamedetails['server_tags'])
    ranked = (serverruledetails['RankedServer_b'])
    coop = (serverruledetails['Coop_b'])
    versus = (serverruledetails['Versus_b'])
    mods = (serverruledetails['Mods_b'])
   


#Check for correct setting of Servervars and assign Yes/No to these
def checkservervars():
    global servermodcheck, serverpwcheck, servervaccheck, serverrulecheck, servercoopcheck
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


#Print out the collected data to console
def printdata():
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



#Call main functions
getdata()
checkservervars()
printdata()
