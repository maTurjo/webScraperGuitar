import sqlite3
from pathlib import Path

def getArtistLinkDB(id:int):
    root = Path(__file__).parent.parent.__str__()
    databasePath = Path("/data/GuitarTabs.db").__str__()
    connect = sqlite3.connect(root+databasePath)
    cursor = connect.cursor()
    cursor.execute('SELECT id, name, link FROM artistsLinks WHERE id =?', (id,))
    row=cursor.fetchone()
    newRowItem1=row[1].decode('utf-8') if isinstance(row[1], bytes) else row[1]
    newRowItem2=row[2].decode('utf-8') if isinstance(row[2], bytes) else row[2]
    blobDecodedRow=(row[0],newRowItem1,newRowItem2)
    return blobDecodedRow   
    