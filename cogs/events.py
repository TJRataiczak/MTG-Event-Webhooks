from nextcord.ext import commands
import sqlite3

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello")
    
    @commands.command()
    async def events(self, ctx):
        conn = sqlite3.connect("D:\Windows Files\Documents\MTG Event Bot\discordbot.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}'")

        results = c.fetchall()

        await ctx.send(buildeventreply(results))

        conn.close()
    
    @commands.command()
    async def pioneer(self, ctx):
        conn = sqlite3.connect("D:\Windows Files\Documents\MTG Event Bot\discordbot.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Pioneer'")

        results = c.fetchall()

        await ctx.send(buildeventreply(results))

        conn.close()

    @commands.command()
    async def modern(self, ctx):
        conn = sqlite3.connect("D:\Windows Files\Documents\MTG Event Bot\discordbot.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Modern'")

        results = c.fetchall()
        await ctx.send(buildeventreply(results))

        conn.close()

    @commands.command()
    async def standard(self, ctx):
        conn = sqlite3.connect("D:\Windows Files\Documents\MTG Event Bot\discordbot.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Standard'")

        results = c.fetchall()

        await ctx.send(buildeventreply(results))

        conn.close()

    @commands.command()
    async def legacy(self, ctx):
        conn = sqlite3.connect("D:\Windows Files\Documents\MTG Event Bot\discordbot.db")
        c = conn.cursor()
        c.execute(f"SELECT * FROM events WHERE serverID = '{ctx.guild.id}' AND eventformat = 'Legacy'")

        results = c.fetchall()
        #await ctx.send(buildeventreply(results))

        conn.close()


def setup(bot):
    bot.add_cog(Events(bot))

def buildeventreply(results):
        reply = ""

        print(results)
        # if results == None:
        #     for result in results:
        #         reply += f"{result[2]}: {result[1]}\n"
        #     return reply
        # else:
        #     return "There are no upcoming events for that format."