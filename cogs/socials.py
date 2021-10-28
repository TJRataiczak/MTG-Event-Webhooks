from nextcord import message
from nextcord.ext import commands
import sqlite3
from dotenv import load_dotenv
import os

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx):
       await ctx.send(socialbuilder(ctx))

    @commands.command()
    async def twitch(self, ctx):
        await ctx.send(socialbuilder(ctx))

    @commands.command()
    async def facebook(self, ctx):
        await ctx.send(socialbuilder(ctx))

    @commands.command()
    async def twitter(self, ctx):
        await ctx.send(socialbuilder(ctx))

    @commands.command()
    async def website(self, ctx):
        await ctx.send(socialbuilder(ctx))

def setup(bot):
    bot.add_cog(Socials(bot))
    load_dotenv()

def socialbuilder(ctx):
        conn = sqlite3.connect(os.getenv("DATABASE_PATH"))
        c = conn.cursor()

        match ctx.message.content:
            case "!youtube":
                c.execute(f"SELECT youtube FROM servers WHERE serverID = '{ctx.guild.id}'")
                results = c.fetchone()
                if results[0] != None:
                    return f"https://www.youtube.com/channel/{results[0]}"
                else:
                    return "This discord doesn't have a YouTube channel registered."
            case "!twitch":
                c.execute(f"SELECT twitch FROM servers WHERE serverID = '{ctx.guild.id}'")
                results = c.fetchone()
                if results[0] != None:
                    return f"https://www.twitch.tv/{results[0]}"
                else:
                    return "This discord doesn't have a Twitch channel registered."
            case "!facebook":
                c.execute(f"SELECT facebook FROM servers WHERE serverID = '{ctx.guild.id}'")
                results = c.fetchone()
                if results[0] != None:
                    return f"https://www.facebook.com/{results[0]}"
                else:
                    return "This discord doesn't have a Facebook page registered."
            case "!twitter":
                c.execute(f"SELECT twitter FROM servers WHERE serverID = '{ctx.guild.id}'")
                results = c.fetchone()
                if results[0] != None:
                    return f"https://twitter.com/{results[0]}"
                else:
                    return "This discord doesn't have a Twitter page registered."
            case "!website":
                c.execute(f"SELECT website FROM servers WHERE serverID = '{ctx.guild.id}'")
                results = c.fetchone()
                if results[0] != None:
                    return results[0]
                else:
                    return "This discord doesn't have a website registered."