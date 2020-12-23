# ISRT Insurgency Sandstorm RCON TOOL v0.7 released
This is a python3 and PyQt5/SQLite3-based RCON Tool for mapchanging, server monitoring and other basic RCON functionalities that help administering and controlling Insurgency Sandstorm Servers. I just released version 0.7 of it, again coming with a lot of hopefully good changes! I implemented all your feature requests, wishes and a couple of things I found convenient, like importing your v0.5/6 server database or having customizable commands and so on - see below! Of course I would love, if you test it and let me know, in case you find bugs or have additional feature or change requests! So, if you like, give it a shot. It only takes a couple of minutes to try it out - please watch the known error below. 

## For even more Information, look here: http://www.isrt.info

Report any bug or feature/change requests here or send me an e-mail/steam message: https://github.com/olli-e/ISRT-Insurgency-Sandstorm-RCON-Query-Tool/issues

### For Installation How-to, common problems, issue reporting, commands and the general usage, visit the Wiki pages via the link below: 
https://github.com/olli-e/ISRT-Insurgency-Sandstorm-RCON-Query-Tool/wiki

<center><img src="http://src.isrt.info/isrt_v0.7.jpg"></center>

#### Status: In development phase of full release - open for all ideas

## 1. Release Notes
- Renamed a couple of items for better understanding
- RCON commands are now automatically saved if not already in the history
- Inserted Security/Insurgents DropDown Menu for selecting travel commands
- Changed the Tell Map picture for better identification
- Added rcon commands quit and exit as valid commands
- Removed the automatic execution of custom commands on selection
- Added DB Table View to Server Manager for easier overview
- Discarded Night-View Maps, because you can't actually see anything in them
- Re-Designed the server info box and a couple other GUI elements
- Integrated Password Image display, removed the text display
- Added DB Table View for online players directly on query execution
- Aggregated the VAC/Ranked view
- Implemented Threading for monitor to prevent app freeze
- Added Maps Sheds, Stork_Castle_x Map, Frost, Temple, TORO and Bap
- Changed the Mapchanger so the Scenarios are based on what the server provides
- Removed the Side-Selector in the Mapchanger - now done by selecting the specific scenario.
- Modified 127.0.0.1 handling to auto-switch to LAN IP, due to a Windows bug.
- Removed auto-execution of commands selected from the Cutom Commands Dropdown menu
- Added server monitor to view all saved servers in one table overview

## 2. Known bugs
- When chosing random map change, the map is not updated correctly (NWI Server Bug reported - I unfortunately can't change false reporting on server side...)

## 3. Tested on the following virtualized systems:

### Windows (EXE-Version):
- Windows 7 (Version 6.1 Build 7601: SP1): Successfull - no errors after installlation of Update KB2533623  (windows6.1-kb2533623-x64) https://web.archive.org/web/20200412130407/https://www.microsoft.com/en-us/download/details.aspx?id=26764
- Windows 10 Home (Version 20H2 Build 19042.572): Successful - no errors
- Windows 10 Pro (Version 2004, Build 19041.630): Successful - no errors

* I have decided to focus on releases for Windows Clients as of v0.7, since I haven't even heard of anybody using it on Linux or Mac.

## 4. General Remarks, Feedback and stuff...
This release is proudly powered by <a href="https://www.advancedinstaller.com">AdvancedInstaller.com:
  
<img src="https://cdn.advancedinstaller.com/svg/pressinfo/AiLogoColor.svg" width="300"></a>

If you have any questions or feedback, please send me an e-mail to: madman@isrt.info - In case of feature requests or find any error in the software, please open an issue or in any other case, just write to me on our Discord: https://discord.gg/zEdTrgg

If you think that my software is cool and helps you do your daily tasks, why not buy me a coffee ;-) I love coffee. You can do so by clicking one of the buttons below!

<a href="https://www.buymeacoffee.com/oedelmeier"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=oedelmeier&button_colour=5176e6&font_colour=ffffff&font_family=Lato&outline_colour=ffffff&coffee_colour=FFDD00"></a>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate?hosted_button_id=RLSPYUNWLYA9Y)


Thanks and have a lovely day!

Oliver aka =[TCT]= Madman

