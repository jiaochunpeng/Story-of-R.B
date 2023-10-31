import sqlite3

GAME_DB="db\game.db"


def connect():
    db_conn =sqlite3.connect(GAME_DB, isolation_level=None)
    db_conn.row_factory = sqlite3.Row
    cur=db_conn.cursor()
    return db_conn,cur

def execute(sql):
    conn,cur=connect()
    cur.execute(sql)
    try:
        conn.commit()
        conn.close()
        return True
    except:
        return False
    
def execute_query(sql):
    conn,cur=connect()
    res = cur.execute(sql)
    result=res.fetchall()
    conn.close()
    return result
    