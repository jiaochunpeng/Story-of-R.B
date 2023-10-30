import sqlite3

GAME_DB="db\game.db"


db_conn =sqlite3.connect(GAME_DB)
db_conn.row_factory = sqlite3.Row

def execute(sql):
    cur=db_conn.cursor()
    cur.execute(sql)
    try:
        cur.commit()
        cur.close()
        return True
    except:
        return False
    

def execute_query(sql):
    cur=db_conn.cursor()
    res = cur.execute(sql)
    result=res.fetchall()
    cur.close()
    return result
    