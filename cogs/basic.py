import discord
from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Basic cog loaded.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pinged! {round(self.client.latency*1000)} ms.')

    @commands.command()
    async def clear(self, ctx, amount = 10):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Basic(client))