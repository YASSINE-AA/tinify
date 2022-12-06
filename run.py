from main import application
import sqlite3
import config
# Author Yassine Ahmed Ali
conn = sqlite3.connect("urls.db")
cur = conn.cursor()
cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table'")
#? if the count is 1, then table exists
if not cur.fetchone()[0]==1 : {
    cur.execute("CREATE TABLE urltable (original,shortened)")
}
cur.close()
conn.close()

if __name__ == "__main__":
    application.run(host=config.HOST, debug=config.DEBUG)
