# ISRT Insurgency Sandstorm RCON TOOL v0.6 released (Win/Lin/Mac)
This is a python3 (3.8.6) - and PyQt5/SQLite3-based RCON Tool for mapchanging, server monitoring and other basic RCON functionalities that help administering and controlling Insurgency Sandstorm Servers. That said, I just released version 0.6 of it, again coming with a lot of new features that I list down below in the release notes! I implemented all your feature requests, wishes and a couple of things I found convenient, like importing your v0.5 server database or having customizable commands. Of course I would love, if you test it and let me know, in case you find bugs or have additional feature or change requests! So, if you like, give it a shot. It only takes a couple of minutes to try it out - please watch the known errors below. In the future I'll add more and more functionality and also add a proper installation/de-installation routine:

Report any bug or feature/change requests here or send me an e-mail/steam message: https://github.com/olli-e/ISRT-Insurgency-Sandstorm-RCON-Query-Tool/issues

### For Installation How-to, common problems, issue reporting, commands and the general usage, visit the Wiki pages via the link below: 
https://github.com/sargolin/ISRT-Insurgency-Sandstorm-RCON-Query-Tool/wiki

<center><img src="http://src.isrt.info/isrt_v0.6.jpg"></center>

#### Status: In development phase of full release - open for all ideas

## 1. Release Notes
- Re-Designed to "tabbed" layout for easier usage
- Customizable RCON buttons are available now
- Database can be backed up, imported or combined (Yes, you can import your v0.5 database now!)
- Imported the new maps: Frost, Stork_Castle_x, Temple and Toro from mod.io
- Added Wiki reference
- Added customizable RCON commands as Custom Command Manager - save, add, delete
- Now working on Windows 7 and Mac OS as well

## 2. Known bugs
- List Player command produces a weird output that has to be structured - working on it - solution found, but a lot more difficult than I thought
- Program throws an error if using 127.0.0.1 as IP - SourceQuery bug - will change it in the next version - switching sourcequery code - use your LAN IP instead

## 3. Tested on the following virtualized systems:

### Windows (EXE-Version):
- Windows 7 (Version 6.1 Build 7601: SP1): Successfull - no errors after installlation of Update KB2533623  (windows6.1-kb2533623-x64) https://web.archive.org/web/20200412130407/https://www.microsoft.com/en-us/download/details.aspx?id=26764
- Windows 10 Home (Version 20H2 Build 19042.572): Successful - no errors
- Windows 10 Pro (Version 2004, Build 19041.630): Successful - no errors

### Linux (Python 3.7/8 .py-Version) -> Ensure Python3 and libPyQt5 are installed -> "sudo apt-get install python3 python3-pyqt5":
- Debian 10.6: Successful - no errors
- Ubuntu - Linux Mint 20.04: Successful - no errors

### Mac OSX (Python 3.9 .py-Version) -> Ensure Python3.X and PyQt5 are installed:
- Mac OS Catalina: Successful - no errors

## 4. General Remarks, Feedback and stuff...
If you have any questions or feedback, please send me an e-mail to: isrt@edelmeier.org - In case of feature requests or find any error in the software, please open an issue or in any other case, just write to me on our Discord: https://discord.gg/zEdTrgg

If you think that my software is cool and helps you do your daily tasks, why not buy me a coffee ;-) I love coffee. You can do so by clicking one of the buttons below!

<a href="https://www.buymeacoffee.com/oedelmeier" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 150px !important;"></a>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?hosted_button_id=RLSPYUNWLYA9Y)


Thanks and have a lovely day!

Oliver aka =[TCT]= Madman

