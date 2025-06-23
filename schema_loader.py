import sqlite3

def get_schema_descriptions(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    schema = {}

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table = table_name[0]
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        schema[table] = [col[1] for col in columns]

    conn.close()
    return schema
