import os
import interactions
from dotenv import load_dotenv
import json
import random
import datetime
import discord

# Developer Server GUILD ID 475422952121171970
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')
SCOPE = os.getenv('SCOPE')

intents = discord.Intents.default()
intents.message_content = True
bot = interactions.Client(token=TOKEN)

# TODO: merge searchword and getquote to one
# function; they're literally the same thing

# function to get a quote from quotes.json
# and returns a string
def getquote():

    f = open('quotes.json')
    quotes = json.load(f)
    response = random.choice(quotes)
    quote = response['quote']
    author = response['author']

    quoteinfo = [quote, author]
    return quoteinfo

# searches a random word in english.json
# and return a string
def searchword():

    f = open('english.json')
    words = json.load(f)
    keys = list(words)
    response = random.choice(keys)

    return response

def getinsult():
    f = open('insults.json')
    insults = json.load(f)
    response = random.choice(insults)
    insult = response['insult']

    return insul

# Checking that the bot has started and providing information
# about the session
@bot.event
async def on_ready():
    print("ready ran")
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(f'Guild connection established to:\n'
          f'{guild.name} (id: {guild.id})')

    print('-----Guild Information-----\n'
          f'Name: {guild.name}\n'
          f'Icon Hash: {guild.icon}\n'
          '---------------------------'
    )

# creating a button and styling it
button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Are you sure?",
    custom_id="confirm",
)

# testing slash commend functionality
# name -->
@bot.command(
    name="nametest",
    description="command description",
    scope=SCOPE,
)
async def hello(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

# callback that sends a response upon button click
# button gets edited but stays; need to fix that
@bot.component("confirm")
async def _click_me(ctx: interactions.ComponentContext):
    button.disabled=True
    insult=getinsult()
    await ctx.edit(components=button)
    await ctx.send(insult)


# test command with button functionalist
@bot.command(
    name="test",
    description="TESTING THIS SHIT",
    scope=SCOPE,
)
async def _button(ctx: interactions.CommandContext):
    await ctx.send(components=button)

# quote command to get a quote
@bot.command(
    name="quote",
    description="Get me a quote fucker.",
    scope=SCOPE,
)
# pulling a quote from the json file
async def quote(ctx: interactions.CommandContext):

    info = getquote()
    quote = info[0]
    author = info[1]
    await ctx.send(f'\"**{quote}**\"\n-{author}')
    curr_time = datetime.datetime.now()
    curr_time = curr_time.strftime("%m/%d/%Y %H:%M:%S")
    print(curr_time + ": " + "Quote successfully sent.")

# command to send a random word
@bot.command(
    name="word",
    description="Random word please!",
    scope=789213817912557588
)
async def word(ctx: interactions.CommandContext):
    findwd=searchword()
    await ctx.send(f'You word is: **{findwd}**')

@bot.event
async def on_message(message):
    print("FUCK")


bot.start()
