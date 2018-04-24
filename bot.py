import discord
import asyncio
import platform
import sys

try:
    from discord.ext import commands
except Import Error:
    print('Discord.py is not installed.')
    sys.exit(1)

from settings import settings

# Modify Bot Description, Prefix, and if it will direct message help.
description = "Royal Bot by Mystykall."



@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('Created by Mystykall')
	return await client.change_presence(game=discord.Game(name='Someone set us up the groups.'))

#Load the Modules
from modules import grouping
from modules import attendance

client.run('Enter Discord Token Here')
