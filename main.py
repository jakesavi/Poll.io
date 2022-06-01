import discord
from babble import babble, coinflip
from secret import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    
    if message.content.startswith('$babble'):
        listOfBabble = babble()
        await message.channel.send("You cast babble!")
        await message.channel.send("Your randomly generated word is: "+ listOfBabble[0])
        await message.channel.send("Its definition is: " + listOfBabble[2])
        return
    if message.content.startswith('$flip'):
        await message.channel.send("You cast flip!")
        if(coinflip()):
            await message.channel.send("You landed Heads!")
            return
        else:
            await message.channel.send("You landed Tails!")
            return
client.run(token())
