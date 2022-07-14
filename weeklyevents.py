from discord_webhook import DiscordWebhook, DiscordEmbed
import sqlite3
import datetime

#Set today's date and setup week
today = datetime.date.today()
week = [today + datetime.timedelta(days=i) for i in range(7)]

#Open connection to database and grab all stores to iterate through
conn = sqlite3.connect("apexgamingesports.db")
c = conn.cursor()

#Start webhook
webhook = DiscordWebhook(url="https://discordapp.com/api/webhooks/988274101112160288/OhZLBf1L5DSQU-vPDa7_vpWr-kVlrbTPaZODOKazoR6TIWBOxsiYXq5q7lSsXTiSAsQJ", username=f"Apex Gaming Events")
embed = DiscordEmbed(title="Weekly Events")
count = 0
for day in week:
    #Add event for every day of the week to embed
    print(day)
    c.execute(f"SELECT * FROM events WHERE date={day}")
    print(c.fetchall())

    # if events != []:
    #     for event in events:
    #         number_date = event[0].split("-")
    #         string_date = datetime.datetime(int(number_date[0]), int(number_date[1]), int(number_date[2]))
    #         embed.add_embed_field(name=string_date.strftime("%B %d"), value=f"{event[1]}\n{event[2]}")   
    # else:
    #     count += 1
    
#If no events for the week post nothing
if count == 7:
    embed.add_embed_field(name=f"{today.strftime('%B %d')}-{week[-1].strftime('%B %d')}", value="No events for the week")

#Post embed to webhook
webhook.add_embed(embed)
webhook.execute()
print(f"Posted events to: Apex Gaming")

conn.close()