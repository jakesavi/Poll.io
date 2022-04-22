from email.headerregistry import MessageIDHeader
from anyio import sleep_forever
import discord

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

    if message.content.startswith('$create'):
        original_channel = message.channel
        dmchannel = await client.create_dm(message.author)
        await dmchannel.send("You wish to create a poll?")
        await dmchannel.send("Text me a name for the poll using $name /{Name of Poll/}")
        if message.content.startswith('$name'):
            pollName = message.content.replace("$name","")
            await original_channel.send(str(message.author)+ " has created a poll named: " + pollName)
            return
            
client.run(token())