import discord
import os
import datetime
import asyncio
from discord.ext import commands
import aiohttp
import random
import youtube_dl




class fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(ctx):
		print("fun cog on")


	@commands.command()
	#@commands.cooldown(1, 5, commands.BucketType.guild)
	async def owl(self, ctx):
		embed = discord.Embed(title="", description="", color=ctx.author.color)
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/Owls/new.json') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				await ctx.send(embed=embed)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def catowl(self, ctx):
		embed = discord.Embed(title="", description="", color=ctx.author.color)
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/OwlsWithCatHeads/new.json') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				await ctx.send(embed=embed)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def meme(self, ctx):
		embed = discord.Embed(title="", description="", color=ctx.author.color)
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/memes/hot.json') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				await ctx.send(embed=embed)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def iq(self, ctx):

		if ctx.author.id == 690895078247497799:
			embed = discord.Embed(title="<:6245badgeserverbooster8:991372261951021176> Iq", description=f"{ctx.author}, ваш iq равен: 1000 - 7", color=ctx.author.color)
		elif ctx.author.id == 406695050349903884:
			embed = discord.Embed(title="<:6245badgeserverbooster8:991372261951021176> Iq", description=f"{ctx.author}, ваш iq равен: {random.randint(500, 1000)}", color=ctx.author.color)
		else:
			embed = discord.Embed(title="<:6245badgeserverbooster8:991372261951021176> Iq", description=f"{ctx.author}, ваш iq равен: {random.randint(30, 300)}", color=ctx.author.color)
		await ctx.send(embed=embed)	


def setup(bot):
	bot.add_cog(fun(bot))