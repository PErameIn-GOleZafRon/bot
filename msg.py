import discord
import os
import traceback
from discord.ext import commands
import asyncio
import datetime
import youtube_dl
import random
import sqlite3




TOKEN = "OTg0NzkyNzk3NjQ5NDY1Mzk0.G-WR2y.-8-VZT8Bs6dWKn5FJlFEhW5K6W2GzmV5_ZXkTQ"
PREFIX = "w."
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('msg is on')
    await bot.change_presence(status=discord.Status.dnd)



@bot.event
async def on_message(message):
	if message.author.id == 867075286189342750:
		await message.delete()
	await bot.process_commands(message)


'''@bot.event
async def on_message(message):
	if message.author.id == bot.user.id:
		return
	if message.author.bot: return
	await bot.process_commands(message)
	c = bot.get_channel(1002521552044183552)
	e = discord.Embed(title=f"", description = '<:role:808826577785716756> ➤ **{0.content}**'.format(message), colour = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
	e.set_footer(text = "{0.guild} | {0.channel}".format(message), icon_url = "{0.guild.icon_url}".format(message))
	e.set_author(name="{0.author} ({0.author.id})".format(message), icon_url="{0.author.avatar_url}".format(message))
	await c.send(embed=e)

'''    


bot.run(TOKEN)

