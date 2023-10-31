#import places 
import puzzles
import adventurelib as adv
import random
import os
import utils
import player
import places
import items
import NPC
import global_vars as gv

  
def prompt():
    return f'{gv.curr_city}:{gv.curr_cell} > '

def main():

    os.system('cls||clear')
    
    #choose player
    print("choose the player:")
    players=player.get_players()
    print(",".join(players))
    while True:
        user_input=input()
        if user_input in players:
            gv.curr_player=user_input
            break
    
    #load player infor
    gv.player_info=player.load_player(gv.curr_player)[0]
    gv.curr_city=gv.player_info['current_city']
    gv.city_info=places.load_place(gv.curr_city)[0]
    gv.curr_cell=gv.player_info['current_cell']
    gv.curr_zone=gv.city_info['zone']
     
    adv.prompt = prompt

    #Active the robot. Just once. 
    flags=gv.player_info['flags'].split(',')
    if flags[0]=='1':
        if True or puzzles.game_passcode():
            adv.say(f"""Experiment {random.randint(1000000,9000000)} activated!
                Me Jo is your assistant and will server you 24/7 for free.
                Say help to get the command you can use.
                Say jo to ask me some questions.""")
            #set puzzles to false so that no more play.
            flags[0]='0'
            player.update_player(gv.curr_player,'flags',','.join(flags))
    adv.start()
    
@adv.when('jo')
def activate_Jo():
    gv.previous_context=adv.get_context()
    
    if gv.player_info['puzzles number']:
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
            adv.say(f'you are in {gv.curr_city["aliases"]},{gv.curr_city["description"]}')
        case 'name':
            adv.say('your name is Alice? I dont know')
        case 'whyhere':
            adv.say('why you ask why you here?')
        case 'bye':
            adv.say('%&^(#$&)!')
            adv.set_context(gv.previous_context)

@adv.when('right',direction='right')
@adv.when('r',direction='right')
@adv.when('left',direction='left')
@adv.when('l',direction='left')
@adv.when('up',direction='up')
@adv.when('u',direction='u')
@adv.when('down',direction='down')
@adv.when('d',direction='down')
def move(direction):
    x=int(gv.curr_cell.split(',')[0])
    y=int(gv.curr_cell.split(',')[1])
    match direction:
        case "right" | "r":  
            if x<10:  x+=1
        case "left" | "l": 
            if x>1: x-=1
        case "up" | "u": 
            if y<10: y+=1
        case "down" | "d": 
            if y>1: y-=1
    gv.curr_cell=str(x)+','+str(y)

    #check_NPC(curr_cell)
    #check_monsters(curr_cell)
    #check_events(curr_cell)
@adv.when("take ITEM")
def take(item):
    player.add_to_inventory(gv.curr_player, item,1)
    items.remove_item(gv.curr_zone,gv.curr_cell,item)

@adv.when("look")
def look():
    available_items= items.get_items(gv.curr_zone,gv.curr_cell)
    if len(available_items)>0: 
        adv.say(f"You find {','.join(available_items)}.")
    else:
        adv.say('Nothing around.')
    
    available_npc= NPC.get_NPCs(gv.curr_zone,gv.curr_cell)
    if len(available_npc)>0: 
        adv.say(f"{','.join(available_npc)} are here.")
    else:
        adv.say('No one is around.')

@adv.when('inventory')
@adv.when('i')
def inv():
    inv=player.get_inventory(gv.urr_player)
    if len(inv)>0:
        adv.say(f"you have {','.join(inv)}")
    else:
        adv.say('You have nothing.')

@adv.when('talk to NPC')
def talk(npc):
    if not NPC.has_active_request(npc):
        npc_infor=NPC.load_npc(npc)[0]
        adv.say(npc_infor['greetings'])
    else:
        import RB001
        # script_file=NPC.get_active_request_scripts(npc)
        # with open(script_file) as f:
        #     exec(f.read())

def check_monsters(cell):
    pass

def check_events(cell):
    pass

main()

