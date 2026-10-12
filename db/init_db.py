import sqlite3
db = sqlite3.connect("db/incidents.db")
db.execute("""CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    severity TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'OPEN')""")
db.execute("INSERT INTO incidents (title, severity) VALUES (?, ?)",
           ("Trade feed delayed", "HIGH"))
db.commit()
for row in db.execute("SELECT * FROM incidents"):
    print(row)
