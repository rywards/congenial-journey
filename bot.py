# bot.py
import os
import interactions

import discord
import random
import json
import string
import requests
import re
import datetime

from dotenv import load_dotenv
# Developer Server GUILD ID 475422952121171970
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

# These two lines are required by a discord.py update
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

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
# maybe turn this into a function
@client.event
async def on_message(message):

    #if debugging needed, use the trusty print statements
    #    print(client.user)
    #    print(message.content)
    check = message.content
    result = re.search(".*narc.*", check, re.IGNORECASE)
    print(type(result))
    if type(result) == re.Match:
        await message.reply("You're a fucking narc")


@client.event
async def on_message_edit(before, after):

    if before.author == client.user:
        return

    f = open('insults.json')
    insults = json.load(f)
    response = random.choice(insults)
    insult = response['insult']

    await after.reply(f'{insult}', mention_author=True)
    curr_time = datetime.datetime.now()
    curr_time = curr_time.strftime("%m/%d/%Y %H:%M:%S")
    print(curr_time + ": " + "Successful response to edit.")

bot = interactions.Client(token=TOKEN)

@bot.event
async def on_message(message):

    #if debugging needed, use the trusty print statements
    #    print(client.user)
    #    print(message.content)
    check = message.content
    result = re.search(".*narc.*", check, re.IGNORECASE)
    print(type(result))
    if type(result) == re.Match:
        await message.reply("You're a fucking narc")

    await bot.precess_commands(message)

@bot.command(
    name="quote",
    description="Get me a quote fucker.",
    scope=789213817912557588,
)
async def quote(ctx: interactions.CommandContext):
    f = open('quotes.json')
    quotes = json.load(f)
    response = random.choice(quotes)
    quote = response['quote']
    author = response['author']

    await ctx.send(f'\"{quote}\"\n-{author}')
    curr_time = datetime.datetime.now()
    curr_time = curr_time.strftime("%m/%d/%Y %H:%M:%S")
    print(curr_time + ": " + "Quote successfully sent.")

bot.start()
client.run(TOKEN)
