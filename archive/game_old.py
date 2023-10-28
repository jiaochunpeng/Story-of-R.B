import places 
import puzzles
from adventurelib import *
import random
import os

previous_context=None

def main():
    global current_room
    os.system('cls||clear')
    set_context('North Kindom.Ottawa')
    current_room=places.Ottawa
    if puzzles.game_passcode():
        say(f"""Experiment {random.randint(1000000,9000000)} activated!
                Me Jo is your assistant and will server you 24/7 for free.
                Say help to get the command you can use.
                Say jo to ask me some questions.""")
    start()
    
@when('jo')
def activate_Jo():
    say(""" Play a game before ask a question.""")
    if puzzles.game_guessnumber():
        say("You good! Shot your questions.")
        global previous_context
        previous_context=get_context()
        set_context("Q&A mode")

@when('what your name',context="Q&A mode",question='yourname')
@when('where am i',context="Q&A mode",question='where')
@when('who am i',context="Q&A mode",question='name')
@when('who are you',context="Q&A mode",question='yourwho')
@when('why me here',context="Q&A mode",question='whyhere')
@when('bye',context="Q&A mode",question='bye')
def myname(question):
    match question:
        case 'yourname' | 'yourwho':
            say('My name is Jo. You know already. Dumb.')
        case 'where':
            say(f'you are in {current_room.aliases},{current_room}')
        case 'name':
            say('your name is Alice? I dont know')
        case 'whyhere':
            say('why you ask why you here?')
        case 'bye':
            say('%&^(#$&)!')
            set_context(previous_context)

main()