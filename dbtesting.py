import sqlite3

conn = sqlite3.connect('discordbot.db')
c = conn.cursor()

# c.execute("""CREATE TABLE servers (
#             serverID integer,
#             storeID integer
# )""")


c.execute("UPDATE servers SET website = 'https://www.apexgaming.gg/' WHERE serverID = '863187370119659560' ")

# c.execute("""ALTER TABLE servers
#             ADD website text""")

c.execute("SELECT * FROM servers")

# c.execute("DELETE FROM events")

for event in c.fetchall():
    print(event)


conn.commit()

conn.close()