from ohbot import ohbot

ohbot.reset()

# blinking
ohbot.move(ohbot.LIDBLINK, 0)
ohbot.wait(0.4)
ohbot.move(ohbot.LIDBLINK, 10)


# 2nd parameter (False) means ohbot will continue moving while talking
# 3rd parameter (True) means ohbot will lipsync to the text
ohbot.say("If you're blue, and you don't know where to go to", False, True)
# turning the eyes
ohbot.move(ohbot.EYETURN, 10)
ohbot.wait(0.6)
ohbot.move(ohbot.EYETURN, 0)

# blinking
ohbot.move(ohbot.LIDBLINK, 0)
ohbot.wait(0.4)
ohbot.move(ohbot.LIDBLINK, 10)
ohbot.wait(2)
ohbot.say("Why don't you go where fashion sits?", False, True)

# Moving the eyes
ohbot.move(ohbot.EYETURN, 7)
ohbot.move(ohbot.EYETILT, 7)
ohbot.wait(0.5)  # Wait for .5 seconds
ohbot.move(ohbot.HEADTURN, 7, spd=1)  # moving the head to the random number at speed 1 (slow)
ohbot.move(ohbot.HEADNOD, 7, spd=1)
ohbot.wait(0.5)  # Wait for .5 seconds
ohbot.move(ohbot.EYETURN, 5)
ohbot.move(ohbot.EYETILT, 5)


ohbot.say("Putting on the ritz", False, True)
# blinking
ohbot.move(ohbot.LIDBLINK, 0)
ohbot.wait(0.4)
ohbot.move(ohbot.LIDBLINK, 10)

ohbot.move(ohbot.HEADTURN, 5, spd=3)
ohbot.move(ohbot.HEADNOD, 5, spd=3)
ohbot.wait(2)  # Wait for 2 seconds


ohbot.say("Dressed up like a million-dollar trouper", False, True)

ohbot.wait(.5)
ohbot.say("Trying hard to look like Gary Cooper", False, True)
ohbot.say("Super duper", False, True)

ohbot.wait(1) 
ohbot.say("If you're blue, and you don't know where to go to", False, True)
ohbot.wait(.5)  # Wait for 2 seconds
ohbot.say("Why don't you go where fashion sits?", False, True)
ohbot.say("Puttin' on the Ritz", False, True)

ohbot.wait(2)  # Wait for 2 seconds
ohbot.say("Puttin' on the Ritz", False, True)
ohbot.say("Puttin' on the Ritz", False, True)
ohbot.say("Puttin' on the Riiiitzzzz", False, True)

# close ohbot at the end.
ohbot.reset()
ohbot.close()
