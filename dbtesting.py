import sqlite3

conn = sqlite3.connect('mtg.db')
c = conn.cursor()

c.execute("SELECT * FROM events")

print(c.fetchall())
conn.commit()

conn.close()