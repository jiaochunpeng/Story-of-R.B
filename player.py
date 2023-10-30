import database as db

def get_players():
    result=db.execute_query('select player_name from players')
    return [x[0] for x in result ]
    
def load_player(player:str):
    result=db.execute_query(f"select * from players where player_name='{player}'")
    return result

def update_player(player :str,attribute : str,value):
    result=db.execute(f"update players set {attribute}='{value}' where player_name='{player}'")
    return result

def get_inventory(player:str):
    result=db.execute_query(f"select item_name from player_items where player_name='{player}'")
    return [x[0] for x in result ]


def add_to_inventory(player:str,item:str,count):
    if item not in get_inventory(player):
        result=db.execute(f"insert into player_items(player_name,item_name,counts) values('{player}','{item}',1)")
    else:
        result=db.execute(f'update player_items set counts=counts+{count}')