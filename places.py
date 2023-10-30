import database as db

def get_places():
    result=db.execute_query('select name from places')
    return [x[0] for x in result ]
    
def load_place(place:str):
    result=db.execute_query(f"select * from places where name='{place}'")
    return result

