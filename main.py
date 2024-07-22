import discord
from discord import app_commands
from discord.ext.commands import Bot
from discord.ext.commands import Context
from dotenv import load_dotenv
import os
import datetime

import sqlite3

from constants import *
from database import db
import phrases
import util

load_dotenv()

token = os.environ["BOT_TOKEN"]

if token == "CHANGE_THIS":
    print("Change the token in the environment file or you will be sent to a re-education camp.")
    exit(1)

intents = discord.Intents.all()
client = Bot(command_prefix='ccp!', intents=intents)

def format_social_credit_msg(string: str, num: int):
    return util.format_var(string, {
        "num": num,
        "absnum": abs(num),
    })


@client.command(aliases=["credits"])
async def credit(ctx: Context):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    user = db.get_user_by_discord_id(ctx.author.id)
    social_credit = user.social_credit
    if social_credit != 0:
        await ctx.reply(f"You currently have {social_credit} Social Credit{util.plural(social_credit)}.")
    elif social_credit == 0:
        await ctx.reply(f"{social_credit}! Your execution date is {tomorrow.year}-{tomorrow.month}-{tomorrow.day}.")
    else:
        await ctx.reply("erm")

@client.command()
async def sherlock(ctx: Context):
    today = datetime.date.today()
    await ctx.reply(f"Goodbye! {today.year}-{today.month}-{today.day}.")


@client.event
async def on_message(message: discord.Message):
    ctx = await client.get_context(message)
    
    if message.author.bot: # don't let bots talk to each other
        return
    
    user = db.get_user_by_discord_id(ctx.author.id)

    credit = phrases.get_msg_credit(message.content)
    user.social_credit += credit
    if credit > 0:
        await ctx.reply(format_social_credit_msg(ADD_CREDIT_MSG, credit))
    elif credit < 0:
        await ctx.reply(format_social_credit_msg(MINUS_CREDIT_MSG, credit))

    await client.process_commands(message) # process commands (without this, commands won't run)

@client.event
async def on_ready():
    print("Ready!")

client.run(token)