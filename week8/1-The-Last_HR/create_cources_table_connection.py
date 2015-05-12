import sqlite3

conn2 = sqlite3.connect("../databases/cources.db")
with open("create_table_of_cources.sql", 'r') as f:
    conn2.executescript(f.read())
conn2.row_factory = sqlite3.Row

conn2.commit()
