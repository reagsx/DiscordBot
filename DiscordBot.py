import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Modify Bot Description, Prefix, and if it will direct message help.
client = Bot(description="Grouping Bot Alpha Development, by Mystykall.", command_prefix="?", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	print('You are running Grouping Bot')
	print('Created by Mystykall')
	return await client.change_presence(game=discord.Game(name='Someone set us up the groups.'))

@client.command(pass_context = True)
async def groups(ctx, voice_channel_id):
    #First getting the voice channel object
    voice_channel = discord.utils.get(ctx.message.server.channels, id = voice_channel_id)
    if not voice_channel:
        return await client.say("That is not a valid voice channel.")


    group_dict = {'Flex 1': [],
                  'Flex 2': [],
                  'Defense': [],}
    tank_list = []
    pa_list = []
    fill_list = []


    members = voice_channel.voice_members
    for m_role_check in members:
        members_roles = m_role_check.roles

        #debugging purposes
        role_read = [x.name for x in members_roles]
        print(role_read)

        #make lists of players for roles
        if "defense" in [x.name.lower() for x in members_roles]:
            print('Defensive Player Found')
            group_dict['Defense'].append(m_role_check.display_name)
        elif "flex 1" in [x.name.lower() for x in members_roles]:
            print('Flex Player Found')
            group_dict['Flex 1'].append(m_role_check.display_name)
        elif "flex 2" in [x.name.lower() for x in members_roles]:
            print('Flex Player Found')
            group_dict['Flex 2'].append(m_role_check.display_name)
        elif "pa" in [x.name.lower() for x in members_roles]:
            print("PA player found")
            pa_list.append(m_role_check.display_name)
        elif "tank" in [x.name.lower() for x in members_roles]:
            print("Tank player found")
            tank_list.append(m_role_check.display_name)
        else:
            print("no one important found, sorting...")
            fill_list.append(m_role_check.display_name)

        total_players = len(tank_list) + len(pa_list) + len(fill_list)

        number_of_groups = (total_players//5) + 1

    print("Total Groups: " + str(number_of_groups))

    for group_number in range(number_of_groups):
        group_dict['Group ' + str(group_number+1)] = []
        try:
            group_dict['Group ' + str(group_number+1)].append(pa_list.pop())
        except Exception as e:
            print('No PA')
        try:
            group_dict['Group ' + str(group_number+1)].append(tank_list.pop())
        except Exception as e:
            print('No Tank')
        for x in range(3):
            try:
                group_dict['Group ' + str(group_number+1)].append(fill_list.pop())
            except Exception as e:
                print('No Fill')





    member_names = '\n'.join([x.name for x in members])

    #Debug the groups in terminal
    print(group_dict)
    print(fill_list)
    print(tank_list)
    print(pa_list)

    group = "\n\n".join("**{}:** {}".format(key,', '.join(value)) for (key,value) in group_dict.items())\
    + '\n\n\n__**Not Assigned:**__' + '\n**Fills:** ' + ' '.join(fill_list) + '\n\n**PAs: **' + ' '.join(pa_list)\
    + '\n\n**Tanks:** ' + ' '.join(tank_list)

    embed = discord.Embed(title = "Group setup for all members in {}".format(voice_channel.name),
                          description = group,
                          color=discord.Color.blue())

    return await client.say(embed = embed)


@client.command()
async def cippy(*args):

	await client.say("Cippy is a complete and utter jackass.")


client.run('Enter Discord Token Here')
