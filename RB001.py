import adventurelib as adv
import quests
import player
import json
import global_vars as gv

class RB001(quests.Quest):
    quest_shortdesc=None
    quest_flags=None

    def update():
        quest_infor=quests.load_quest(quests.get_NPC_active_quest('r.b'))
        RB001.quest_shortdesc=quest_infor['quest_shortdesc']
        if quest_infor['flags']=='':
            RB001.quest_flags={'firstmet':1}
        else:
            RB001.quest_flags=json.loads(quest_infor['flags'])
        
    def run():
        if RB001.quest_flags['firstmet'] ==1:
            adv.say("Finally you are here. I have been here for 500 years waiting for you! Before I explain what happened, bring me a knife so that I can cut the anorning rope on my leg.")
            RB001.quest_flags['firstmet']=0
            RB001.quest_flags['bring knife']=1
            flags= json.dumps(RB001.quest_flags)
            quests.update_flags(RB001.quest_shortdesc,flags)
            return

        if 'bring knife' in  RB001.quest_flags.keys() and RB001.quest_flags['bring knife']==1:
            if 'knife' in player.get_inventory(gv.curr_player):
                adv.say("Aha! You bring a knife. Thank you. Could you cut the rope for me? Now let me tell you the whole story.")
                #adv.say('press space to continue.')
                #waitforspace()
                adv.say('Here are 5000 words.................................................................................')
                adv.say('Now bring me 12 head skull of dog, I will give a mysterias stuff in return.')
                RB001.quest_flags['bring knife']=0
                RB001.quest_flags['bring skull']=1
                flags= json.dumps(RB001.quest_flags)
                quests.update_flags(RB001.quest_shortdesc,flags)
                return
            else:
                adv.say("Did you find a knife?.")
            


        if 'bring knife' in  RB001.quest_flags.keys() and RB001.quest_flags['bring knife']==1:
            if 'head skull of dog' in player.get_inventory(gv.curr_player):
                adv.say("Aha! You take me the head skull of dog. Here you are. I don't know what it is but i must be very cool!")
                player.add_to_inventory(gv.curr_player,'time traveler')
                RB001.quest_flags['bring skull']=0
                flags= json.dumps(RB001.quest_flags)
                quests.update_flags(RB001.quest_shortdesc,flags)
            else:
                adv.say("Did you find the head skulls?")



RB001.update()
RB001.run()