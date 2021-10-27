import sqlite3

conn = sqlite3.connect('discordbot.db')
c = conn.cursor()

# c.execute("""CREATE TABLE servers (
#             serverID integer,
#             storeID integer
# )""")


# c.execute("INSERT INTO servers VALUES ('863187370119659560', '12723')")

# c.execute("PRAGMA table_info(events)")

c.execute("SELECT * FROM events")

# c.execute("DELETE FROM events")

for event in c.fetchall():
    print(event)


conn.commit()

conn.close()