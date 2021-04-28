########################################################
#
# Discord bot script to delete fixed number of messages
# Script by AtomixDem -> https://github.com/AtomixDem
#
########################################################


import discord
from discord.ext import commands
from discord import client

print("The bot is starting up...") # Startup message
token = "PASTE YOUR TOKEN HERE" # Paste your Token Bot here
client = commands.Bot(command_prefix=("!")) # Bot prefix

@client.event

async def on_ready():
    print(client.user,"ONLINE ","(ID ",client.user.id,")") # Print ONLINE when the bot is online
    

# Commands         
@client.command()

@commands.has_permission(administrator=True) # This command can only be run by an administrator (if you want to leave it free, delete this string)
async def clear(ctx, amount=10): # Delete 10 messages above
    await ctx.channel.purge(limit=amount)


client.run(token)
