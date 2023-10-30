#import places 
import puzzles
import adventurelib as adv
import random
import os
import utils
import player
import places
import items


CURR_PLAYER=None  #player name
CURR_CITY=None    #city name  
CURR_CELL=None    #x,x
CURR_ZONE=None    #int from 1 to 12

previous_context=None
current_context=None
player_info=None
city_info=None
        
   
def prompt():
    return f'{CURR_CITY}:{CURR_CELL} > '

def main():
    global CURR_PLAYER,CURR_CITY,CURR_CELL,CURR_ZONE

    os.system('cls||clear')
    
    #choose player
    print("choose the player:")
    players=player.get_players()
    print(",".join(players))
    while True:
        user_input=input()
        if user_input in players:
            CURR_PLAYER=user_input
            break
    
    #load player infor
    player_info=player.load_player(CURR_PLAYER)[0]
    CURR_CITY=player_info['current_city']
    city_info=places.load_place(CURR_CITY)[0]
    CURR_CELL=player_info['current_cell']
    CURR_ZONE=city_info['zone']
     
    adv.prompt = prompt

    #Active the robot. Just once. 
    flags=player_info['flags'].split(',')
    if flags[0]=='1':
        if True or puzzles.game_passcode():
            adv.say(f"""Experiment {random.randint(1000000,9000000)} activated!
                Me Jo is your assistant and will server you 24/7 for free.
                Say help to get the command you can use.
                Say jo to ask me some questions.""")
            #set puzzles to false so that no more play.
            flags[0]='0'
            player.update_player(CURR_PLAYER,'flags',','.join(flags))
    adv.start()
    
@adv.when('jo')
def activate_Jo():
    global previous_context
    previous_context=adv.get_context()
    
    if CURR_PLAYER['puzzles number']:
        adv.say(""" Play a game before ask a question.""")
        if puzzles.game_guessnumber():
            adv.say("You good! Shot your questions.")
            adv.set_context("Q&A mode")
    else:   adv.set_context("Q&A mode")        

@adv.when('what your name',context="Q&A mode",question='yourname')
@adv.when('where am i',context="Q&A mode",question='where')
@adv.when('who am i',context="Q&A mode",question='name')
@adv.when('who are you',context="Q&A mode",question='yourwho')
@adv.when('why me here',context="Q&A mode",question='whyhere')
@adv.when('bye',context="Q&A mode",question='bye')
def questions(question):
    match question:
        case 'yourname' | 'yourwho':
            adv.say('My name is Jo. You know already. Dumb.')
        case 'where':
            adv.say(f'you are in {CURR_CITY["aliases"]},{CURR_CITY["description"]}')
        case 'name':
            adv.say('your name is Alice? I dont know')
        case 'whyhere':
            adv.say('why you ask why you here?')
        case 'bye':
            adv.say('%&^(#$&)!')
            adv.set_context(previous_context)

@adv.when('right',direction='right')
@adv.when('r',direction='right')
@adv.when('left',direction='left')
@adv.when('l',direction='left')
@adv.when('up',direction='up')
@adv.when('u',direction='u')
@adv.when('down',direction='down')
@adv.when('d',direction='down')
def move(direction):
    global CURR_CELL
    x=int(CURR_CELL.split(',')[0])
    y=int(CURR_CELL.split(',')[1])
    match direction:
        case "right" | "r":  
            if x<10:  x+=1
        case "left" | "l": 
            if x>1: x-=1
        case "up" | "u": 
            if y<10: y+=1
        case "down" | "d": 
            if y<1: y-=1
    CURR_CELL=str(x)+','+str(y)

    #check_NPC(CURR_CELL)
    #check_monsters(CURR_CELL)
    #check_events(CURR_CELL)
@adv.when("take ITEM")
def take(item):
    player.add_to_inventory(CURR_PLAYER, item,1)
    items.remove_item(CURR_ZONE,CURR_CELL,item)

@adv.when("look")
def look():
    available_items= items.get_items(CURR_ZONE,CURR_CELL)
    if len(available_items)>0: 
        adv.say(f"You find {','.join(available_items)}.")
    else:
        adv.say('Nothing around.')

@adv.when('inventory')
@adv.when('i')
def inv():
    inv=player.get_inventory(CURR_PLAYER)
    if len(inv)>0:
        adv.say(f"you have {','.join(inv)}")
    else:
        adv.say('You have nothing.')


def check_NPC(cell):
    pass
    
def check_monsters(cell):
    pass

def check_events(cell):
    pass

main()
