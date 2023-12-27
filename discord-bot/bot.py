import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random 
from db_helper import get_random_challenge
from db_helper import get_all_challenge

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.all()

client = commands.Bot(intents=intents,command_prefix = "!")

@client.event
async def on_ready():
    print('{} has connected to discord!'.format(client.user))
    
@client.event
async def on_message(message):
    content = message.content
    if content == 'Hello':
        await message.channel.send('Hello, {}'.format(message.author))
    await client.process_commands(message) 

@client.command(name='quote', help='Gives a random quote!')
async def get_quote(ctx):
    quoteid = random.randint(1,100)
    response = requests.get("https://dummyjson.com/quote/{}".format(quoteid))
    quote = response.json()['quote']
    await ctx.send(quote)

@client.command(name='challenge', help='Gives a random challenge!')
async def get_challenge(ctx):
    await ctx.send(get_random_challenge())

@client.command(name='list', help='List all challenges!')
async def list_challenge(ctx):
    await ctx.send(get_all_challenge())

@client.command(name='add', help='Add a new challenge!')
async def add_new_challenge(ctx,challenge_url):
    print(challenge_url)
    ctx.send("Done")
    
    
client.run(TOKEN)