import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.all()

client = discord.Client(intents=intents,command_prefix = "!")

@client.event
async def on_ready():
    print('{} has connected to discord!'.format(client.user))
    
@client.event
async def on_message(message):
    content = message.content
    if content == 'Hello':
        await message.channel.send('Hello, {}'.format(message.author))

client.run(TOKEN)