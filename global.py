import re
import discord
import os
import traceback
from discord.ext import commands
import asyncio
import datetime
from numpy import False_
import youtube_dl
import random
import sqlite3
import json

with open ("bans.json", "r") as f:
	global users
	users = json.load(f)
print (f"Забаненные - {users}")

TOKEN = "OTg0NzkyNzk3NjQ5NDY1Mzk0.G-WR2y.-8-VZT8Bs6dWKn5FJlFEhW5K6W2GzmV5_ZXkTQ"
PREFIX = "wg."
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)
bot.remove_command('help')
global STARTED
STARTED = True
staff = [690895078247497799, 956171634094518323]

@bot.event
async def on_ready():
    print('global is on')
    await bot.change_presence(status=discord.Status.dnd)

global Gban
GLOBAL_CHAT = 'global-chat1'  # PEP8: Названия констант пишутся капсом
Gban = users
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if STARTED == False:
        return
    channel = discord.utils.get(message.guild.text_channels, name=GLOBAL_CHAT)
    if message.author.id == bot.user.id:
        return
    if message.author.bot: return
    if message.channel.id != channel.id:
        return
    await message.delete() 
    if message.author.id in Gban:
        return
    for guild in bot.guilds:
        if channel := discord.utils.get(guild.text_channels, name=GLOBAL_CHAT):

            try:
            	embed = discord.Embed(title=f"", description = '<:7371discordhypesquadbrilliance:1030520234051907674> <a:2353arrowrightglow:1029814234416169040>   **{0.content}**'.format(message), colour = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
            	embed.set_footer(text = "{0.guild}".format(message), icon_url = "{0.guild.icon_url}".format(message))
            	embed.set_author(name="{0.author} ({0.author.id})".format(message), icon_url="{0.author.avatar_url}".format(message))
            	await channel.send(embed = embed)
            except discord.Forbidden:
                print(f"Невозможно отправить сообщение на сервер {guild.name}: Недостаточно прав")
            except discord.HTTPException as e:
                print(f"Невозможно отправить сообщение на сервер {guild.name}: {e}")


@bot.command()
async def ban(ctx, member: discord.Member, *, reason="Просто так"):
	if ctx.author.id in staff:
		c = bot.get_channel(993273720040853577)
		embed = discord.Embed(title=f"Пользователь {member} был за банен в глобальном чате по причине [{reason}]", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await c.send(embed=embed)
		embed = discord.Embed(title=f"Успешно", description=f"[Подробнее в канале оповещений глобала](https://discord.com/channels/993144849219993680/993273720040853577)", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)
		with open ("bans.json", "r") as f:
			users1 = json.load(f)
		with open ("bans.json", "w") as f:
			users1.append(member.id)
			global Gban
			Gban = users1
			json.dump (users1, f)
	else:
		embed = discord.Embed(title=f"Ошибка!\nВы не являетесь персоналом глобального чата, чтоб использовать эту команду!", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)


@bot.command()
async def ping(ctx):
	embed = discord.Embed(title=f"Пинг Глобального чата: {round(bot.latency * 1000)}ms", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
	await ctx.reply(embed=embed)

@bot.command()
async def clear(ctx, amount=6):
	if ctx.author.id in staff:
		c = bot.get_channel(993273720040853577)
		GLOBAL_CHAT = 'global-chat'
		embed = discord.Embed(title=f"Отчистка глобального чата!\nСообщений отчищается [{amount}]", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await c.send(embed=embed)
		embed = discord.Embed(title=f"Успешно", description=f"[Подробнее в канале оповещений глобала](https://discord.com/channels/993144849219993680/993273720040853577)", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)

		for guild in bot.guilds:

			if channel := discord.utils.get(guild.text_channels, name=GLOBAL_CHAT):
				await channel.purge(limit=amount)

	else:
		embed = discord.Embed(title=f"Ошибка!\nВы не являетесь персоналом глобального чата, чтоб использовать эту команду!", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)

@bot.command()
async def unban(ctx, member: discord.Member):
	if ctx.author.id in staff:
		c = bot.get_channel(993273720040853577)
		embed = discord.Embed(title=f"Пользователь {member} был за разбанен в глобальном чате по причине", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		with open ("bans.json", "r") as f:
			users1 = json.load(f)
		with open ("bans.json", "w") as f:
			users1.remove(member.id)
			global Gban
			Gban = users1
			json.dump (users1, f)
		await c.send(embed=embed)
		embed = discord.Embed(title=f"Успешно", description=f"[Подробнее в канале оповещений глобала](https://discord.com/channels/993144849219993680/993273720040853577)", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)
	else:
		embed = discord.Embed(title=f"Ошибка!\nВы не являетесь персоналом глобального чата, чтоб использовать эту команду!", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)

@bot.command()
async def stop(ctx):
	if ctx.author.id in staff:
		global STARTED
		STARTED = False
		c = bot.get_channel(993273720040853577)
		embed = discord.Embed(title=f"Глобальный чат был остановлен пользователем \n'{ctx.author} | {ctx.author.id}'", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await c.send(embed=embed)
		embed = discord.Embed(title=f"Успешно", description=f"[Подробнее в канале оповещений глобала](https://discord.com/channels/993144849219993680/993273720040853577)", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)

@bot.command()
async def start(ctx):
	if ctx.author.id in staff:
		global STARTED
		STARTED = True
		c = bot.get_channel(993273720040853577)
		embed = discord.Embed(title=f"Глобальный чат был запущен пользователем \n'{ctx.author} | {ctx.author.id}'", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await c.send(embed=embed)
		embed = discord.Embed(title=f"Успешно", description=f"[Подробнее в канале оповещений глобала](https://discord.com/channels/993144849219993680/993273720040853577)", color=discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def msg(ctx, *, msg):
    for guild in bot.guilds:
        channel = bot.get_channel(bot.guild.text_channels, name=GLOBAL_CHAT)
        if channel := discord.utils.get(guild.text_channels, name=GLOBAL_CHAT):
            try:
                embed = discord.Embed(title=f"Owner message", description = f'<:7371discordhypesquadbrilliance:1030520234051907674> <a:2353arrowrightglow:1029814234416169040>   **{msg}**', colour = ctx.author.color, timestamp=datetime.datetime.utcnow())
                await ctx.send(embed = embed)
            except discord.Forbidden:
                print(f"Невозможно отправить сообщение на сервер {guild.name}: Недостаточно прав")
            except discord.HTTPException as e:
                print(f"Невозможно отправить сообщение на сервер {guild.name}: {e}")

bot.run(TOKEN)

