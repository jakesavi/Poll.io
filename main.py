import discord
from babble import *
from secret import *

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

    if message.content.startswith("$roll "):
        if (len(message.content) <= 6):
            return message.channel.send("Invalid len of string")
        
        split = message.content[6:]
        count = 6
        for i in split:
            if i == 'd' or i == 'D':
                break
            else:
                count +=1
        numberOfDie = int(message.content[6:count])
        count +=1 
        split : str = message.content[count:]
        count = 0
        for i in split:
            if i == ' ':
                break
            else:
                count +=1
        numberOfSides: str = int(split[:count])
        listOfRolls = roll(numberOfDie, numberOfSides)
        await message.channel.send("You rolled: " + str(listOfRolls) + "\nThe sum being: " + str(sum(listOfRolls)))
#This should be the last thing executed as this launches the bot.
client.run(token())
