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

#Start webhook
webhook = DiscordWebhook(url=os.getenv("WEBHOOK_URL"), username=f"Apex Gaming Events")
embed = DiscordEmbed(title="Today's Events", url = os.getenv("EVENT_LOCATOR_URL"), color = 242424)
c.execute(f"SELECT * FROM events WHERE date = '{today}'")
events = c.fetchall()
#Add event(s) for the day posts none if no events
if events != []:
    for event in events:
        number_date = event[1].split("-")
        time_of_day = event[3].split(":")
        if "pm" in time_of_day[1]:
            string_date = datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]), int(time_of_day[0]) + 12, int(time_of_day[1][0:2]))
        else:
            string_date = datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]), int(time_of_day[0]), int(time_of_day[1][0:2]))

        if(len(event[2]) == 6 or len(event[2]) == 7):
            embed.add_embed_field(name=event[0], value=f"<t:{int(string_date.timestamp())}>\nCompanion Code: {event[2]}", inline = False)
        else:
            embed.add_embed_field(name=event[0], value=f"<t:{int(string_date.timestamp())}>", inline = False)            
else:
    embed.add_embed_field(name=f"{today.strftime('%B %d')}", value="No events for today")
    
#Post embed to webhook
webhook.add_embed(embed)
webhook.execute()

conn.close()