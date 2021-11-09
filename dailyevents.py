from os import name
from discord_webhook import DiscordWebhook, DiscordEmbed
import sqlite3
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

today = datetime.date.today()

#Open connection to database and grab all stores to iterate through
conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
c = conn.cursor()
c.execute("SELECT webhookid, storeid, storeimage FROM stores")

for store in c.fetchall():
    #Start webhook
    webhook = DiscordWebhook(url=store[0], username=f"{store[1]} Events", avatar_url=store[2])
    embed = DiscordEmbed(title="Today's Events")
    c.execute(f"SELECT eventdate, eventid, eventdescription FROM events WHERE eventdate='{today}'")
    events = c.fetchall()
    #Add event(s) for the day posts none if no events
    if events != []:
        for event in events:
            number_date = event[0].split("-")
            string_date = datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]))
            embed.add_embed_field(name=string_date.strftime("%B %d"), value=f"{event[1]}\n{event[2]}")
    else:
        embed.add_embed_field(name=f"{today.strftime('%B %d')}", value="No events for today")
    
    #Post embed to webhook
    webhook.add_embed(embed)
    webhook.execute()
    print(f"Posted events to: {store[1]}")

conn.close()