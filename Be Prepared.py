from ohbot import ohbot

ohbot.reset()

# Audio sync timestamps (seconds into the video)
SYNC = {
    "line1": 12.50,
    "line2": 15.00,
    "line3": 17.20,
    "line4": 19.00,
    "line5": 21.00,
    "line6": 23.00,
    "line7": 25.00,
    "line8": 27.00,
    "hyena_choir": 29.00,
    "where_do_we_feature": 34.00,
    "listen_to_teacher": 35.00,
    "reward_start": 36.00,
    "reward_mid": 38.00,
    "reward_pre": 40.00,
    "reward_final": 42.00,
    "coup_century": 44.00,
    "coup_scam": 48.00,
    "final_be_prepared": 80.00
}

# Helper functions
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

    ohbot.say(text)
    blink()
    express(eye_turn=eye, head_turn=head, head_nod=nod)

def hyena_react(direction, sync_key):
    express(head_turn=direction, head_nod=5, wait=0.6)
    express(head_turn=0, head_nod=0, wait=0.3)

scar_line("I know that your powers of retention", "line5", eye=0, head=0, nod=2)
scar_line("Are as wet as a warthog's backside", "line6", eye=10, head=5, nod=1)
scar_line("But thick as you are, pay attention!", "line7", eye=0, head=-5, nod=2)
scar_line("My words are a matter of pride", "line8", eye=-10, head=-10, nod=2)

'''
It's clear from your vacant expressions
The lights are not all on upstairs
But we're talking kings and successions
Even you can't be caught unawares
'''

'''
So prepare for a chance of a lifetime
Be prepared for sensational news
A shining new era
Is tiptoeing nearer
'''
hyena_react(-30, "hyena_choir")
hyena_react(30, "hyena_choir")

hyena_react(-30, "where_do_we_feature")
scar_line("Just listen to teacher!", "listen_to_teacher", eye=5, head=5, nod=2)

scar_line("I know it sounds sordid, but you'll be rewarded", "reward_start", eye=10, head=0, nod=1)
scar_line("When at last I am given my dues", "reward_mid", eye=-10, head=-5, nod=1)
scar_line("And injustice deliciously squared", "reward_pre", eye=0, head=0, nod=2)
scar_line("Be prepared!", "reward_final", eye=0, head=0, nod=3)

# Ohbot doesnt speak for a small while as background singers sing 1 line

'''
Of course with quid pro quo, you're expected
To take certain duties on board
The future is littered with prizes
And though I'm the main addressee
The point that I must emphasize is
You won't get a sniff without me
'''

scar_line("So prepare for the coup of the century", "coup_century", eye=0, head=0, nod=2)
scar_line("Be prepared for the murkiest scam", "coup_scam", eye=5, head=5, nod=2)
scar_line("Meticulous planning", "coup_scam", eye=-5, head=-5, nod=1)
scar_line("Tenacity spanning", "coup_scam", eye=5, head=5, nod=1)
scar_line("Decades of denial", "coup_scam", eye=0, head=0, nod=1)

scar_line("Is simply why I'll", "coup_scam", eye=0, head=0, nod=1)
scar_line("Be king undisputed", "coup_scam", eye=0, head=0, nod=2)
scar_line("Respected, saluted", "coup_scam", eye=0, head=0, nod=2)
scar_line("And seen for the wonder I am", "coup_scam", eye=0, head=0, nod=2)

scar_line("Yes, my teeth and ambitions are bared", "coup_scam", eye=0, head=0, nod=2)
scar_line("Be prepared!", "final_be_prepared", eye=0, head=0, nod=3)

# Final echo with hyenas
hyena_react(-30, "final_be_prepared")
hyena_react(30, "final_be_prepared")

scar_line("Be prepared!", "final_be_prepared", eye=0, head=0, nod=3)

ohbot.move(ohbot.HEADNOD, 0)
ohbot.move(ohbot.HEADTURN, 0)

# close ohbot at the end.
ohbot.wait(.5)  # Wait for 2 seconds
ohbot.reset()
ohbot.close()

