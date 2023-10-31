import adventurelib as adv
import quests
import player
import json


quest_infor=quests.load_request(quests.get_active_quests()[0])
quest_shortdesc=quest_infor['quest_shortdesc']
if quest_infor['flags']=='':quest_flags={}
try:
    quest_flags=json.loads(quest_infor['flags'])
except:
    raise(Exception('Flags in quest table should be json format.'))

#player_info=None
#city_info=None
if 'firstmet' not in list(quest_flags.keys()):
    adv.say("Finally you are here. I have been here for 500 years waiting for you! Before I explain what happened, bring me a knife so that I can cut the anorning rope on my leg.")
    quest_flags['firstmet']=0
    flags= json.dumps(quest_flags)
    quests.update_flags(quest_shortdesc,flags)

if 'bring knife' not in list(quest_flags.keys()) and 'knife' in player.get_inventory(CURR_PLAYER):
    adv.say("Aha! You bring a knife. Thank you. Could you cut the rope for me? Now let me tell you the whole story.")
    #adv.say('press space to continue.')
    #waitforspace()
    adv.say('Here are 5000 words.................................................................................')
    adv.say('Now bring me 12 head skull of dog, I will give a mysterias stuff in return.')
    quest_flags['bring knife']=0
    flags= json.dumps(quest_flags)
    quests.update_flags(quest_shortdesc,flags)


if  'bring skull' not in list(quest_flags.keys()) and 'head skull of dog' in player.get_inventory(CURR_PLAYER):
    adv.say("Aha! You take me the head skull of dog. Here you are. I don't know what it is but i must be very cool!")
    player.add_to_inventory(CURR_PLAYER,'time traveler')
    quest_flags['bring skull']=0
    flags= json.dumps(quest_flags)
    quests.update_flags(quest_shortdesc,flags)



