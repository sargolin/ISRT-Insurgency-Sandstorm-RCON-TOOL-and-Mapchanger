# ISRT-Insurgency-Sandstorm-RCON/Query-TOOL-and-Mapchanger - v0.3 released
This is a python (3.8.6) - and PyQt5/SQLite3-based RCON Tool for mapchanging and other basic RCON functionalities that help administering and controlling Insurgency Sandstorm Servers. The first version will be based on spezifanta's SourceWatch (https://github.com/spezifanta/SourceWatch) and ttk1's Py-Rcon (https://github.com/ttk1/py-rcon) - in the future this will be replaced by similar integrated python-based modules to get rid of third party modules I don't have any control over.

For the tracking of development and progress, as well as integrated feature requests, look here: https://trello.com/b/BHMJLISQ/isrt-insurgency-sandstorm-rcon-tool-ins

## 1. Introduction
The first stage will be the minimum viable product (MVP - see 2.) so you can see and try-out its basic functionality and have it working correctly, without any basic installation routine. I'll just pre-compile it for Windows 10 and Python 3.x directly while it's in development. In the future I'll add more and more functionality described in the features list and also add a proper installation/deinstallation routine:

<center><img src="http://gs.tct-gaming.com/isrt3.jpg"></center>

#### Status: In development phase - open for all ideas

## 2. MVP - first trial release - basic functionality:
- Actual Code for Remote Control including Mapchanger
- Graphical User Interface QT5
- Integrate all Standard Maps (open)
- Add Tell Map (open)
- Pre-compiled exe and .py (open)
- Select between day and night map (open)
- Using MCRCON (replaced by python integration
- Enter IP, Port and Password
- STDOUT Terminal
- Store IP, Port and PW in Textfile (open)

### 2.1 Features currently planned, but not yet implemented:
- Windows Installer
- Query Module Python - replace api.js
- RCON Module Python - replace MCRCON
- Save IP
- Save RCON Password
- Multiple Servers
- Store PW, IP, Port in Sqlite3 DB
- Multiple RCON Passwords
- Server Query Status
- Map Images
- Integrate custom maps
- Let users add own maps
- Allow custom travel commands
- Allow say command
- Integrate other rcon commands
- Integrate Kick
- Integrate Ban
- Allow Ban for specific time
- Integrate Reason why kicked/banned
- Select game mode for next map
- Using a minimalistic Discord Bot for map changes - role-based
- Database for all maps and travel commands

## 3. Installation and Deinstallation
- Download, Unzip in one folder and execute isrt_v0.3.py-file with Python 3.x and above or on Windows just call ISRT_v0.3.exe!
- For deinstalling, just delete folder or file

## 4. Commands and usage
It's all built inside call isrt_v0.3.py with Python or wihtout just shoot at ISRT_v0.3.exe - just use the entry fields and buttons - should work as designed - please report any errors as issues, please.

## 5. Testing and quality assurance
Tested on the following systems:
- Windows 7 Pro, 64 Bit (fails - not working - missing Visual C++ Runtime Redistributable Runtime Library + ?))
- Windows 10 Pro, 64 Bit (working)
- Windows 10 Home, 64 Bit (working)
- Debian 10.6
-- Ensure Python3 is installed - I tested with 3.7.3 that came with the standard Debian install -> sudo apt-get install python3
-- Ensure PIP is installed -> sudo apt-get install python3-pip
-- Ensure PyQt5 is install -> python3 -m pip install PyQt5
-- Ensure the correct X11 Libx are installed -> sudo apt-get install libx11-xcb1 libqt5x11extras5
- Ubuntu 20.04 (Linux Mint XFCE), 64 Bit
 
## 6. General Remarks, Feedback and stuff...
If you have any questions or feedback, please send me an e-mail to: oe-at-edelmeier.org - In case of feature requests or find any error in the software, please open an issue or in any other case, just write to me on our Discord: https://discord.gg/zEdTrgg

If you think that my software is cool and helps you do your daily tasks, why not buy me a coffee ;-) You can do so here: https://www.buymeacoffee.com/oedelmeier or just click the button below

<a href="https://www.buymeacoffee.com/oedelmeier" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 150px !important;"></a>

Thanks and have a lovely day!
Oliver

