from pathlib import Path
import sqlite3
def initialize():
    root=Path(__file__).parent.parent.__str__()
    databasePath=Path("/data/GuitarTabs.db").__str__()
    sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS letterLinks (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            link TEXT 
        );""",
    """CREATE TABLE IF NOT EXISTS artistsLinks (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            link TEXT 
        );""",
    ]
    # create a database connection
    try:
        with sqlite3.connect(root+databasePath) as conn:
            # create a cursor
            cursor = conn.cursor()

            # execute statements
            for statement in sql_statements:
                cursor.execute(statement)

            # commit the changes
            conn.commit()

            print("Tables created successfully.")
    except sqlite3.OperationalError as e:
        print("Failed to create tables:", e)