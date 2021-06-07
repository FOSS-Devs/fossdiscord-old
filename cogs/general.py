# Copyright (c) 2021 SKBotNL (and the members of the FOSS-Devs)
# See LICENSE in the project root for license information.

import discord
from discord.ext import commands
import psutil
import config
import bot
import datetime
import time
import json
import os
start_time = time.time()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Shows information about bot instance.')
    async def about(self, ctx):
        em = discord.Embed(title = "About this instance", color = discord.Color.green())
        em.add_field(name = "Project URL", value = "https://github.com/FOSS-Devs/freediscord/")
        em.add_field(name = "Support server", value = "https://discord.gg/myzbqnVUFN")
        servers = list(self.bot.guilds)
        serverNumber = len(servers)
        em.add_field(name = "Number of servers this instance is in", value = serverNumber)
        cpuUsage = psutil.cpu_percent()
        em.add_field(name = "CPU usage of host", value = cpuUsage)
        em.add_field(name = "Ping", value = "`"f"{round(self.bot.latency*1000)} ms`")
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        em.add_field(name="Uptime", value=text)
        await ctx.send(embed = em)

    # welcomer
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if os.path.isfile(f"settings/welcomer/{str(member.guild)}_welcomerenabled.json"):
            with open(f"settings/welcomer/{str(member.guild)}_welcomerenabled.json") as file:
                welcomersettings = json.load(file)
            if welcomersettings['enabled'] == 'true':
                await self.bot.get_channel(848464385710358549).send(f" Welcome!{member.mention}.")
            else:
                return
        else:
            return

def setup(bot):
    bot.add_cog(General(bot))
