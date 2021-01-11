import discord
from discord.ext import commands

class Email(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @client.event()
    async def on_message(self, message):
        if message.content.startswith('$greet'):
            channel = message.chanel
            await channel.send('Hello')

def setup(client):
    client.add_cog(Email(client))