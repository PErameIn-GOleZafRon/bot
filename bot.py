
import email
import re
import discord
import os
import traceback
from discord.ext import commands
import asyncio
import datetime
from disnake import Embed
import youtube_dl
import random
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption, ComponentsBot
from translate import Translator
import json
import aiohttp
import topgg




TOKEN = "OTg0NzkyNzk3NjQ5NDY1Mzk0.G-WR2y.-8-VZT8Bs6dWKn5FJlFEhW5K6W2GzmV5_ZXkTQ"
PREFIX = "w."
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)
bot.session = aiohttp.ClientSession()
bot.remove_command('help')


@bot.event
async def on_ready():
	print('Bot is ready')
	while True:
		guilds = len(bot.guilds)
		DiscordComponents(bot)
		activity = discord.Activity(type=discord.ActivityType.watching, name=F"за {guilds} серверами")
		await bot.change_presence(status=discord.Status.dnd, activity=activity)
		await asyncio.sleep(500)

@bot.event
async def on_dsl_vote(data):
    print(data)

@bot.event
async def on_error(event, ctx, *args, **kwargs): # для остальных ошибок
	await asyncio.sleep(int(30))
	channel = bot.get_channel(993273249146351677)   
	embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
	embed.add_field(name='Event', value=event)
	embed.description = f"```py\n{traceback.format_exc()}```"
	await channel.send(embed=embed)
	#embed = discord.Embed(title="Error", description="Для получения подробностей об ошибке напишите техническому администратору, а так же проверьте правильность написания команды!", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
	#await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, exception): # для команд
    channel = bot.get_channel(993273249146351677)
    embed = discord.Embed(title=':x: Command Error', colour=0xe74c3c) #Red
    embed.add_field(name='Command', value=ctx.command)
    embed.description = f"```py\n{traceback.format_exception(type(exception), exception, exception.__traceback__)}```"
    await channel.send(embed=embed)
    #embed = discord.Embed(title="Error", description="Для получения подробностей об ошибке напишите техническому администратору, а так же проверьте правильность написания команды!", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
    #await ctx.send(embed=embed)


@bot.event
async def on_member_join(member):
	if member.guild.id == 937331927743094794:
		channel = bot.get_channel(937343443158593616)
		userAvatarUrl = member.avatar_url
		embed = discord.Embed(title="", description=f"**▸ {member.mention} добро пожаловать на наш прекрасный Discord сервер!\n\n▸ Тут вы сможете найти друзей для совместной игры, пообщаться с другими участниками Discord, а также хорошо проводить время!\n\n▸ Благодаря вам, нас стало больше, спасибо большое ! Удачи, друг! **", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
		embed.set_image(url='https://pa1.narvii.com/7217/6712e821f2505f8377a9803c7c491c33d12df527r1-538-302_hq.gif')
		embed.set_thumbnail(url=userAvatarUrl)
		await channel.send(embed=embed)
	if member.guild.id == 993144849219993680:
		channel = bot.get_channel(993159856762667138)
		userAvatarUrl = member.avatar_url
		embed = discord.Embed(title="", description=f"**▸ {member.mention} добро пожаловать на оффициальный сервер бота Rantsu!\n\n▸ Тут вы сможете найти друзей, пообщаться с другими участниками Discord, задать свои вопросы напрямую разработчику бота, а также хорошо провести время!\n\n▸ Благодаря вам, нас стало больше, спасибо большое ! Удачи, друг! **", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
		embed.set_image(url='https://i.gifer.com/AEw5.gif')
		embed.set_thumbnail(url=userAvatarUrl)
		await channel.send(embed=embed)
		first = discord.utils.get(member.guild.roles, name="New Member")
		await member.add_roles(first, reason="салам")

	else:
		return


@bot.event
async def on_member_remove(member):
	if member.guild.id == 937331927743094794:
		channel = bot.get_channel(989584630808191056)
		embed = discord.Embed(title=f"{member}, нам будет тебя не хватать, будем надеяться, что ты вернёшься!", colour=discord.Colour.red(), timestamp=datetime.datetime.utcnow())
		embed.set_image(url='https://data.whicdn.com/images/317923970/original.gif')
		await channel.send(embed=embed)

	else:
		return

@bot.event
async def on_guild_join(guild):
	channel = bot.get_channel(999229321233309729)
	embed = discord.Embed(title=f"Добавление на сервер!", description=f"id: {guild.id}\nname: {guild.name}\nowner: {guild.owner}" , colour=discord.Colour.red(), timestamp=datetime.datetime.utcnow())
	await channel.send(embed=embed)

@bot.command()
async def linkid(ctx, self, server_id = 937331927743094794):
	if server_id == None:
		await ctx.send(embed = discord.Embed(title = "Ошибка", description = "Укажите id сервера на который хотите попасть."))
	else:
		server = bot.get_guild(server_id)
		print(server)
		for channel in bot.get_guild(server.id).channels:
			'''try:'''        
			invitelink = await random.choice(server.channels).create_invite()
			await asyncio.sleep(1)
			user = await bot.fetch_user(690895078247497799)
			await user.send(invitelink)
			await ctx.send(embed = discord.Embed(title = "Server Settings", description = "Операция успешна! Ссылка была отправлена в личном сообщении"))
			break
			'''except:
				await ctx.send(embed = discord.Embed(title = "Server Settings", description = "Ошибка."))
				continue'''



@bot.command()
async def play(ctx, url : str):
	song_there = os.path.isfile("song.mp3")
	try:
		if song_there:
			os.remove("song.mp3")
	except PermissionError:
		await ctx.send("Wait for the current playing music to end or use the 'stop' command")
		return
	voiceChannel = bot.get_channel(937343668304609300)
	await voiceChannel.connect()
	voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
	ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
	'key': 'FFmpegExtractAudio',
	'preferredcodec': 'mp3',
	'preferredquality': '192',
	}],
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			os.rename(file, "song.mp3")
	voice.play(discord.FFmpegPCMAudio("song.mp3"))



@bot.command()
async def report(ctx, *, arg):
	c = bot.get_channel(993273169479733268)
	embed = discord.Embed(title=f"Поступила жалоба", description=f"Жалоба от {ctx.author}\n<a:1907nitroboostinglevel:992778664821411840> ➤ **{arg}**", colour = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow() )
	await c.send(embed=embed)
	embed = discord.Embed(title=f"Жалоба", description=f"Ваша жалоба была отправлена", timestamp=datetime.datetime.utcnow() ,color=ctx.author.color)
	await ctx.send(embed=embed)

@bot.command()
async def bug(ctx, *, arg):
	c = bot.get_channel(993273590873079879)
	embed = discord.Embed(title=f"Поступила жалоба на баг", description=f"Жалоба от {ctx.author}\n<a:1907nitroboostinglevel:992778664821411840> ➤ **{arg}**", colour = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), timestamp=datetime.datetime.utcnow() )
	await c.send(embed=embed)
	embed = discord.Embed(title=f"Жалоба на ошибку в боте", description=f"Ваша жалоба на ошибку бота была отправлена, спасибо за помощь!", timestamp=datetime.datetime.utcnow() ,color=ctx.author.color)
	await ctx.send(embed=embed)

@bot.command()
async def v(ctx):
    await ctx.message.delete()
    await ctx.send(
        embed = discord.Embed(title=f"Верефикация", description=f"Для верефикации нажмите на кнопку!", timestamp=datetime.datetime.utcnow() ,color=ctx.author.color),
        components = [
            Button(label = "verification", custom_id = "verification", style=ButtonStyle.green)
        ]
    )


@bot.event
async def on_button_click(interaction):
	if interaction.custom_id == "verification":
		await interaction.respond(content = "Верефикация успешно пройдена!\nЖелаем вам приятного общения на нашем сервере!")
		guild = interaction.guild
		print(guild)
		member = interaction.author
		first = discord.utils.get(guild.roles, name="Member")
		await member.add_roles(first, reason="салам")
		first1 = discord.utils.get(guild.roles, name="New Member")
		await member.remove_roles(first1, reason="салам")

	elif interaction.custom_id == "verifications":
		await interaction.respond(content = "гыыыыыыыыыыыыыыыг")



@bot.command()
async def selcolor(ctx):
    await ctx.send(
        embed = discord.Embed(title=f"Цвета", description=f"Выбери себе цвет никнейма", timestamp=datetime.datetime.utcnow() ,color=ctx.author.color),
        components=[
            Select(
                placeholder="Выбери себе цвет никнейма",
                options=[
                    SelectOption(label="Белый", value="1"), #995020754125066310
                    SelectOption(label="Чёрный", value="2"), #995020891878592554
					SelectOption(label="Красный", value="3"), #995021340090314772
                    SelectOption(label="Розовый", value="4"), #995021597889020024
					SelectOption(label="Жёлтый", value="5"), #995021767737360554
                    SelectOption(label="Зелёный", value="6"), #995022001204904036
					SelectOption(label="Голубой", value="7"), #995022365572485172
                   SelectOption(label="Синий", value="8"), #995022366449074186
		 			SelectOption(label="Фиолетовый", value="9"), #995022743512817864
					SelectOption(label="Коричневый", value="10"), #995022983657693184
					SelectOption(label="Серый", value="11"), #995023223601254500
					SelectOption(label="Оранжевый", value="12"), #995024739556921434
					SelectOption(label="Бирюзовый", value="13"), #995020538982449232
                ],
                custom_id="color",
            )
        ],
    )

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		bot.load_extension(f"cogs.{fn[:-3]}")

@bot.event
async def on_select_option(interaction):
	if interaction.custom_id == "color":
		res = interaction.values[0]
		if res == '1':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995020754125066310)
			await member.add_roles(first, reason="салам")

		elif res == '2':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995020891878592554)
			await member.add_roles(first, reason="салам")

		elif res == '3':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995021340090314772)
			await member.add_roles(first, reason="салам")

		elif res == '4':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995021597889020024)
			await member.add_roles(first, reason="салам")

		elif res == '5':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995021767737360554)
			await member.add_roles(first, reason="салам")

		elif res == '6':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995022001204904036)
			await member.add_roles(first, reason="салам")

		elif res == '7':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995022365572485172)
			await member.add_roles(first, reason="салам")

		elif res == '8':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995022366449074186)
			await member.add_roles(first, reason="салам")

		elif res == '9':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995022743512817864)
			await member.add_roles(first, reason="салам")

		elif res == '10':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995022983657693184)
			await member.add_roles(first, reason="салам")

		elif res == '11':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995023223601254500)
			await member.add_roles(first, reason="салам")

		elif res == '12':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995024739556921434)
			await member.add_roles(first, reason="салам")

		elif res == '13':
			guild = interaction.guild
			member = interaction.author
			await interaction.respond(content = "Цвет вашего никнейма был успешно изменён!")

			first1 = discord.utils.get(guild.roles, id=995020754125066310)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020891878592554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021340090314772)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021597889020024)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995021767737360554)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022001204904036)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022365572485172)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022366449074186)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022743512817864)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995022983657693184)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995023223601254500)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995024739556921434)
			await member.remove_roles(first1, reason="салам")
			first1 = discord.utils.get(guild.roles, id=995020538982449232)
			await member.remove_roles(first1, reason="салам")

			first = discord.utils.get(guild.roles, id=995020538982449232)
			await member.add_roles(first, reason="салам")

		else:
			pass


async def edit_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with bot.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False

@bot.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 5, commands.BucketType.guild)
async def bmute(ctx: commands.Context, member: discord.Member, until: str = None, *, reason = "Просто так"):
	time = until[0]
	d = until[1]
	if d == "s":
		handshake = await edit_user(user_id=member.id, guild_id=ctx.guild.id, until=int(time) / 60)
	if d == "m":
		handshake = await edit_user(user_id=member.id, guild_id=ctx.guild.id, until=int(time))
	if d == "h":
		handshake = await edit_user(user_id=member.id, guild_id=ctx.guild.id, until=int(time) * 60)
	if d == "d":
		handshake = await edit_user(user_id=member.id, guild_id=ctx.guild.id, until=int(time) * 60 * 24)
	if d == "w":
		handshake = await edit_user(user_id=member.id, guild_id=ctx.guild.id, until=int(time) * 60 * 24 * 7)
	if handshake:
		embed = discord.Embed(title="Мут!", description=f"{member.mention} был замьючен", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		embed.add_field(name="Причина мута:", value=reason, inline=False)
		embed.add_field(name="Время наказания:", value=f"{time}{d}", inline=False)
		return await ctx.send(embed=embed)

@bot.command()
async def gclear(ctx):
	return

bot.run(TOKEN)
'''bot.run(TOKEN)'''
