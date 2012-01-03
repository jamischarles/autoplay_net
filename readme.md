
## Description:
This is a script that automates the clicking of the "**Next Episode**" button on the netflix screen. It uses the <a href="http://sikuli.org/">Sikuli</a> program (open source GUI Automation tool released by MIT).

## Instructions:
1. <a href="http://sikuli.org/">Download and install Sikuli</a> (the program that automates your UI)
2. Download this script **autoplay_source.sikuli**  
3. Run the **autoplay_source.sikuli** file (double clicking, should open up the sikuli IDE program)
4. Click "Run" in the Skikuli IDE program.

This will prompt you for how many times you want the "next episode" button to be clicked (how many episodes to play). 

You will then be asked to draw a zone on the screen where the cursor should rest after clicking the "next episode" button.

After that, the script will look for the "next episode" button to appear, and if found, will automate the clicking of it.

The script will end after the # of clicks has been reached that you defined in the first popup.

## Ending the script early
If you'd like to terminate the script early, hold down:<br>
**Ctrl + Alt + F1** (a mac will likely require Fn as well)


## Supported Operating Systems:
Sikuli works on Windows, Mac OSX, Linux. I've only tested on Mac. Tell me if you run into issues on the other platforms.

## Known Issues / Limitations:
- You can only mark the cursor resting point (after a click) on the primary display. 
- Automating currently only work on the primary display.

## Questions / Bug Notifications
If you have questiongs / problems / comments, use Github to create the issues, or contact me via this form:<br>
<a href="http://jamischarles.com/contact.php">http://jamischarles.com/contact.php</a>
