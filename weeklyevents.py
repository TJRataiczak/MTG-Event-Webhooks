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

#Start webhook
webhook = DiscordWebhook(url=os.getenv("WEBHOOK_URL"), username=f"Apex Gaming Events")
embed = DiscordEmbed(title="Weekly Events", url = os.getenv("EVENT_LOCATOR_URL"), color = 242424)
count = 0
for day in week:
    #Add event for every day of the week to embed
    c.execute(f"SELECT * FROM events WHERE date='{day}'")
    events = c.fetchall()

    if events != []:
        for event in events:
            number_date = event[1].split("-")
            time_of_day = event[3].split(":")
            if "pm" in time_of_day[1] and "12" not in time_of_day[0]:
                string_date = int(datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]), int(time_of_day[0]) + 12, int(time_of_day[1][0:2])).timestamp())
            else:
                string_date = int(datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]), int(time_of_day[0]), int(time_of_day[1][0:2])).timestamp())
        
            if(len(event[2]) == 6 or len(event[2]) == 7):
                embed.add_embed_field(name=event[0], value=f"<t:{string_date}>\nCompanion Code: {event[2]}", inline = True)
            else:
                embed.add_embed_field(name=event[0], value=f"<t:{string_date}>", inline = True)
    else:
        count += 1
    
#If no events for the week post nothing
if count == 7:
    embed.add_embed_field(name=f"{today.strftime('%B %d')}-{week[-1].strftime('%B %d')}", value="No events for the week")

#Post embed to webhook
with open("images/logo.png", "rb") as f:
    webhook.add_file(file=f.read(), filename="logo.png")

embed.set_thumbnail(url="attachment://logo.png")
webhook.add_embed(embed)
webhook.execute()
print(f"Posted events to: Apex Gaming")

conn.close()