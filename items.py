import database as db

def get_items(zone,cell):
    result=db.execute_query(f"select item_name from items where zone={zone} and cell='{cell}'")
    return [x[0] for x in result ]
    
def add_item(zone,cell,item):
    result=db.execute_query(f"insert into items(zone,cell,item_name) values({zone},'{cell}','{item}')")
    return result

def remove_item(zone,cell,item):
    result=db.execute(f"delete from items where zone={zone} and cell='{cell}' and item_name='{item}'")