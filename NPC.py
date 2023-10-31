import database as db

def get_NPCs(zone,cell):
    result=db.execute_query(f"select npc_name from NPC where zone={zone} and cell='{cell}'")
    return [x[0] for x in result ]

def load_npc(npc:str):
    result=db.execute_query(f"select * from NPC where lower(npc_name)='{npc}'")
    return result
    
def move_NPC(name,zone,cell,new_zone,new_cell):
    result=db.execute(f"update NPC set zone={new_zone},cell='{new_cell}' where lower(npc_name)='{name}'")
    return result

def remove_npc(name):
    result=db.execute(f"delete from NPC where lower(npc_name)='{name}'")
    return result

def has_active_request(npc:str):
    result=db.execute_query(f"select count(1) from quests where lower(npc_name)='{npc}' and status='active'")
    return len(result)

def get_active_request_scripts(npc:str):
    result=db.execute_query(f"select script_file from quests where lower(npc_name)='{npc}' and status='active' limit 1")
    if len(result)>0: 
        return result[0][0]
    else:
        return ''