import sqlite3
from pathlib import Path


def getRowCount(tableName: str) -> int:
    root = Path(__file__).parent.parent.__str__()
    databasePath = Path("/data/GuitarTabs.db").__str__()
    connect = sqlite3.connect(root+databasePath)
    cursor = connect.cursor()
    query = f"SELECT COUNT(*) FROM {tableName}"
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]
    cursor.close()
    connect.close()
    return row_count