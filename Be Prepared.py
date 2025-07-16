from ohbot import ohbot

ohbot.reset()

# Audio sync timestamps (seconds into the video) https://www.youtube.com/watch?v=2ScpnOlFWaA
SYNC = {
    "line1": 09.00, # I know that your powers of retention
    "line2": 13.00, # Are as wet as a warthog's backside
    "line3": 17.00, # But thick as you are, pay attention!
    "line4": 21.00, # My words are a matter of pride
    "line5": 25.00, # It's clear from your vacant expressions
    "line6": 29.00, # The lights are not all on upstairs
    "line7": 33.00, # But we're talking kings and successions
    "line8": 36.00, # Even you can't be caught unawares
    "line9": 40.00, # So prepare for a chance of a lifetime
    "line10": 44.00, # Be prepared for sensational news
    "line11": 49.00, # A shining new era
    "line12": 50.00, # Is tiptoeing nearer
    "where_do_we_feature": 53.00, # And where do we feature?
    "listen_to_teacher": 54.50, # Just listen to teacher!
    "line13": 56.00, # I know it sounds sordid, but you'll be rewarded
    "line14": 60.00, # When at last I am given my dues
    "line15": 64.00, # And injustice deliciously squared
    "line16": 68.00, # Be prepared!
    "hyena_choir": 73.00, # (When background singers start)
    "line17": 80.00, # Of course with quid pro quo, you're expected
    "line18": 84.50, # To take certain duties on board
    "line19": 88.00, # The future is littered with prizes
    "line20": 92.00, # And though I'm the main addressee
    "line21": 96.00, # The point that I must emphasize is
    "line22": 100.00, # You won't get a sniff without me
    "line23": 103.00, # So prepare for the coup of the century
    "line24": 107.50, # Be prepared for the murkiest scam
    "line25": 111.50, # Meticulous planning
    "line26": 113.00, # Tenacity spanning
    "line27": 116.00, # Decades of denial
    "line28": 118.50, # Is simply why I'll
    "line29": 119.50, # Be king undisputed
    "line30": 120.50, # Respected, saluted
    "line31": 123.00, # And seen for the wonder I am
    "line32": 127.00, # Yes, my teeth and ambitions are bared
    "line33": 130.00, # Be prepared!
    "line34": 138.50, # Be prepared!
}

def blink(duration=0.3):
    ohbot.move(ohbot.LIDBLINK, 0)
    ohbot.wait(duration)
    ohbot.move(ohbot.LIDBLINK, 10)

def express(eye_turn=0, head_turn=0, head_nod=0, wait=0.4, spd=2):
    ohbot.move(ohbot.EYETURN, eye_turn)
    ohbot.move(ohbot.HEADTURN, head_turn, spd=spd)
    ohbot.move(ohbot.HEADNOD, head_nod, spd=spd)
    ohbot.wait(wait)

def scar_line(text, sync_key, eye=0, head=0, nod=0):
    ohbot.wait(SYNC[sync_key])
    ohbot.say(text)
    blink()
    express(eye_turn=eye, head_turn=head, head_nod=nod)

def hyena_react(direction, sync_key):
    ohbot.wait(SYNC[sync_key])
    express(head_turn=direction, head_nod=5, wait=0.6)
    express(head_turn=0, head_nod=0, wait=0.3)

# Maybe sync keys should be line 2 - line 1 = sync etc. If its using ohbot.wait otherwise it will wait too long
# Experimenting with this 
scar_line("I know that your powers of retention", "line1", eye=0, head=0, nod=2)
ohbot.wait(SYNC["line2"] - SYNC["line1"]) # Wait for the difference between lines
scar_line("Are as wet as a warthog's backside", "line2", eye=10, head=5, nod=1)
ohbot.wait(SYNC["line3"] - SYNC["line2"]) # Wait for the difference between lines
scar_line("But thick as you are, pay attention!", "line3", eye=0, head=-5, nod=2)
ohbot.wait(SYNC["line4"] - SYNC["line3"]) # Wait for the difference between lines
scar_line("My words are a matter of pride", "line4", eye=-10, head=-10, nod=2)

scar_line("It's clear from your vacant expressions", "line5", eye=0, head=5, nod=1)
scar_line("The lights are not all on upstairs", "line6", eye=10, head=0, nod=1)
scar_line("But we're talking kings and successions", "line7", eye=-10, head=5, nod=1)
hyena_react(-30, "line8")
scar_line("Even you can't be caught unawares", "line8", eye=0, head=0, nod=2)

scar_line("So prepare for a chance of a lifetime", "line9", eye=0, head=0, nod=2)
scar_line("Be prepared for sensational news", "line10", eye=5, head=5, nod=2)
scar_line("A shining new era", "line11", eye=-5, head=-5, nod=1)
scar_line("Is tiptoeing nearer", "line12", eye=0, head=0, nod=1)


scar_line("And where do we feature?", "where_do_we_feature", eye=0, head=0, nod=1)
hyena_react(-30, "listen_to_teacher")
scar_line("Just listen to teacher!", "listen_to_teacher", eye=5, head=5, nod=2)

scar_line("I know it sounds sordid, but you'll be rewarded", "line13", eye=10, head=0, nod=1)
scar_line("When at last I am given my dues", "line14", eye=-10, head=-5, nod=1)
scar_line("And injustice deliciously squared", "line15", eye=0, head=0, nod=2)
scar_line("Be prepared!", "line16", eye=0, head=0, nod=3)

hyena_react(-30, "hyena_choir")
hyena_react(30, "hyena_choir")

# Background singers’ break until next line
ohbot.wait(SYNC["line17"])
scar_line("Of course with quid pro quo, you're expected", "line17", eye=5, head=5, nod=1)
scar_line("To take certain duties on board", "line18", eye=-5, head=-5, nod=1)
scar_line("The future is littered with prizes", "line19", eye=0, head=0, nod=2)
scar_line("And though I'm the main addressee", "line20", eye=5, head=0, nod=1)
scar_line("The point that I must emphasize is", "line21", eye=-5, head=0, nod=1)
scar_line("You won't get a sniff without me", "line22", eye=0, head=0, nod=2)

scar_line("So prepare for the coup of the century", "line23", eye=0, head=0, nod=2)
scar_line("Be prepared for the murkiest scam", "line24", eye=5, head=5, nod=2)
scar_line("Meticulous planning", "line25", eye=-5, head=-5, nod=1)
scar_line("Tenacity spanning", "line26", eye=5, head=5, nod=1)
scar_line("Decades of denial", "line27", eye=0, head=0, nod=1)

scar_line("Is simply why I'll", "line28", eye=0, head=0, nod=1)
scar_line("Be king undisputed", "line29", eye=0, head=0, nod=2)
scar_line("Respected, saluted", "line30", eye=0, head=0, nod=2)
scar_line("And seen for the wonder I am", "line31", eye=0, head=0, nod=2)

scar_line("Yes, my teeth and ambitions are bared", "line32", eye=0, head=0, nod=2)
scar_line("Be prepared!", "line33", eye=0, head=0, nod=3)

# Final movement and line
hyena_react(-30, "line34")
scar_line("Be prepared!", "line34", eye=0, head=0, nod=3)

ohbot.move(ohbot.HEADNOD, 0)
ohbot.move(ohbot.HEADTURN, 0)

# Finish
ohbot.wait(0.5)
ohbot.reset()
ohbot.close()
