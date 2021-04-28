import discord
from discord.ext import commands
from discord import client

print("The bot is starting up...") # Startup message
token = "PASTE YOUR TOKEN HERE" # Paste your Token Bot here
client = commands.Bot(command_prefix=("!")) # Bot prefix

@client.event

async def on_ready():
    print(client.user,"ONLINE ","(ID ",client.user.id,")") # Print ONLINE when the bot is online
    

# Commands         
@client.event

async def on_message(message):
       if message.content == "Hi":
            await message.channel.send("Hi, I am a Discord Bot!")


client.run(token)
