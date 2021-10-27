from dotenv import load_dotenv
import os
import nextcord
from nextcord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix=os.getenv("DISCORD_PREFIX"))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # await client.change_presence(activity=nextcord.Game("Bricker"))

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"loaded: {filename}")


client.run(os.getenv("DISCORD_TOKEN"))