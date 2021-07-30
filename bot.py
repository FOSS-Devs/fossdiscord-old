# Copyright (c) 2021 FOSS-Devs
# See LICENSE in the project root for license information.

import discord
from discord.ext import commands
import config
import globalconfig
import socket
import os
import json
import re
#import time
from datetime import datetime
from noswear import noswear


class FOSSDiscord:
    global intents
    global bot
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(command_prefix=config.prefix, intents=intents)
    
    def __init__(self):
        host = "127.0.0.1"
        port = 18265
        _socket = socket.socket()
        try:
            _socket.bind((host,port))
        except Exception as e:
            print(e)
            print('Bind port failed, probably another bot instance is running\nTry killing all Python processes')
            return
        bot.remove_command('help')
        bot.load_extension("cogs.general")
        bot.load_extension("cogs.utils")
        bot.load_extension("cogs.moderation")
        bot.load_extension("cogs.settings")
        bot.load_extension("cogs.caesarcrypt")
        bot.load_extension("cogs.help")
        bot.load_extension("cogs.update")
        bot.load_extension("cogs.admin")
        bot.load_extension("cogs.vtscan")
        bot.load_extension("cogs.fun")
        bot.run(config.bot_token)

    @bot.event
    async def on_ready():
        # What gets printed in the terminal when the bot is succesfully logged in
        print('\n')
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print(f"It's a good idea to use {config.prefix}shutdownbot to shut down the bot to prevent multiple instances")
        print('------')
        # Changes bot status to the default status when the bot starts up
        await bot.change_presence(activity=discord.Game(name=f'v{globalconfig.currentversion} | {config.prefix}help'))
        botowner = bot.get_user(int(config.ownerID))
        em = discord.Embed(title = "The bot is back online", color = discord.Color.green())
        try:
            await botowner.send(embed = em)
        except Exception:
            print("The bot is back online")

    @bot.event
    async def on_message(message):
        if not os.path.exists('settings'):
            os.makedirs('settings')
        if message.channel.type is discord.ChannelType.private or message.author == bot.user:
            pass
        else:
            try:
                with open(f"settings/enablement-{message.guild.id}.json") as file:
                    data = json.load(file)
                command_enable = data["settings"]["commands"]
                filter_enable = data["settings"]["filter"]
            except Exception:
                default = {"settings": {"filter": 0, "commands": 1}}
                with open(f"settings/enablement-{message.guild.id}.json", 'w') as file:
                    data = json.dump(default, file, indent=4)
                filter_enable = 1
                command_enable = 1
            if filter_enable == 1:
                #Check for profanity.
                if noswear(message.content).getresult == True:
                    await message.delete()
                    em = discord.Embed(title = "Please don't swear", color = discord.Color.orange())
                    await message.channel.send(embed=em, delete_after=10.0)
                    if not os.path.exists('settings'):
                        os.makedirs('settings')
                    if os.path.isfile(f"settings/logging-{message.guild.id}.json"):
                        with open(f"settings/logging-{message.guild.id}.json") as file:
                            logingjson = json.load(file)
                        logingchannel = logingjson["data"]["logging"]["channel"]
                        channel = bot.get_channel(int(logingchannel))
                        em = discord.Embed(title = f"{message.author} used swear word(s)", color = discord.Color.red())
                        em.set_author(name=message.author, icon_url=message.author.avatar_url)
                        em.add_field(name = "Message", value = message.content)

                        if os.path.isfile(f"settings/dateformat-{message.guild.id}.json"):
                            with open(f"settings/dateformat-{message.guild.id}.json") as file:
                                dateformatjson = json.load(file)
                            date_format = dateformatjson["data"]["dateformat"]["format"]
                        else:
                            date_format = config.date_format

                        datetimenow = datetime.now()
                        currentdate = datetime.strftime(datetimenow, date_format)
                        em.set_footer(text = f"{currentdate}")
                        await channel.send(embed=em)
                        return
                    else:
                        return
                else:
                    pass
            else:
                pass

            if os.path.isfile(f"settings/blacklist.json"):
                with open(f"settings/blacklist.json") as file:
                    blacklistjson = json.load(file)
                blacklist = blacklistjson["data"]
                if blacklist == {}:
                    pass
                else:
                    for attr, value in blacklist.items():
                        if re.search(str(message.author.id), blacklist[attr]["id"]):
                            if re.match(f'{config.prefix}', message.content):
                                BotOwner = await bot.fetch_user(config.ownerID)
                                em = discord.Embed(title = "You Are Blacklisted", description = f"You are blacklisted from using the bot. Please contact {BotOwner} for more information.", color = discord.Color.red())
                                await message.channel.send(embed = em, delete_after=10.0)
                                return
                            else:
                                pass
                        else:
                            pass
            else:
                pass
            if command_enable == 1:
                await bot.process_commands(message)
            else:
                if f"{config.prefix}settings" in message.content or f"{config.prefix}shutdownbot" in message.content:
                    await bot.process_commands(message)
                elif f"{config.prefix}restartbot" in message.content:
                    await bot.process_commands(message)
                else:
                    pass

    # error handling
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.delete()
            em = discord.Embed(title = "Error", description = "You do not have permission to do that", color = discord.Color.red())
            em.add_field(name = "Detailed Error", value = "`" + str(error) + "`")
            await ctx.send(embed = em, delete_after=10.0)
    #     elif isinstance(error, commands.MissingRequiredArgument):
    #         em = discord.Embed(title = "Error", description = "Your command is missing an argument", color = discord.Color.red())
    #         em.add_field(name = "Detailed Error", value = "`" + str(error) + "`")
    #         await ctx.send(embed = em, delete_after=10.0)
        elif isinstance(error, commands.CommandNotFound):
            await ctx.message.delete()
            em = discord.Embed(title = "Error", description = "Command not found", color = discord.Color.red())
            em.add_field(name = "Detailed Error", value = "`" + str(error) + "`")
            await ctx.send(embed = em, delete_after=10.0)
        elif isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow down!", description=f"Try again in `{round(error.retry_after*1)}s`", color = discord.Color.red())
            await ctx.send(embed=em, delete_after=10.0)
        elif isinstance(error, commands.MaxConcurrencyReached):
            await ctx.message.delete()
            em = discord.Embed(title=f"Oops!", description="Someone in this guild is already using that command, please wait", color = discord.Color.red())
            await ctx.send(embed=em, delete_after=10.0)
        else:
            em = discord.Embed(title = "An internal error occurred", color = discord.Color.red())
            em.add_field(name = "Detailed Error", value = "`" + str(error) + "`")
            await ctx.send(embed = em)

if __name__ == "__main__":
    FOSSDiscord()