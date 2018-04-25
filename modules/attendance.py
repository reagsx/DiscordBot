from discord.ext import commands
import discord
import asyncio

class attendance:
    def __init__(self, bot):
        self.bot = bot

    # Attendance Command
    @commands.command()
    async def attendance(self):
        def format_names(total_list):
            return '\n'.join(total_list)


        def get_channels():
            voice_channel_list = []
            for server in self.bot.servers:
                for channel in server.channels:
                    if channel.type == discord.ChannelType.voice:
                        if channel.name != 'AFK':
                            voice_channel_list.append(channel)
            return voice_channel_list

        def get_display_names(channel_list):
            list_of_people = []
            for channel in channel_list:
                members = channel.voice_members
                for person in members:
                    list_of_people.append(person.display_name)
            return sorted(list_of_people)

        all_members = get_display_names(get_channels())
        await self.bot.say(str(len(all_members)) + ' members currently on Server: \n' + format_names(all_members))

def setup(bot):
    bot.add_cog(attendance(bot))
