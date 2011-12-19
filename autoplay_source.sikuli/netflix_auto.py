#setThrowException(False)

#function exit the script
def exitScript(event):
    popup("You've managed to close Autoplay. Script will abort.")

    #kill the program (this is native python)
    import sys
    sys.exit()

#how often has next button been pressed?
counter = 0

#prompt user with input
numEpisodes = input("How many more episodes should this run for? \nexample: 4     |     Press Ctrl + F1 to cancel.")
#default success message that will play after script ends successfully
popMessage = "Done auto-playing episodes!\n" + str(counter) + " played."



#select a region
region = Screen().selectRegion("Where should the mouse-pointer go after autoplaying?")

#take a screenshot, then click that one
#scrnShot = Screen(0).capture("take a screenshot")


#add key listener. Listen for this key combo to exit the script. 
Env.addHotkey(Key.F1, KeyModifier.ALT+KeyModifier.CTRL, exitScript)

#loop through looking for the next for the # of times specified by user through input above
for x in range(int(numEpisodes)):
    #look for the button every 5 seconds (easier on CPU)
    while not ("PlayNextEpis.png"):
        wait(5)
        
    #Check for button existence (for 1 hr) 
    if exists("PlayNextEpis.png", 60 * 60 ): 
        click(exists("PlayNextEpis.png")) #(first click for focus)
        wait(2) #wait for load
        click(exists("PlayNextEpis.png")) #click again if still there (since we now certainly have focus)

        #increment the counter to show how many were played
        counter += 1
        #update play count here for how many episodes have played
        popMessage = "Done auto-playing episodes!\n" + str(counter) + " episodes auto-played."
        
        try:
            #move moouse to rest after clicking next episode. This was user selected earlier.
            mouseMove(region.getTopLeft()) #move to place selected
            #popup("found")
            
        except:
            #upon failure to find a valid region specified, pop this up, before terminating the script.
            popMessage = "Region selected earlier was invalid. So mouse move didn't work.\n" + str(counter) + " episodes autoplayed."
            #pass # we miss it
            #pass is just a placeholder.
         
    else:
        popMessage = "Auto-play aborted! Next button wasn't found for 1 hour. \n"
        break #terminate the loop
         
           
#popup before script ends with success or failure message.
popup(popMessage)


             
             




