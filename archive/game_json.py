#import places 
import puzzles
import adventurelib as adv
import random
import os
import json
import utils

CURR_PLAYER=None  #json object
CURR_CITY=None    #json object  
CURR_CELL=None    #x,x
CURR_ZONE=None    #int from 1 to 12

previous_context=None
current_context=None

def get_players():
    with open('players.json') as f:
        players = json.load(f)
        return players['players'].keys()
    
def load_player(player:str) -> json:
    found={}
    with open('players.json') as f:
        players = json.load(f)
        found[player]=players['players'][player]
        return found

def update_player(player :str,attribute : str,value):
    with open('players.json',"w") as f:
        players=json.load(f)
        players[player][attribute]=value
        json.dump(players,f)

        
def load_city(city:str) -> json:
    #load places
    with open('places.json') as f:
        world = json.load(f)
        city=utils._json_search_key(world,city)
        return city
    
def prompt():
    return f'{CURR_CITY["aliases"]}:{CURR_CELL} > '

def main():
    global CURR_PLAYER,CURR_CITY,CURR_CELL,CURR_ZONE

    os.system('cls||clear')
    
    #choose player
    print("choose the player:")
    players=get_players()
    print(",".join(players))
    while True:
        user_input=input()
        if user_input in players:
            CURR_PLAYER=load_player(user_input)
            break
    
    #load player infor
    player_infor=next(iter(CURR_PLAYER.values()))
    city=player_infor['current city']
    CURR_CITY= load_city(city)[city]
    CURR_CELL=player_infor['current cell']
    CURR_ZONE=1 #need to fix
     
    adv.prompt = prompt

    #Active the robot. Just once. 
    if player_infor['puzzles pass']:
        if puzzles.game_passcode():
            adv.say(f"""Experiment {random.randint(1000000,9000000)} activated!
                Me Jo is your assistant and will server you 24/7 for free.
                Say help to get the command you can use.
                Say jo to ask me some questions.""")
            #set puzzles to false so that no more play.
            update_player(next(iter(CURR_PLAYER.keys())),"puzzles pass",False)
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

    items= check_items(CURR_CELL)
    if items: 
        adv.say(f"You find {','.join(items)}.")
    #check_NPC(CURR_CELL)
    #check_monsters(CURR_CELL)
    #check_events(CURR_CELL)

def check_items(cell):
    with open('items.json') as f:
        items = json.load(f)
        loc=str(CURR_ZONE)+':'+CURR_CELL
        if loc in items.keys():
            return list(items[loc]['items'].keys())

@adv.when("take ITEM")
def take(item):
    items=item+'.'+next(iter(CURR_PLAYER.values()))["items"]
    update_player(player,"items",items)

def check_NPC(cell):
    pass
    
def check_monsters(cell):
    pass

def check_events(cell):
    pass

main()
