import discord
from discord.ext import commands
from secret import *
from babble import *
import random

description = ''' A small bot project'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='$', description=description, intents= intents)

@bot.command()
async def roll(ctx, *dice:str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send("Format must be in #d#")
        return
    results =', '.join(str(random.randint(1,limit)) for r in range(rolls))
    listres: list[str] = (results.split(", "))
    sum = 0 
    for i in listres:
        sum += int(i)
    await ctx.send("Rolled: "+results + " with a sum of: " + str(sum))

@bot.command()
async def babble(ctx):
    listOfBabble = babbleExt()
    await ctx.send("You cast babble! Your word is " + listOfBabble[0] + " with definition: " + listOfBabble[2])

bot.run(token())