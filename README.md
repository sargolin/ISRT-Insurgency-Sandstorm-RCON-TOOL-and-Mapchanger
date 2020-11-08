# ISRT-Insurgency-Sandstorm-RCON/Query-TOOL-and-Mapchanger - v0.5 released
This is a python (3.8.6) - and PyQt5/SQLite3-based RCON Tool for mapchanging and other basic RCON functionalities that help administering and controlling Insurgency Sandstorm Servers. The first version will be based on spezifanta's SourceWatch (https://github.com/spezifanta/SourceWatch) and ttk1's Py-Rcon (https://github.com/ttk1/py-rcon) - in the future this will be replaced by similar integrated python-based modules to get rid of third party modules I don't have any control over.

For the tracking of development and progress, as well as integrated feature requests, look here: https://trello.com/b/BHMJLISQ/isrt-insurgency-sandstorm-rcon-tool-ins

## 0. Release Notes
- Implemented a lot of bug fixes and error handling routines, direct rcon commands, map changer and progess bar for map changer
- Put in a link for issue reporting
- Added copy of console content
- Made content of RCOn help and console content mark- and copy-able (if those words exist ;-) )
- Inserted Map view thumbnails for the running maps
- Inserted a lot of custom maps
- Made the entire app resizable

### 0.1 Known bugs
- List Player command produces a weird output that has to be structured - next release

## 1. Introduction
The first stage will be the minimum viable product (MVP - see 2.) so you can see and try-out its basic functionality and have it working correctly, without any basic installation routine. I'll just pre-compile it for Windows 10 and Python 3.x directly while it's in development. In the future I'll add more and more functionality described in the features list and also add a proper installation/deinstallation routine:

<center><img src="http://gs.tct-gaming.com/isrt05.jpg"></center>
<p>
<center><img src="http://gs.tct-gaming.com/isrt05a-jpg"></center>

#### Status: In development phase of full release - open for all ideas

## 2. Features currently in implementation:
- Windows Installer 
- Server Query Status time-based
- Map Images Integration
- Full Monitor view for up to nine servers at a time
- Integrate custom mapswitch
- Let users add own maps
- Allow custom travel commands
- Integrate Kick form
- Integrate Ban form
- Allow Ban for specific time in a form
- Integrate Reason why kicked/banned
- Select game mode for next map
- Database entries for all maps and travel commands

### 2.1 MVP - finished:
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

## 3. Installation
- On Windows: Download "isrt_version.exe.zip", Unzip in one folder and execute ISRT_version.exe! (Make sure that folders db and img are in the same folder as the exe file!!!)
- On Linux: Download the entire git.zip and unzip - execute isrt_version.py and ensure that the pre-requisites in topic 5 are met!
- For un-installing, just delete folder or file

## 4. Commands and usage
It's all built inside call isrt_version.py with Python or wihtout just shoot at ISRT_version.exe - just use the entry fields and buttons or the server manager, if you want to store any data - should work as designed - please report any errors as issues. It also has a simple rcon-help integrated for you to look at syntax and commands.

## 5. Tested on the following systems:
Success:
- Windows 10 Pro, 64 Bit (working)
- Windows 10 Home, 64 Bit (working)
- Debian 10.6 (working -> Ensure Python3 and libPyQt5 are installed -> "sudo apt-get install python3 python3-pyqt5")
- Ubuntu 20.04 (Linux Mint XFCE), 64 Bit (working -> Ensure Python3 and libPyQt5 are installed -> "sudo apt-get install python3 python3-pyqt5")

Fail:
- Windows 7 Pro, 64 Bit (fails - not working - missing Visual C++ Runtime Redistributable Runtime Library + ?)

## 6. General Remarks, Feedback and stuff...
If you have any questions or feedback, please send me an e-mail to: isrt@edelmeier.org - In case of feature requests or find any error in the software, please open an issue or in any other case, just write to me on our Discord: https://discord.gg/zEdTrgg

If you think that my software is cool and helps you do your daily tasks, why not buy me a coffee ;-) You can do soby clicking the button below!

<a href="https://www.buymeacoffee.com/oedelmeier" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 150px !important;"></a>

Thanks and have a lovely day!
Oliver

