import database as db

def get_players():
    result=db.execute_query('select player_name from players')
    return [x[0] for x in result ]
    
def load_player(player:str):
    result=db.execute_query(f"select * from players where player_name='{player}'")
    return result

def update_player(player :str,attribute : str,value):
    with open('players.json',"w") as f:
        players=json.load(f)
        players[player][attribute]=value
        json.dump(players,f)