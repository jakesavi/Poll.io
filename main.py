import json
import discord
from babble import babble, coinflip
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
    if message.author == client.user:
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


    # Create a poll!
    if message.content.startswith("$createPoll"):
        if not message.channel.permissions_for(message.author).kick_members: 
            
            await message.channel.send("You are not a certified user")
        else:
            await message.channel.send("Ok! What would you like the name of the poll to be?")
            
            # check function that is optional with wait_for() see wait_for() in pycord documentation
            DiscussedChannel = message.channel
            # Ensures that the message matches the user (PLEASE TAKE NOTE OF SCOPE OF THIS FUNCTION)


            def match_certified_user(m):
                return m.author == message.author

            pollTitle = await client.wait_for('message',check=match_certified_user, timeout = 180.0)
            await DiscussedChannel.send("Alright, creating poll: " + pollTitle.content)
            await message.channel.send("Ok now tell me the options seperated by ',' If there are no comma's there will only be one option! ALSO DON'T PUT A SPACE BETWEEN OPTIONS PLEASE!")
            pollOptions = await client.wait_for('message',check=match_certified_user, timeout = 200.0)
            pollOptionsArray = pollOptions.content.split(',')
            await message.channel.send(pollEvents.makePoll(pollTitle, pollOptionsArray)["url"])
        

  #This should be the last thing executed as this launches the bot.  
client.run(token())
