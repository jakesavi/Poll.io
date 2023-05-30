import discord
from babble import *
from secret import *
import pollEvents

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.event
async def on_message(message):
    if message.author == client.user: # Ignore self function
        return


    # Each of these sections are different "Functions" to pollio message commands.
    # I am unsure if there is a better way to do this
    
    # Random word search
    if message.content.startswith('$babble'):
        listOfBabble = babble()
        await message.channel.send("You cast babble!")
        await message.channel.send("Your randomly generated word is: "+ listOfBabble[0])
        await message.channel.send("Its definition is: " + listOfBabble[2])
        return
    # CoinFlipper
    if message.content.startswith('$flip'):
        await message.channel.send("You cast flip!")
        if(coinflip()):
            await message.channel.send("You landed Heads!")
            return
        else:
            await message.channel.send("You landed Tails!")
            return

# TODO FIX the parsing with $roll
    if message.content.startswith("$roll "):
        if(len(message.content)) > 5 and 'd' in message.content:
            rolls = roll(int(message.content[6]),int(message.content[8]))
            for j in rolls:
                await message.channel.send(j)
            await message.channel.send("Your total is: " + str(sum(rolls)))


        else:
            await message.channel.send("Incorrect Syntax")

#This should be the last thing executed as this launches the bot.
client.run(token())
