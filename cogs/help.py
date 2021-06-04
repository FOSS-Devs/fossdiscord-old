# Copyright (c) 2021 SKBotNL (and the members of the FOSS-Devs)
# See LICENSE in the project root for license information.

import discord
from discord.ext import commands
import config
import globalconfig
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed(title = "Help", description = "Use `" + config.prefix + "help <command>` for extended information on a command.", color = discord.Color.orange())
            em.add_field(name = "General", value = "about")
            em.add_field(name = "Moderation", value = "ban, changenick, delwarn, kick, modnick, mute, purge, unban, unmute, warn, warns")
            em.add_field(name = "Settings", value = "botstatus, botstatusrepeat")
            em.add_field(name = "Utils", value = "avatar, joined, ping, quickpoll, uptime, userinfo")
            em.add_field(name = "Fun", value = "add, choose, f, emote")
            em.add_field(name = "Caesarcrypt", value = "twisted_msg, untwisted_msg")
            em.add_field(name = "VirusTotal", value = "scan_url, vt_hash")
            em.add_field(name = "Update", value = "updatecheck, updatebot, updatecogs")
            em.add_field(name = "Admin", value = "getchannels, getinvite, loadcog, lockdownbot, reloadcog, restartbot, servers, shutdownbot, unloadcog")
            em.add_field(name = "Help", value = "help - Shows this message")
            if config.latest_version > globalconfig.version:
                em.add_field(name = "Notice", value = "This bot has an available update that will update it from version `" + globalconfig.version + "` to version `" + config.latest_version + "`. Please use `" + config.prefix + "updatecheck` for more details.")
            elif config.latest_version < globalconfig.version:
                em.add_field(name = "Notice", value = "This bot has an available downgrade that will downgrade it from version `" + globalconfig.version + "` to version `" + config.latest_version + "`. Please use `" + config.prefix + "updatecheck` for more details.")
            await ctx.send(embed = em)

    # Moderation commands
    @help.command(name="ban")
    async def _ban(self, ctx):
        em = discord.Embed(title = "Moderation: Ban", description = config.prefix + "ban <user> optional:<reason> \n\nBan a member.", color = discord.Color.orange())
        await ctx.send(embed = em)
    
    @help.command(name="changenick")
    async def _changenick(self, ctx):
        em = discord.Embed(title = "Moderation: ChangeNick", description = config.prefix + "changenick <user ID or mention> <new nickname> \n\nChanges the nickname of a user or a bot.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="delwarn")
    async def _delwarn(self, ctx):
        em = discord.Embed(title = "Moderation: Delwarn", description = config.prefix + "delwarn <user> <reason of warn you want to delete> \n\nDelete a warning.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="kick")
    async def _kick(self, ctx):
        em = discord.Embed(title = "Moderation: Kick", description = config.prefix + "kick <user> optional:<reason> \n\nKick a member.", color = discord.Color.orange())
        await ctx.send(embed = em)
    
    @help.command(name="modnick")
    async def _modnick(self, ctx):
        em = discord.Embed(title = "Moderation: ModNick", description = config.prefix + "modnick <user ID or mention>\n\nModerates the nickname of a user or a bot (sets the nickname to 'ModdedNick' plus a random string of letters or numbers).", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="mute")
    async def _mute(self, ctx):
        em = discord.Embed(title = "Moderation: Mute", description = config.prefix + "mtue <user> <mutetime> \n\nMute a member.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="purge")
    async def _purge(self, ctx):
        em = discord.Embed(title = "Moderation: Purge", description = config.prefix + "purge <number of messages to purge> \n\nPurge messages, default amount is 10.\n\nOther usages:\n" + config.prefix + "purge <user> <how many messages to look back for message sent by user>", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="unban")
    async def _unban(self, ctx):
        em = discord.Embed(title = "Moderation: Unban", description = config.prefix + "unban <userid> \n\nUnban a member.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="unmute")
    async def _unmute(self, ctx):
        em = discord.Embed(title = "Moderation: Unmute", description = config.prefix + "unmute <user> \n\nUnmute a member.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="warn")
    async def _warn(self, ctx):
        em = discord.Embed(title = "Moderation: Warn", description = config.prefix + "warn <user> <reason> \n\nWarn a member.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="warns")
    async def _warns(self, ctx):
        em = discord.Embed(title = "Moderation: Warns", description = config.prefix + "warns <user> \n\nSee the warnings for a member.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # General commands
    @help.command(name="about")
    async def _about(self, ctx):
        em = discord.Embed(title = "General: About", description = config.prefix + "about \n\nShows information about this bot instance.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # Fun commands
    @help.command(name="add")
    async def _add(self, ctx):
        em = discord.Embed(title = "Fun: Add", description = config.prefix + "add <number1> <number2> \n\nAdds two numbers together.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="choose")
    async def _choose(self, ctx):
        em = discord.Embed(title = "Fun: Choose", description = config.prefix + "choose "<choice1>" "<choice2>" \n\nChooses between multiple choices.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="f")
    async def _f(self, ctx):
        em = discord.Embed(title = "Fun: F", description = config.prefix + "f <message> \n\nSays F in the chat and adds an F emoji to the message.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="emote")
    async def _emote(self, ctx):
        em = discord.Embed(title = "Fun: emote", description = config.prefix + "emote \n\nEmote command.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # Settings commands
    @help.command(name="botstatus")
    async def _botstatus(self, ctx):
        em = discord.Embed(title = "Settings: BotStatus", description = config.prefix + "botstatus <status> \n\nSets the status of the bot. Owner only. '" + config.prefix + "botstatus' to reset", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="botstatusrepeat")
    async def _botstatusrepeat(self, ctx):
        em = discord.Embed(title = "Settings: BotStatusRepeat", description = config.prefix + "botstatusrepeat \n\nRepeatedly sets the status of the bot. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # Utils commands
    @help.command(name="avatar")
    async def _avatar(self, ctx):
        em = discord.Embed(title = "Utils: Avatar", description = config.prefix + "avatar <user> \n\nGet a link to somebody's avatar.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="joined")
    async def _joined(self, ctx):
        em = discord.Embed(title = "Utils: Joined", description = config.prefix + "joined <user> \n\nTells you when a user joined the server.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="ping")
    async def _ping(self, ctx):
        em = discord.Embed(title = "Utils: Ping", description = config.prefix + "ping \n\nTells you the latency between the bot and the server.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="quickpoll")
    async def _quickpoll(self, ctx):
        em = discord.Embed(title = "Utils: Quickpoll", description = config.prefix + "quickpoll <poll> \n\nMake a poll with yes/no reactions.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="uptime")
    async def _uptime(self, ctx):
        em = discord.Embed(title = "Utils: Uptime", description = config.prefix + "uptime \n\nShows the uptime of the bot.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="userinfo")
    async def _userinfo(self, ctx):
        em = discord.Embed(title = "Utils: Userinfo", description = config.prefix + "userinfo <user> \n\nGives you information about a user.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # Caesar commands
    @help.command(name="twisted_msg")
    async def _encrypt(self, ctx):
        em = discord.Embed(title = "Caesarcrypt: Twisted Your Message", description = config.prefix + "twisted_msg <rounds> <message> \n\nTwisted a message.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="untwisted_msg")
    async def _decrypt(self, ctx):
        em = discord.Embed(title = "Caesarcrypt: Untwisted Your Message", description = config.prefix + "untwisted_msg <rounds> <message> \n\nUntwisted a message.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # Update commands
    @help.command(name="updatebot")
    async def _updatebot(self, ctx):
        em = discord.Embed(title = "Update: UpdateBot", description = config.prefix + "updatebot \n\nUpdates/downgrades the bot, replacing all of the bot files, except for the warns folder and the config.py file, with the newest files directly from the GitHub repository. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="updatecheck")
    async def _updatecheck(self, ctx):
        em = discord.Embed(title = "Update: UpdateCheck", description = config.prefix + "updatecheck \n\nChecks for updates/downgrades for the bot. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="updatecogs")
    async def _updatecogs(self, ctx):
        em = discord.Embed(title = "Update: UpdateCogs", description = config.prefix + "updatecogs \n\nUpdates the bot's cogs, replacing all of the cog files with the newest files directly from the GitHub repository. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # VirusTotal commands
    @help.command(name="scan_url")
    async def _scan_url(self, ctx):
        em = discord.Embed(title = "VirusTotal: Scan_URL", description = config.prefix + "scan_url <link> with https or http at the begining \n\nScans a URL link using a VirusTotal API key.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="vt_hash")
    async def _vt_hash(self, ctx):
        em = discord.Embed(title = "VirusTotal: VT_Hash", description = config.prefix + "vt_hash <file hash> SHA-256 SHA-1 or MD5 \n\nScans a file hash using a VirusTotal API key.", color = discord.Color.orange())
        await ctx.send(embed = em)

    # Owner commands
    @help.command(name="loadcog")
    async def _reloadcog(self, ctx):
        em = discord.Embed(title = "Owner: LoadCog", description = config.prefix + "loadcog <cog> \n\nLoads the user specified cog. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="lockdownbot")
    async def _lockdownbot(self, ctx):
        em = discord.Embed(title = "Owner: LockdownBot", description = config.prefix + "lockdownbot \n\nLocks down the bot in all servers and disables most commands. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="reloadcog")
    async def _reloadcog(self, ctx):
        em = discord.Embed(title = "Owner: ReloadCog", description = config.prefix + "reloadcog <cog> \n\nReloads the user specified cog. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="restartbot")
    async def _restartbot(self, ctx):
        em = discord.Embed(title = "Owner: RestartBot", description = config.prefix + "restartbot \n\nRestarts the bot. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="shutdownbot")
    async def _shutdownbot(self, ctx):
        em = discord.Embed(title = "Owner: ShutdownBot", description = config.prefix + "shutdownbot \n\nShuts down the bot. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="unloadcog")
    async def _reloadcog(self, ctx):
        em = discord.Embed(title = "Owner: UnloadCog", description = config.prefix + "unloadcog <cog> \n\nUnloads the user specified cog. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="servers")
    async def _servers(self, ctx):
        em = discord.Embed(title = "Owner: Servers", description = config.prefix + "servers \n\nProvides a list of servers the bot is in, along with server IDs. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="getchannels")
    async def _getchannels(self, ctx):
        em = discord.Embed(title = "Owner: GetChannels", description = config.prefix + "getchannels <serverid> \n\nGets the channels of the server provided. The bot must be in the server for this to work. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)

    @help.command(name="getinvite")
    async def _getinvite(self, ctx):
        em = discord.Embed(title = "Owner: GetInvite", description = config.prefix + "getinvite <serverid> <channel>\n\nGenerates an invite for the server provided. A channel name can optionally be provided and it defauts to `general`. Owner only.", color = discord.Color.orange())
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Help(bot))
