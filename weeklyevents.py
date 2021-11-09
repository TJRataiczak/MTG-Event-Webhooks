from discord_webhook import DiscordWebhook, DiscordEmbed
import sqlite3
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

#Set today's date and setup week
today = datetime.date.today()
week = [today + datetime.timedelta(days=i) for i in range(7)]

#Open connection to database and grab all stores to iterate through
conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
c = conn.cursor()
c.execute("SELECT webhookid, storeid, storeimage FROM stores")

for store in c.fetchall():
    #Start webhook
    webhook = DiscordWebhook(url=store[0], username=f"{store[1]} Events", avatar_url=store[2])
    embed = DiscordEmbed(title="Weekly Events")
    count = 0
    for day in week:
        #Add event for every day of the week to embed
        c.execute(f"SELECT eventdate, eventid, eventdescription FROM events WHERE eventdate='{day}'")
        events = c.fetchall()

        if events != []:
            for event in events:
                number_date = event[0].split("-")
                string_date = datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]))
                embed.add_embed_field(name=string_date.strftime("%B %d"), value=f"{event[1]}\n{event[2]}")   
        else:
            count += 1
    
    #If no events for the week post nothing
    if count == 7:
        embed.add_embed_field(name=f"{today.strftime('%B %d')}-{week[-1].strftime('%B %d')}", value="No events for the week")

    #Post embed to webhook
    webhook.add_embed(embed)
    webhook.execute()
    print(f"Posted events to: {store[1]}")

conn.close()