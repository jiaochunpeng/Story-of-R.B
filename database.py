import sqlite3

GAME_DB="db\game.db"


db_conn =sqlite3.connect(GAME_DB)

def _execute(sql):
    cur=db_conn.cursor()
    cur.execute(sql)
    cur.commit()

    