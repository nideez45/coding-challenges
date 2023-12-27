import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random 
from db_helper import get_random_challenge
from db_helper import get_all_challenge
from db_helper import add_challenge
from urllib.parse import urlparse
from bs4 import BeautifulSoup

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.all()

client = commands.Bot(intents=intents,command_prefix = "!")

def is_url_valid(url):
    try:
        response = requests.head(url)
        status = response.status_code//100
        return status == 2 or status == 3
    except requests.ConnectionError:
        return False

def get_html_title(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find('title')
    if title_tag:
        return title_tag.text.strip()
    else:
        return "Title not found on the page."

    

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
    parsed_url = urlparse(challenge_url)
    hostname = parsed_url.hostname
    path = parsed_url.path 
    
    if hostname != 'codingchallenges.fyi' or not is_url_valid(challenge_url) or not path.startswith("/challenges/") :
        await ctx.send("Unable to add {} please check if its a valid Coding Challenge".format(challenge_url))
        return 
    title = get_html_title(challenge_url)
    challenge_name = title.split("|")[0][:-1]
    await ctx.send(add_challenge(challenge_name,challenge_url))
    
    
client.run(TOKEN)