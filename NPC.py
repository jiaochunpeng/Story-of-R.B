import database as db

def get_NPCs(zone,cell):
    result=db.execute_query(f"select npc_name from NPC where zone={zone} and cell='{cell}'")
    return [x[0] for x in result ]
    
def move_NPC(name,zone,cell,new_zone,new_cell):
    result=db.execute(f"update NPC set zone={new_zone},cell={new_cell} where npc_name={name}")
    return result

def remove_npc(name):
    result=db.execute(f"delete from NPC where npc_name='{name}'")
    return result