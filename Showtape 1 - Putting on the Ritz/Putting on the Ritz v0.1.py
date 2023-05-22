from ohbot import ohbot
import time

ohbot.reset()

# blinking
ohbot.move(ohbot.LIDBLINK, 0)
ohbot.wait(0.4)
ohbot.move(ohbot.LIDBLINK, 10)


# 1st verse
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

ohbot.say("Why don't you go where fashion sits?", False, True)

# Moving the eyes
ohbot.move(ohbot.EYETURN, 7)
ohbot.move(ohbot.EYETILT, 7)
time.sleep(.5)  # Wait for .5 seconds
ohbot.move(ohbot.HEADTURN, 7, spd=1)  # moving the head to the random number at speed 1 (slow)
ohbot.move(ohbot.HEADNOD, 7, spd=1)
time.sleep(.5)  # Wait for .5 seconds
ohbot.move(ohbot.EYETURN, 5)
ohbot.move(ohbot.EYETILT, 5)
# blinking
ohbot.move(ohbot.LIDBLINK, 0)
ohbot.wait(0.4)
ohbot.move(ohbot.LIDBLINK, 10)
time.sleep(1)  # Wait for 1 second

ohbot.say("Putting on the ritz", False, True)

# close ohbot at the end.
ohbot.reset()
ohbot.close()
