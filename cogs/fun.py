# Copyright (c) 2021 SKBotNL (and the members of the FOSS-Devs)
# See LICENSE in the project root for license information.

import discord
from discord import embeds
from discord.ext import commands
import psutil
import config
import bot
import random
from flickrapi import FlickrAPI

FLICKR_PUBLIC = 'd3e304b312d84e902c5bdf82311f79d7'
FLICKR_SECRET = '345887508fbfc557'

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.cooldown(1, 15, commands.BucketType.channel)
    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        if "@everyone" in choices:
            em = discord.Embed(title = "Nice try, sadly that won't work here.", color = discord.Color.red())
            await ctx.send(embed = em)
        else:
            if "@here" in choices:
                em = discord.Embed(title = "Nice try, sadly that won't work here.", color = discord.Color.red())
                await ctx.send(embed = em)
            else:
                em = discord.Embed(title = random.choice(choices), color = discord.Color.orange())
                await ctx.send(embed = em)
    
    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(description='#emotes')
    async def emote(self, ctx, emote : discord.Emoji = None):
        """emote command"""
        if emote == None:
            em = discord.Embed(title="No emote given", description = f"Please use `{config.prefix}emote <emote>`.", color = discord.Color.red())
            await ctx.send(embed=em)
            return
        else:
            try:
                em = discord.Embed(timestamp=emote.created_at, color = discord.Color.green())
                em.set_author(name=emote.name, icon_url=emote.url)
                em.set_thumbnail(url=emote.url)
                em.set_footer(text="Created on")
                em.add_field(name="ID", value=emote.id)
                em.add_field(name="Usage", value=f"`{emote}`")
                em.add_field(name="URL", value=f"<{emote.url}>")
                await ctx.send(embed=em)
                return
            except Exception:
                em = discord.Embed(title="That emote probably is not in the server that the bot is in.")
                await ctx.send(embed=em)
                return
        '''
        else:
            try:
                emote = discord.utils(self.bot.get_all_emojis())
                emote = discord.utils.get(self.bot.Emoji, name=emote)
            except Exception as e:
                await ctx.send(str(e))
                return
        '''
    @commands.cooldown(1, 15, commands.BucketType.channel)
    @commands.command()
    async def f(self, ctx, *, message2):
        em = discord.Embed(title = f"F in the chat to: **{message2}**", color=discord.Color.green())
        msg = await ctx.send(embed = em)
        await msg.add_reaction('🇫')

    @commands.cooldown(1, 15, commands.BucketType.user)
    @commands.command(aliases=['aww','kat','cats'])
    async def cat(self, ctx):
        flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
        response = flickr.photos.search(text='kitten', per_page=10, extras = 'url_c', safe_search=1, privacy_filter = 1)
        index = random.randint(0,9)
        url = response['photos']['photo'][index]['url_c']
        em = discord.Embed(title = "Cat Picture:", color = discord.Color.blue())
        em.set_image(url=url)
        await ctx.send(embed=em)
        

        
def setup(bot):
    bot.add_cog(Fun(bot))
