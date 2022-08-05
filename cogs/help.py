import discord
import datetime
from discord.ext import commands
import bot as b
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption, ComponentsBot
import asyncio

TOKEN = "OTg0NzkyNzk3NjQ5NDY1Mzk0.G-WR2y.-8-VZT8Bs6dWKn5FJlFEhW5K6W2GzmV5_ZXkTQ"
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=b.PREFIX, intents=intents)
bot.remove_command('help')


class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(ctx):
		print("help cog on")
		DiscordComponents(bot)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help(self, ctx, Chapter = None):

		alls = discord.Embed(title=f"Помощь", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
		alls.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		alls.add_field(name=f":shield: Модерация", value=f"`{b.PREFIX}ping`, `{b.PREFIX}clear`, `{b.PREFIX}mute`, `{b.PREFIX}infinitymute`, `{b.PREFIX}unmute`, `{b.PREFIX}kick`, `{b.PREFIX}ban`, `{b.PREFIX}unban`", inline=False)
		alls.add_field(name=f":diamond_shape_with_a_dot_inside: Фан", value=f"`{b.PREFIX}owl`, `{b.PREFIX}catowl`, `{b.PREFIX}meme`", inline=False)
		alls.add_field(name=f":infinity: Ролеплей", value=f"`{b.PREFIX}kiss`, `{b.PREFIX}kill`, `{b.PREFIX}feed`, `{b.PREFIX}cry`, `{b.PREFIX}bite`", inline=False)
		alls.add_field(name=f":beginner: Остальное", value=f"`{b.PREFIX}info`, `{b.PREFIX}help`, `{b.PREFIX}report`, `{b.PREFIX}bug`", inline=False)
		alls.add_field(name=f":ghost: Глобальный чат", value=f"`Для информации выберите меню помощи по глобальному чату`", inline=False)
		alls.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")

		mod = discord.Embed(title=f":shield: Модерация", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
		mod.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		mod.add_field(name=f"{b.PREFIX}clear", value=f"Синтаксис: {b.PREFIX}clear (количество сообщений). Удаляет определенное количество сообщений в канале!", inline=False)
		mod.add_field(name=f"{b.PREFIX}mute", value=f"Синтаксис: {b.PREFIX}mute (участник) (время и буква времянного промяжутка (s, m, h, d, w)) (причина). Временный мут участника! Если поставить слишком большое число, то бот проигнорирует команду!", inline=False)
		mod.add_field(name=f"{b.PREFIX}infinitymute", value=f"Синтаксис: {b.PREFIX}infinitymute (участник) (причина). Перманентный мут участника!", inline=False)
		mod.add_field(name=f"{b.PREFIX}unmute", value=f"Синтаксис: {b.PREFIX}unmute (участник). Снятие мута с участника!", inline=False)
		mod.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		mod.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		mod.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		mod.add_field(name=f"{b.PREFIX}report", value=f"Синтаксис: {b.PREFIX}report (текст жалобы с id, именем пользователя и самой жалобой). Написание жалобы на участника", inline=False)
		mod.add_field(name=f"{b.PREFIX}bug", value=f"Синтаксис: {b.PREFIX}bug (подробное описание ошибки бота). Нашли ошибку в боте? Помогите нам исправить её, сообщив о её существовании", inline=False)
		mod.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")

		fun = discord.Embed(title=f":diamond_shape_with_a_dot_inside: Фан", description="", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
		fun.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		fun.add_field(name=f"{b.PREFIX}owl", value="Случайное фото совы", inline=False)
		fun.add_field(name=f"{b.PREFIX}catowl", value="Случайное фото совы с головой кота", inline=False)
		fun.add_field(name=f"{b.PREFIX}meme", value="Отправляет случайный мем", inline=False)
		#fun.add_field(name=f"{b.PREFIX}unmute", value=f"Синтаксис: {b.PREFIX}unmute (участник). Снятие мута с участника!", inline=False)
		#fun.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		#fun.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		#fun.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		fun.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")

		rp = discord.Embed(title=f":infinity: Ролеплей", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
		rp.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		rp.add_field(name=f"{b.PREFIX}kiss", value=f"Синтаксис: {b.PREFIX}kiss (участник). Поцеловать участника", inline=False)
		rp.add_field(name=f"{b.PREFIX}kill", value=f"Синтаксис: {b.PREFIX}kill (участник). Убить участника", inline=False)
		rp.add_field(name=f"{b.PREFIX}feed", value=f"Синтаксис: {b.PREFIX}feed (участник). Покормить участника", inline=False)
		rp.add_field(name=f"{b.PREFIX}cry", value=f"Начать плакать", inline=False)
		rp.add_field(name=f"{b.PREFIX}bite", value=f"Синтаксис: {b.PREFIX}bite (участник). Укусить участника", inline=False)
		#rp.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		#rp.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		#rp.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		rp.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")

		oth = discord.Embed(title=f":beginner: Остальное", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
		oth.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		oth.add_field(name=f"{b.PREFIX}info", value=f"Синтаксис: {b.PREFIX}info (участник). Просмотр информации об участнике", inline=False)
		oth.add_field(name=f"{b.PREFIX}help", value=f"Показ меню помощи по командам", inline=False)
		oth.add_field(name=f"{b.PREFIX}serverinfo", value=f"Посмотреть информацию о сервере", inline=False)
		oth.add_field(name=f"{b.PREFIX}avatar", value=f"Синтаксис: {b.PREFIX}avatar (участник). Отправляет аватар участника", inline=False)
		oth.add_field(name=f"{b.PREFIX}translator", value=f"Синтаксис: {b.PREFIX}translator (язык, на который перевести (en, ru и т д)) (текст). Перевод вашего текста", inline=False)
		oth.add_field(name=f"{b.PREFIX}ping", value="Показ задержки бота", inline=True)
		#oth.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		#oth.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		#oth.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		oth.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")

		gl = discord.Embed(title=f":ghost: Глобальный чат", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
		gl.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		gl.add_field(name=f"Описание", value=f"Глобальный чат позволяет общаться с людьми с других серверов, где есть канал глобального чата и присутствует данный бот", inline=False)
		gl.add_field(name=f"Использование", value=f"Для включения данной функции вам требуется создать канал с названием '`global-chat`'\nПосле создания канала можно начанать общаться, просто отправляя туда обычные сообщения", inline=False)
		gl.add_field(name=f"Правила общения в глобальном чате", value=f"**1. Не рекламировать сервера!**\n**2. Не отправлять скам-ссылки, или ссылки которые нарушают правила Discord!**\n**3. Не флудить/спамить!**\n**4. Не кидать NSFW (Not Save For Work (18+)) изображения!**\n**5. Не отправлять в данный чат никаких команд!**", inline=False)
		gl.add_field(name=f"Примечания", value=f"Менять название канала нельзя, в противном случае чат перестанет работать\nЗа нарушение правил глобального чата вам может быть выдан бан глобального чата\nЕсли вы заметили нарушение правил глобального чата, напишите `{b.PREFIX}report` с описанием нарушения, id и полным ником с тегом пользователя, совершивсего нарушение", inline=False)
		gl.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")

		err = discord.Embed(title="Error", description="Извините, но данной категории помощи не существует!", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)




		message = await ctx.send(embed = alls, components=[
			Select(
			placeholder="Выбери нужный модуль помощи!",
			options=[
				SelectOption(label="✳️ » Все команды", value= '1'),
				SelectOption(label="🛡️ » Модерация", value= '2'),
				SelectOption(label="💠 » Фан", value= '3'),
				SelectOption(label="♾️ » Ролеплей", value= '4'),
				SelectOption(label="🔰 » Остальное", value= '5'),
				SelectOption(label="👻 » Глобальный чат", value= '6'),
				],
				custom_id="select1",
			)
		])
		
		while True:
			interaction = await b.bot.wait_for("select_option", check = lambda inter: inter.custom_id == "select1" and inter.user == ctx.author)
			res = interaction.values[0]
			if res == '1':
				await message.edit(embed = alls)
				await interaction.respond(type=6)
			elif res == '2':
				await message.edit(embed = mod)
				await interaction.respond(type=6)
			elif res == '3':
				await message.edit(embed = fun)
				await interaction.respond(type=6)
			elif res == '4':
				await message.edit(embed = rp)
				await interaction.respond(type=6)
			elif res == '5':
				await message.edit(embed = oth)
				await interaction.respond(type=6)
			elif res == '6':
				await message.edit(embed = gl)
				await interaction.respond(type=6)
			else:
				await message.edit(embed = err)
				await interaction.respond(type=6)










def setup(bot):
	bot.add_cog(Help(bot))