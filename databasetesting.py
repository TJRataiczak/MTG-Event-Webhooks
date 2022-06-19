import sqlite3

conn = sqlite3.connect("apexgamingesports.db")
c = conn.cursor()

# c.execute("CREATE TABLE events (name text, date text, description text, time text)")
c.execute("SELECT * FROM events")
print(c.fetchall())

conn.commit()
conn.close()