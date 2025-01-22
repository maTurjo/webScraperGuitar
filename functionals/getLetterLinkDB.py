import sqlite3
from pathlib import Path

def getLetterLinkDB(id:int)->str:
    root = Path(__file__).parent.parent.__str__()
    databasePath = Path("/data/GuitarTabs.db").__str__()
    connect = sqlite3.connect(root+databasePath)
    cursor = connect.cursor()
    cursor.execute('SELECT id, name, link FROM letterLinks WHERE id =?', (id,))
    row=cursor.fetchone()
    return row