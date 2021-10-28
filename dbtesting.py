import sqlite3

conn = sqlite3.connect('discordbot.db')
c = conn.cursor()

# c.execute("INSERT INTO servers (serverID, storeID) VALUES ('574389293318012928', '12723')")

c.execute("SELECT * FROM events")

for event in c.fetchall():
    print(event)


conn.commit()

conn.close()