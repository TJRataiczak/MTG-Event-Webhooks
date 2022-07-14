from os import name
from discord_webhook import DiscordWebhook, DiscordEmbed
import sqlite3
import datetime

today = datetime.date.today()

#Open connection to database and grab all stores to iterate through
conn = sqlite3.connect("apexgamingesports.db")
c = conn.cursor()

#Start webhook
webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/988274101112160288/OhZLBf1L5DSQU-vPDa7_vpWr-kVlrbTPaZODOKazoR6TIWBOxsiYXq5q7lSsXTiSAsQJ", username=f"Apex Gaming Events")
embed = DiscordEmbed(title="Today's Events")
c.execute(f"SELECT * FROM events WHERE date = '{today}'")
events = c.fetchall()
#Add event(s) for the day posts none if no events
if events != []:
    for event in events:
        number_date = event[1].split("-")
        string_date = datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]))
        if(len(event[2]) == 6 or len(event[2]) == 7):
            embed.add_embed_field(name=string_date.strftime("%B %d"), value=f"{event[0]}\n{event[3]}\nCompanion Code: {event[2]}", inline = False)
        else:
            embed.add_embed_field(name=string_date.strftime("%B %d"), value=f"{event[0]}\n{event[3]}", inline = False)            
else:
    embed.add_embed_field(name=f"{today.strftime('%B %d')}", value="No events for today")
    
#Post embed to webhook
webhook.add_embed(embed)
webhook.execute()

conn.close()