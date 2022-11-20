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

intents = discord.Intents.default()
intents.message_content = True
bot = interactions.Client(token=TOKEN)

@bot.event
async def on_ready():
    print("ready ran")
    for guild in bot.guilds:
        if guild.name == GUILD:
            break


    print(f'{interactions.Member} is connected to the following guild:\n'
          f'{guild.name} (id: {guild.id})')

    print('-----Guild Information-----\n'
          f'Name: {guild.name}\n'
          f'Icon Hash: {guild.icon}\n'
          '---------------------------'
    )


@bot.command(
    name="nametest",
    description="command description",
    scope=789213817912557588,
)
async def hello(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

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

@bot.event
async def on_message(message):
    print("FUCK")


bot.start()