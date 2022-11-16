# bot.py
import os

import discord
import random
import json
import string

from dotenv import load_dotenv
# Developer Server GUILD ID 475422952121171970
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

# These two lines are required by a discord.py update
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

url_size = 11
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break


    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name} (id: {guild.id})')

    print('-----Guild Information-----\n'
          f'Name: {guild.name}\n'
          f'Icon Hash: {guild.icon}\n'
          '---------------------------'
    )

# listens for  a member to join the server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

# listens for a specific message to be sent in the server
@client.event
async def on_message(message):

    #if debugging needed, use the trusty print statements
    #    print(client.user)
    #    print(message.content)
    if message.author == client.user:
        return

    # TODO: migrate all of these message statements to a cleaner format
    # load a quote from quotes.json when someone calls this
    # deletes the message after printing quote
    if message.content == '/quote':
        try:
            f = open('quotes.json')
            quotes = json.load(f)
            response = random.choice(quotes)
            quote = response['quote']
            author = response['author']

            await message.channel.send(f'\"{quote}\"\n-{author}')
            await message.delete()
            print("Quote successfully sent.")
        except:
            await message.channel.send("I fucked up.... Sorry")

    if message.content == '/video':
        url = 'https://www.youtube.com/watch?v='
        code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))

        video = url+code
        await message.channel.send(video)
        await message.delete()
        print(video)


client.run(TOKEN)
