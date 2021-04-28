########################################################
#
# Discord bot script to ban users from the server
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

@commands.has_permission(administrator=True) # This command can only be run by an administrator (if you want to leave it free, delete this string)
async def ban(ctx, member : discord.Member,*,reason=None): # Ban a user whit !ban <user>
    await member.ban(reason = reason)


client.run(token)
