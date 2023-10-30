import database as db

def get_active_quests():
    result=db.execute_query(f"select quest_shortdesc+'('+NPC_name+')' from quests")
    return [x[0] for x in result ]
    
def add_quest(NPC_name,quest_shortdesc,quest_description,quest_script):
    result=db.execute(f"insert into quests(NPC_name,quest_shortdesc,quest_description,quest_script,quest_status)
                             values('{NPC_name}','{quest_shortdesc}','{quest_description}','{quest_script}','inactive')")
    return result

def remove_quest(quest_shortdesc):
    result=db.execute(f"delete from quests where quest_shortdesc='{quest_shortdesc}'")
    return result

def update_status(qeust_shortdesc,status):
    result=db.execute(f"update quests set status='{status}' where qeust_shortdesc={qeust_shortdesc}")
    return result