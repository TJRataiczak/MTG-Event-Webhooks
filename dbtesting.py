import sqlite3

conn = sqlite3.connect('discordbot.db')
c = conn.cursor()

c.execute("SELECT * FROM events")

for event in c.fetchall():
    print(event)


conn.commit()

conn.close()