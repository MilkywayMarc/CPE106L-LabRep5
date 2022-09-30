import sqlite3 as sql

db = sql.connect("machineprob3.db")
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
print("\nFetching \"ADVENTURE_TRIP\" from database:\n\n")
cursor.execute("SELECT * FROM ADVENTURE_TRIP")
for row in cursor:
    print(row)
    print("\n")
