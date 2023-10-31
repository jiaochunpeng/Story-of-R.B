import database as db

def get_active_quests():
    result=db.execute_query(f"select quest_shortdesc from quests where status='active'")
    return [x[0] for x in result ]

def get_NPC_active_quest(npc):
    result=db.execute_query(f"select quest_shortdesc from quests where lower(NPC_name)='{npc}' and status='active' order by sequence limit 1")
    if len(result)>0:
        return result[0][0]
    else:
        return ''

def activate_NPC_quest(npc,quest_shortdesc):
    result=db.execute(f"update quests set status='active' where lower(NPC_name)='{npc}' and quest_shortdesc='{quest_shortdesc}'")
    return result


def load_quest(quest_shortdesc):
    result=db.execute_query(f"select * from quests where quest_shortdesc='{quest_shortdesc}'")
    return result[0]
    
def add_quest(NPC_name,quest_shortdesc,description,script_file):
    result=db.execute(f"insert into quests(NPC_name,quest_shortdesc,description,script_file,status) values('{NPC_name}','{quest_shortdesc}','{description}','{script_file}','inactive')")
    return result

def remove_quest(quest_shortdesc):
    result=db.execute(f"delete from quests where quest_shortdesc='{quest_shortdesc}'")
    return result

def update_status(qeust_shortdesc,status):
    result=db.execute(f"update quests set status='{status}' where quest_shortdesc='{qeust_shortdesc}'")
    return result

def update_flags(qeust_shortdesc,flags:str):
    result=db.execute(f"update quests set flags='{flags}' where quest_shortdesc='{qeust_shortdesc}'")
    return result

class Quest:
    def update():
        pass
    def run():
        pass