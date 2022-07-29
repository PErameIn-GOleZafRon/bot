import discord
import os
import datetime
import asyncio
from discord.ext import commands
import aiohttp
import random
import youtube_dl
from translate import Translator
import bot as b

TOKEN = "OTg0NzkyNzk3NjQ5NDY1Mzk0.G-WR2y.-8-VZT8Bs6dWKn5FJlFEhW5K6W2GzmV5_ZXkTQ"
PREFIX = "w."
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)


class Mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(ctx):
		print("mod cog on")

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def ping(self, ctx):
		embed = discord.Embed(title=f"🏓Pong! {round(self.bot.latency * 1000)}ms", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def clear(self, ctx, amount=6):
		embed = discord.Embed(title=f"Очищаю чат от ненужных вам сообщений", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)
		await ctx.channel.purge(limit=amount)
		embed = discord.Embed(title=f"Очищенно - {amount}!\nОчистка окончена!", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def mute(self, ctx, member: discord.Member, time, d, reason="Просто так"):
		guild = ctx.guild
		role = discord.utils.get(guild.roles, name="Muted") 
		print ("выдан мут!")

		if not role:
			role = await guild.create_role(name="Muted")

			for channel in guild.channels:
				await channel.set_permissions(role, speak=False, send_messages=False)

		await member.add_roles(role)
		embed = discord.Embed(title="Мут!", description=f"{member.mention} был замьючен", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		embed.add_field(name="Причина мута:", value=reason, inline=False)
		embed.add_field(name="Время наказания:", value=f"{time}{d}", inline=False)
		await ctx.reply(embed=embed)
		if d == "s":
			await asyncio.sleep(int(time))
		if d == "m":								
			await asyncio.sleep(int(time*60))
		if d == "h":
			await asyncio.sleep(int(time*60*60))
		if d == "d":
			await asyncio.sleep(int(time*60*60*24))
		await member.remove_roles(role)
		embed = discord.Embed(title="Мут", description=f"Пользователь {member.mention} был размьючен", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		await ctx.reply(embed=embed)
	            
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def infinitymute(self, ctx, member: discord.Member, *, reason="Просто так"):
	    guild = ctx.guild
	    mutedRole = discord.utils.get(guild.roles, name="Muted")

	    if not mutedRole:
	        mutedRole = await guild.create_role(name="Muted")

	        for channel in guild.channels:
	            await channel.set_permissions(mutedRole, speak=False, send_messages=False)
	    embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
	    embed.add_field(name="Reason:", value=reason, inline=False)
	    await ctx.reply(embed=embed)
	    await member.add_roles(mutedRole, reason=reason)
	    await member.send(f"You have been muted from: {guild.name} Reason: {reason}")


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member):
	    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	    await member.remove_roles(mutedRole)
	    await member.send(f"Вы были размьючены: {ctx.guild.name}")
	    embed = discord.Embed(title="Размут", description=f"Пользователь {member.mention} был размьючен", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
	    await ctx.reply(embed=embed)

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def kick(self, ctx, member: discord.Member, reason="Просто так"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, пожалуйста, введите пользователя!", color=ctx.author.color)
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Кик!", description=f"{member.mention} был кикнут!!\nБольше он вас не потревожит", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Причина: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.kick(user=member)

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def tempban(self, ctx, member: discord.Member, time, d, *, reason="Просто так"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, пожалуйста, введите пользователя!", color=ctx.author.color)
			await ctx.reply(embed=embed)
			

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Бан!", description=f"{member.mention} был забанен!\nЭтот парень был из тех, кто просто любит жизнь!", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Причина: ", value=reason, inline=False)
			embed.add_field(name="Время наказания:", value=f"{time}{d}", inline=False)
			await ctx.reply(embed=embed)
			await guild.ban(user=member)

			if d == "s":
				await asyncio.sleep(int(time))
				await guild.unban(user=member)
			if d == "m":
				await asyncio.sleep(int(time*60))
				await guild.unban(user=member)
			if d == "h":
				await asyncio.sleep(int(time*60*60))
				await guild.unban(user=member)
			if d == "d":
				await asyncio.sleep(time*60*60*24)
				await guild.unban(int(user=member))

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def ban(self, ctx, member: discord.Member, reason="Просто так"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, пожалуйста, введите пользователя!")
			await ctx.reply(embed=embed)
		else:
			guild = ctx.guild
			embed = discord.Embed(title="Бан!", description=f"{member.mention} был забанен перманентно!\nМне очень жаль, наверное\nХотя... Не жаль\nЕсли тебя забанили, значит была причина", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Причина: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.ban(user=member)



	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def unban(self, ctx, user: discord.User):
		if user == None:
			embed = discord.Embed(f"{ctx.message.author}, пожалуйста, введите пользователя!", color=ctx.author.color)
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Разбан!", description=f"{user.display_name} был разбанен!\nУра, ты снова с нами!", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
			await ctx.reply(embed=embed)
			await guild.unban(user=user)
	
	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def link(self, ctx):
		invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
		await ctx.author.send(invitelink)
		print (invitelink)
		embed = discord.Embed(title="", description=f"Успешно :)", color=ctx.author.color(), timestamp=datetime.datetime.utcnow())
		await ctx.reply(embed=embed)

	@commands.command()
	async def avatar(self, ctx, *,  avamember : discord.Member=None):
		userAvatarUrl = avamember.avatar_url
		embed = discord.Embed(title=f"Аватар пользователя {avamember}", description=f"[Ссылка на аватар пользователя]({userAvatarUrl})", color=ctx.author.color, timestamp=datetime.datetime.utcnow())
		embed.set_image(url=userAvatarUrl)
		await ctx.reply(embed=embed)

	@commands.command()
	async def kiss(self, ctx, member: discord.Member = None):
		kiss = ['https://aniyuki.com/wp-content/uploads/2021/07/aniyuki-anime-gif-kiss-35.gif',
        'https://acegif.com/wp-content/uploads/anime-kissin-11.gif',
        'https://pa1.narvii.com/7193/5504fe828eb263e4b80a316efb3cecb48bee95adr1-500-275_hq.gif',
        'https://pa1.narvii.com/7576/ac3f13fbf249854aba0aefc81243da48ca42f31dr1-540-300_hq.gif',
        'https://safebooru.org/images/1892/377044c2bc11cebf89a4465b0e547523b4d1e1d8.gif?1974662',
        'https://i.pinimg.com/originals/86/d4/a0/86d4a046c8a32a28341353fc95bedc82.gif',
        'https://pa1.narvii.com/7248/cb59ac479e5d8e25954ad28dbbeae9e8e87d04adr1-500-281_hq.gif',
        'https://i.gifer.com/7pDW.gif'
        ]
		if member is None:
			member = ctx.author
		await ctx.message.delete()
		embed = discord.Embed(color=ctx.author.color, title=f"")
		embed.description = f"**{ctx.author.mention} поцеловал {member.mention}**"
		url = (random.choice(kiss))
		embed.set_image(url=url)
		await ctx.send(embed=embed)


	@commands.command()
	async def feed(self, ctx, member: discord.Member = None):
		feed = ['https://images-ext-1.discordapp.net/external/EXCeATaurEsrH2AmgcuOqCFCDnvhgk5SKVw5qrJ6On4/https/cdn.nekos.life/feed/feed_015.gif',
        'https://images-ext-2.discordapp.net/external/_4-o725T5ZifxbMq8-f_nburUtHzNRlsVtRhqWWO5Kg/https/cdn.nekos.life/feed/feed_014.gif',
        'https://images-ext-2.discordapp.net/external/tYHu5qu789hJU7it4TTFWawhLypQz6tL1q-T-5Ob1tw/https/cdn.nekos.life/feed/feed_006.gif',
        'https://images-ext-1.discordapp.net/external/zFb9-5aVV72nrgYGtgGqcvWazgVvzsxqxAVsmJ7P_JY/https/cdn.nekos.life/feed/feed_016.gif',
        'https://images-ext-1.discordapp.net/external/kmA1Ay6Y_qtfTOH7WuaElerKAUOYOwYjA6s3_-9luiA/https/cdn.nekos.life/feed/feed_012.gif',
        'https://images-ext-1.discordapp.net/external/clGX4GPfQr7wXPh62n5oPNpA7goIQuqTznDAJypvgJc/https/cdn.nekos.life/feed/feed_001.gif',
        'https://images-ext-2.discordapp.net/external/AVFiEzqVWWryI7nRAjUWNXqylnYhAykvuDwhVSCrHdI/https/cdn.nekos.life/feed/feed_007.gif'
        ]
		if member is None:
			member = ctx.author
		await ctx.message.delete()
		embed = discord.Embed(color=ctx.author.color, title=f"")
		embed.description = f"**{ctx.author.mention} покормил {member.mention}**"
		url = (random.choice(feed))
		embed.set_image(url=url)
		await ctx.send(embed=embed)


	@commands.command()
	async def bite(self, ctx, member: discord.Member = None):
		bite = ['https://media.discordapp.net/attachments/889573796070162432/889573892207804466/image0.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573892530782208/image1.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573893772283944/image3.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573894258843668/image4.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573894598574121/image5.gif',
        'https://media.discordapp.net/attachments/889573796070162432/889573895470972958/image7.gif',
        'https://pa1.narvii.com/6687/26eaef4b158aab82e6a4c4ba91693da496372016_hq.gif',
        'https://data.whicdn.com/images/330399899/original.gif',
        'https://safebooru.org/images/434/50fe28ee97b380945562ce981c1c07906d597193.gif?434412',
        'https://pa1.narvii.com/6639/abe8af3d6c24ce150705711a8d8f032bfafb5eba_hq.gif'
        'https://giffiles.alphacoders.com/192/192308.gif'
        ]
		if member is None:
			member = ctx.author
		await ctx.message.delete()
		embed = discord.Embed(color=ctx.author.color, title=f"")
		embed.description = f"**{ctx.author.mention} укусил {member.mention}**"
		url = (random.choice(bite))
		embed.set_image(url=url)
		await ctx.send(embed=embed)


	@commands.command()
	async def kill(self, ctx, member: discord.Member = None):
		kill = ['https://i.gifer.com/embedded/download/DTBu.gif',
        'https://anime-chan.me/uploads/posts/2013-11/1383368840_hellsing.gif',
        'https://c.tenor.com/VX45OoPs008AAAAC/gun-to-head-gun.gif',
        'https://i.gifer.com/BQQ2.gif',
        'https://pa1.narvii.com/7086/05e2ec586ba1853322f23c767ac2e3ad17312b18r1-500-280_hq.gif',
        'https://forum.nextrp.ru/data/avatars/o/96/96188.jpg?1629011641',
        'https://c.tenor.com/vRf2kACZsBEAAAAC/anime-mad.gif'
        ]
		if member is None:
			member = ctx.author
		await ctx.message.delete()
		embed = discord.Embed(color=ctx.author.color, title=f"")
		embed.description = f"**{ctx.author.mention} убил {member.mention}**"
		url = (random.choice(kill))
		embed.set_image(url=url)
		await ctx.send(embed=embed)


	@commands.command()
	async def cry(self, ctx):
		cry = ['https://data.whicdn.com/images/179970750/original.gif',
        'https://pa1.narvii.com/5913/2f70696c1c4f74f5b3db6fbff0751a468536fe3d_hq.gif',
        'https://steamuserimages-a.akamaihd.net/ugc/910155957957203000/D69F10FE720A4E4BB3727FFA1E6BD4DF830EC488/?imw=512&amp;imh=307&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true',
        'https://images-ext-1.discordapp.net/external/yR2o7w2-5yQS6rneIN0_IRxeH5c4HA0Bim4B-CW1iyw/%3Fitemid%3D5086387/https/media1.tenor.com/images/87ef2f7663b9dc4bf39b7e9481cda842/tenor.gif',
        'https://images-ext-2.discordapp.net/external/XvfxZN06qz5UcXd95HbQii-qFZKQ0kyfxDJILsA0le4/%3Fitemid%3D5652241/https/media1.tenor.com/images/49e4248f18b359dd46f7b60b01d1a4a0/tenor.gif',
        'https://i.gifer.com/embedded/download/FLIw.gif',
        'https://images-ext-1.discordapp.net/external/lQAgqWLJBBjf7xNM70vTsGuNCOr1fAR988V7gOXPuPg/%3Fitemid%3D7552065/https/media1.tenor.com/images/4bb996f5c99d48faf8590d8c66396065/tenor.gif'
        ]
		await ctx.message.delete()
		embed = discord.Embed(color=ctx.author.color, title=f"")
		embed.description = f"**{ctx.author.mention} плачет**"
		url = (random.choice(cry))
		embed.set_image(url=url)
		await ctx.send(embed=embed)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def dev(self, ctx):
		embed = discord.Embed(title="Разработчик бота", description="Разработчиком / владельцем бота является @Сова#3269", color=ctx.author.color)
		await ctx.send(embed=embed)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def info(self, ctx,member:discord.Member = None, guild: discord.Guild = None):
		await ctx.message.delete()

		if member == None:
			member = ctx.author

		allroles = [role for role in member.roles]

		emb = discord.Embed(title="Информация о пользователе", description=f"Пользователь: **{member}**\nНикнейм: **{member.display_name}**\nАйди пользователя: **{member.id}**", color=member.color)
		
		t = member.status
		if t == discord.Status.online:
			d = " В сети"
		t = member.status
		if t == discord.Status.offline:
			d = "⚪ Не в сети"
		t = member.status
		if t == discord.Status.idle:
			d = " Не активен"
		t = member.status
		if t == discord.Status.dnd:
			d = " Не беспокоить"

		emb.add_field(name="Активность:", value=d,inline=True)
		emb.add_field(name="Статус:", value=f"{member.activity}",inline=True)
		emb.add_field(name="Все роли пользователя:", value="/".join(role.mention for role in allroles),inline=False)
		emb.add_field(name="Дата присоединения:", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"),inline=True)
		emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"),inline=True)
		emb.set_thumbnail(url=member.avatar_url)
		await ctx.send(embed = emb)

	@commands.command()
	async def serverinfo(self, ctx):
		region = ctx.guild.region
		icon_url=ctx.guild.icon_url
		owner = ctx.guild.owner.mention
		ownerid = ctx.guild.owner.id
		ownerc = ctx.guild.owner.color
		all = len(ctx.guild.members)
		members = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
		bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
		statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]
		channels = [len(list(filter(lambda m: str(m.type) == "text", ctx.guild.channels))),
                    len(list(filter(lambda m: str(m.type) == "voice", ctx.guild.channels))),
                    len(list(ctx.guild.categories)),
                    len(list(ctx.guild.roles))]
		voice = set()
		for v in ctx.guild.voice_channels:
			for member in v.members:
				voice.add(member.id)

		emojis = set()
		for emoji in ctx.guild.emojis:
			emojis.add(emoji.id)

		embed = discord.Embed(title=f"Информация сервера", description=f"<:8380badgeserverbooster6:991372278048763974> Название сервера: **{ctx.guild} (`{ctx.guild.id}`)**\n<:8380badgeserverbooster8:991372275930644592> Владелец: **{owner} (`{ownerid}`)**", color = ownerc)
		embed.add_field(name="Другое", value=f"<:2487badgeserverbooster91:991372273955123341> Забаненых пользователей: **{len(await ctx.guild.bans())}**\n<:8600badgeserverbooster5:991372271040073789> Приглашений: **{len(await ctx.guild.invites())}**", inline=False)
		embed.add_field(name="<:6427badgeserverbooster4:991372269735649370> Сервер создан", value=ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=False)

		embed.add_field(name=f"<:6245badgeserverbooster8:991372261951021176> Участники **[{all}]**", value=f"В сети: **{statuses[0] + statuses[1] + statuses[2]}**\nНе в сети: **{statuses[3]}**\nЛюдей: **{members}**\nБотов: **{bots}**", inline=True)
		embed.add_field(name=f"<:7815badgeserverbooster3:991372259799343145> Каналы **[{channels[0] + channels[1]}]**", value=f"Текстовых: **{channels[0]}** \nГолосовых: **{channels[1]}**\nКатегорий: **{channels[2]}**", inline=True)
		embed.add_field(name="<:8586badgeserverbooster:991372257970638890> Статистика", value=f"Ролей: **{channels[3]}**\nВ ГС: **{len(voice)}**\nЭмоджи: **{len(emojis)}**", inline=True)
		await ctx.send(embed=embed)

	@commands.command()
	async def emojis(self, ctx):
		for emoji in ctx.guild.emojis:
			print(f"<a:{emoji.name}:{emoji.id}>")
			embed = discord.Embed(title=f"```<a:{emoji.name}:{emoji.id}>```", description=f"<:{emoji.name}:{emoji.id}>")
			await ctx.send(embed=embed)


	@commands.command()
	async def translator(self, ctx, lang, *, text):
		translator= Translator(to_lang=lang)
		translation = translator.translate(text)
		embed = discord.Embed(title="Перевод", description=f"**Исходный текст:**\n{text}\n**Перевод:**\n{translation}", color=ctx.author.color)
		await ctx.send(embed=embed)

	@commands.command()
	async def rantrules(self, ctx):
		embed = discord.Embed(title=f"**ПРАВИЛА**", description=f"")
		embed.add_field(name=f"**Пункт 1**", value=f"[1.1]Участники сервера Дискорд равны перед правилами вне зависимости от опыта и роли.\n\n[1.2]Мат разрешается, но без злоупотребления.\n\n[1.3]Запрещено оскорбление других пользователей.\n\n[1.4]Нельзя использовать NSFW: шок-контент, порнографию.\n\n[1.5]Запрещено злоупотребление Caps Lock.\n\n[1.6]Запрещены все типы флуда.\n\n[1.7]Запрещается жесткий троллинг.\n\n[1.8]Администрация имеет право менять правила в любое время не предупреждая участников.\n\n[1.9]Fдминистрация имеет право выносить наказания по своему усмотрению даже если данное правило отсутствует, но считает что данное действие нарушает порядок на сервере.", inline=False)
		embed.add_field(name=f"**Пункт 2**", value=f"[2.1]Запрещается реклама без согласования с администратором.\n\n[2.2]Не допускается спам-рассылка в личных СМС с другими пользователями.\n\n[2.3]Нельзя кидать ссылки с доменами на Ютуб, ВК, Вики и тд. Размещение ссылки по согласованию с администратором.", inline=False)
		embed.add_field(name=f"**Пункт 3**", value=f"[3.1]Нельзя включать музыку в микрофон.\n\n[3.2]Не допускается издание громких звуков в микрофон.\n\n[3.3]При наличии шума вокруг рекомендуется применение Push-To-Talk.", inline=False)
		embed.add_field(name=f"**Пункт 4**", value=f"[4.1]Администратор вправе требовать изменение ника и картинки, если считает, что они оскорбляют кого-либо.\n\n[4.2]Запрещены ники типа User, Discord User, NickName и прочие, в том числе Admin, Moderator и т. д.\n\n[4.3]Запрещено использование имен с матом, оскорблением, религиозными названиями, рекламой, пропагандой алкоголя / наркотиков.\n\n[4.4]Не допускается применение символики террористов и запрещенных организации, призыв к насилию и экстремизму.\n\n[4.5]Нельзя использовать бессмысленный набор символов с многократным повторением одной или нескольких букв.\n\n[4.6]Не допускаются картинки с ненормативной лексикой, оскорблением и прочими запрещенными вещами, о которых упоминалось выше.", inline=False)
		embed.add_field(name=f"**Пункт 5**", value=f"[5.1]На название канала распространяются те же требования, что и для сервера Дискорд.\n\n[5.2]В любом канале / подканале запрещена публикация ссылок на донат-сайты, площадки приема платежей, спонсорской помощи, пожертвований и других сервисов.", inline=False)
		embed.add_field(name=f"**Пункт 6**", value=f"[6.1]При нарушении правил сервера Дискорд принимаются меры к пользователям вплоть до ограничения доступа.\n\n[6.2]Обход бана путем входа под другим идентификатором или иными путями — бан.\n\n[6.3]Администратор ДС вправе отказать в доступе любому участнику. Он не обязан указывать причины или предупреждать об этом.\n\n[6.4]Нарушение упомянутых выше норм — бан.\n\n[6.5]Неуважительное отношение к другим пользователям и оскорбление — бан.\n\n[6.6]Разжигание межнациональной розни, конфликтов на политической и религиозном основании — бан.", inline=False)
		embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
		embed.set_image(url="https://egammi.com/images/2017/06/17/KWhf.gif")
		await ctx.send(embed=embed)
		
	@commands.command()
	@commands.is_owner()
	async def guilds(self, ctx):
		embed = discord.Embed(title=f"Сервера бота", description=f"Всего: {len(b.bot.guilds)}")
		for guild in b.bot.guilds:
			invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=10, temporary=False)
			embed.add_field(name=f"{guild.name}", value=f"ID: {guild.id}\nMembers: {guild.member_count}\nLink: ||https://discord.gg/{invite.code}||", inline=True)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Mod(bot))