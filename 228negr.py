import discord
from discord.ext import commands

from discord_components import DiscordComponents, Button, ButtonStyle

import random
import time
import json
import datetime
import sys
import colorama
import requests
import aiohttp
import asyncio
import sqlite3
from Cybernator import Paginator as pag
from asyncio import sleep
from discord.utils import get
from colorama import init
from colorama import Fore, Back, Style
from colorama import Fore

from pymongo import MongoClient
from colorama import Fore, Style, init
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
global prefix
prefix = "sv!"
token = "Токен сюда!"
bot = commands.Bot(command_prefix="sv!", intents=intents)
bot.remove_command( 'help' )
idea_channel = None
report_channel = None
review_channel = None

@bot.event
async def on_ready():
	print(f'svell bot was started')
	DiscordComponents(bot)
	await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="sv!help"))
	global idea_channel
	idea_channel = bot.get_channel(946392129863815248)
	
	global report_channel
	report_channel = bot.get_channel(978758368594382848)
	
	global review_channel
	review_channel = bot.get_channel(956127530216218664)
	
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		embed=discord.Embed(title=f"Команда не найдена!", color=0xFF0000)
		await ctx.send(embed=embed, delete_after=5)
	if isinstance(error, commands.MissingPermissions):
		embed=discord.Embed(title=f"У вас недостаточно прав для выполнения данной команды!", color=0xFF0000) 
		await ctx.send(embed=embed, delete_after=5)
	if isinstance(error, commands.MissingAnyRole):
		embed=discord.Embed(title=f"У вас нет специальной роли для использования этой команды!", color=0xFF0000) 
		await ctx.send(embed=embed, delete_after=5)
	if isinstance(error, commands.CommandOnCooldown):
		retry_after = str(datetime.timedelta(seconds=error.retry_after)).split('.')[0]
		embed=discord.Embed(title=f'**Команда уже была использована!Приходите через {retry_after}**', color=ctx.author.color)
		await ctx.send(embed=embed)
		
privet = ["https://cdn.discordapp.com/attachments/102817255661772800/219512763607678976/large_1.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219512898563735552/large.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219518948251664384/WgQWD.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219518717426532352/tumblr_lnttzfSUM41qgcvsy.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219519191290478592/tumblr_mf76erIF6s1qj96p1o1_500.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219519729604231168/giphy_3.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219519737971867649/63953d32c650703cded875ac601e765778ce90d0_hq.gif",
      "https://cdn.discordapp.com/attachments/102817255661772800/219519738781368321/17201a4342e901e5f1bc2a03ad487219c0434c22_hq.gif",
      "https://c.tenor.com/S6Kxbixp1yUAAAAC/gakkou-gurashi-hello.gif",
      "https://c.tenor.com/EERR4LXoJBoAAAAd/hi-wave.gif",
      "https://c.tenor.com/DDnp-TLMTWQAAAAC/hello-anime.gif",
      "https://c.tenor.com/-KgmJMneKM8AAAAC/hello-anime.gif",
      "https://c.tenor.com/jsIMbsjcZ4YAAAAC/kawaii-anime.gif",
      "https://c.tenor.com/qlT4AO1LID0AAAAC/anime-wave.gif",
      "https://c.tenor.com/S6V1PHV-PQUAAAAC/kuroha-shida-kuroha.gif",
      "https://c.tenor.com/mK8BUmcxq_YAAAAC/evil-iruma-kun-iruma-kun.gif",
      "https://c.tenor.com/OSnZnnqx4vsAAAAC/anime-hello.gif"
      "https://thumbs.gfycat.com/CourageousYellowDunlin-size_restricted.gif",
      "https://c.tenor.com/wZW05QUURk4AAAAC/welcome-anime.gif",
      "https://c.tenor.com/uig4MIIEykoAAAAC/welcome-anime.gif",
      "https://c.tenor.com/L9frOQ90sU8AAAAC/welcome-home-anime.gif",
      "https://c.tenor.com/a4bKFIyoT3IAAAAC/fun-anime-girl.gif",
      "https://c.tenor.com/AwMCvyYjPgAAAAAC/anime-welcome.gif",
      "https://c.tenor.com/-420uI8y-RkAAAAd/anime-welcome.gif",
      "https://c.tenor.com/HNcG3X-Og7wAAAAS/welcome-anime.gif",
      "https://c.tenor.com/6TkRi7pddF8AAAAC/anime-welcome.gif",
      "https://c.tenor.com/NWKnEDVFRJ4AAAAd/welcome-anime.gif",
      "https://c.tenor.com/F1Wghh3OxUEAAAAC/hello-hi.gif"]
		
		
		

@bot.event
async def on_member_join(member):
	channel = bot.get_channel(989978520556027984)
	embed = discord.Embed(title=f"Новый участник сервера!", description=f"Приветствуем тебя на нашем сервере **SVELL COMMUNITY** {member.mention}!\n Мы рады что ты зашел(ла) на наш сервер!\n Надеемся, что тебе тут понравится.Ознокомься с каналом <#935820227831275521>, там основные правила сервера, ну а тут (<#947591418199822356>), основной чат сервера.\n Ну ладно, надеемся что ты тут освоишься сам, желаем тебе удачи!", inline=False)
	embed.set_image(url = random.choice(privet))
	await channel.send(embed=embed)
	role = member.guild.get_role(935467923143790602)
	await member.add_roles(role)

@bot.command(pass_context=True)
async def ping(ctx):
	embed = discord.Embed(title=f" Пинг бота равен", description=f"{round(bot.latency * 1000)}ms :thumbsup: ")
	await ctx.send(embed=embed)
	
@bot.command(pass_context = True, aliases=['размут'])
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, *, member: discord.Member):
	channel = bot.get_channel(935828431038464000)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Muted')
	await member.remove_roles(mute_role)
	embed = discord.Embed(title=f'{member} был размучен <:like:977960101761662996> ')
	await channel.send(embed=embed)
	await ctx.message.delete()
	embed2=discord.Embed(title=f"Вы были размучены на сервере SVELL COMMUNITY")
	await member.send(embed=embed2)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, user: discord.Member, time: int, reason):
	channel = bot.get_channel(935828431038464000)
	embed=discord.Embed(title=f"Вы получили мут на сервере SVELL COMMUNITY по причине {reason} на {time} минут.")
	await user.send(embed=embed)
	role = user.guild.get_role(938090832794378260) # айди роли которую будет получать юзер
	embed = discord.Embed(title=f'{user} получил мут на {time} минут по причине: {reason} <:diz:938316834980126800>')
	await channel.send(embed=embed)
	await ctx.message.delete()
	await user.add_roles(role)
	await user.move_to(None)
	await asyncio.sleep(time * 60)
	await user.remove_roles(role)
	
@bot.command()
@commands.has_permissions(manage_roles=True)
async def ban(ctx, user: discord.Member, time: int, reason):
	channel = bot.get_channel(935828431038464000)
	embed=discord.Embed(title=f"Вы получили бан на сервере SVELL COMMUNITY по причине {reason} на {time} дней.")
	await user.send(embed=embed)
	role = user.guild.get_role(990400999581708368) # айди роли которую будет получать юзер
	embed = discord.Embed(title=f'{user} получил бан на {time} дней по причине: {reason} <:diz:938316834980126800>')
	await channel.send(embed=embed)
	await ctx.message.delete()
	await user.add_roles(role)
	await user.move_to(None)
	await asyncio.sleep(time * 86400)
	await user.remove_roles(role)
	
@bot.command(pass_context = True, aliases=['разбан'])
@commands.has_permissions(manage_roles=True)
async def unban(ctx, *, member: discord.Member):
	channel = bot.get_channel(935828431038464000)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = 'BAN')
	await member.remove_roles(mute_role)
	embed = discord.Embed(title=f'{member} был разбанен <:like:977960101761662996> ')
	await channel.send(embed=embed)
	await ctx.message.delete()
	embed2=discord.Embed(title=f"Вы были разбанены на сервере SVELL COMMUNITY")
	await member.send(embed=embed2)
  
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	channel = bot.get_channel(935828431038464000)
	if reason==None:
		reason="Причина не указана"
	await ctx.guild.kick(member)
	embed=discord.Embed(title=f'Участник {member} был кикнут с сервера по причине; {reason}')
	await channel.send(embed=embed)
	await ctx.message.delete()
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, *, nickname) :
	if member == "<@977952476189835264>" :
		await ctx.send("иди нахуй!")
	elif member == "<@310848622642069504>" :
		await ctx.send("иди нахуй!")
	else:
		embed=discord.Embed(title="Успешно! :white_check_mark:", description=f"**Ник пользователя {member.mention} был успешно изменен на `{nickname}`!**", color=0x33ff0a)
		embed.add_field(name="Модератор", value=f"{ctx.author} ( {ctx.author.mention} )", inline=False)
		await ctx.send(embed=embed)
		await member.edit(nick=nickname)
		await ctx.message.delete() 


@bot.command()
async def info(ctx,member:discord.Member = None, guild: discord.Guild = None):

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
	emb.add_field(name="Статус:", value=member.activity,inline=True)
	emb.add_field(name="Все роли пользователя:", value="/".join(role.mention for role in allroles),inline=False)
	emb.add_field(name="Дата присоединения:", value=member.joined_at.strftime("%d.%m.%Y %H:%M:%S"),inline=True)
	emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"),inline=True)
	emb.set_thumbnail(url=member.avatar_url)
	await ctx.send(embed = emb)

@bot.command(aliases=['si', 'serveri'])
@commands.guild_only()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str("SVELL COMMUNITY Крутой сервер для общения! Плюсы: 1. Красивое оформление сервера ; 2. Отзывчивая администрация ;3. Крутые эмодзи ;4. Уютный сервер, где вы можете пообщаться с кем-нибудь и найти друзей! ")

    owner = str("svell#8845")
    id = str("893755253739094066")
    region = str("Россия")
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Информация о сервере",
        description=description,
        color=discord.Color(0x00000)
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Создатель", value=owner, inline=True)
    embed.add_field(name="ID Сервера", value=id, inline=True)
    embed.add_field(name="Регион", value=region, inline=True)
    embed.add_field(name="Количество участников", value=memberCount, inline=True)

    await ctx.send(embed=embed)
        
@bot.command(aliases=['102', '112'])
async def police(ctx, *, reason):
    if reason is None:
        embed=discord.Embed(title=f"Укажите причину!", color=0xFF0000)
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title=f"{ctx.author} вызвал администрацию!", description=f"**Причина: `{reason}`**", color=0x0000FF)
        await ctx.send("<@&945686746115498004>", embed=embed)

@commands.cooldown(1, 30, commands.BucketType.user)		
@bot.command()
async def fakenitro(ctx, c: int = 1):
    for x in range(c):
        await ctx.send("https://discord.gift/{}".format(''.join([random.choice("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM") for _ in range(16)])))
        await ctx.send("https://discord.gift/{}".format(''.join([random.choice("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM") for _ in range(24)])))
        await msglog.edit(content=f'РљРѕРґС‹ РґР»СЏ РЅРёС‚СЂРѕ СЃРіРµРЅРµСЂРёСЂРѕРІР°Р»РёСЃСЊ.')
		
@bot.command(aliases=['Аватар'])
async def avatar(ctx, member: discord.Member  = None):
    if member == None:#если не упоминать участника тогда выводит аватар автора сообщения
        member = ctx.author
    embed = discord.Embed(color = 0x22ff00, title = f"Аватар участника - {member.name}", description = f"[Нажмите что бы скачать аватар]({member.avatar_url})")
    embed.set_image(url = member.avatar_url)
    await ctx.send(embed = embed)
	
HUG = ["https://c.tenor.com/Ct4bdr2ZGeAAAAAM/teria-wang-kishuku-gakkou-no-juliet.gif",
    "https://c.tenor.com/XyMvYx1xcJAAAAAC/super-excited.gif",
    "https://c.tenor.com/1T1B8HcWalQAAAAC/anime-hug.gif",
    "https://c.tenor.com/9e1aE_xBLCsAAAAC/anime-hug.gif"
	"https://c.tenor.com/kf36zSCz-D0AAAAM/anime-hug-hug.gif"]

@bot.command()
async def hug(ctx, member: discord.Member):

    embed = discord.Embed(title="объятия!", description="**{1}** обнял **{0}**!".format(member.name, ctx.message.author.name), color = discord.Color.purple())

    embed.set_image(url = random.choice(HUG))
    await ctx.send(embed=embed)
        
@bot.command(aliases=['идея'])
async def idea(ctx, *, idea=None):
     global idea_channel
     if idea is None:
        embed=discord.Embed(title=f"Укажите текст идеи!", color=0xFF0000)
        await ctx.send(embed=embed)
     else:
        embed = discord.Embed(title="💥 Новая идея!", description=f"**💡: {idea}**", color=0x0000FF)
        embed.set_footer(text=f'✉️ Отправил: {ctx.author}')
        msg = await idea_channel.send(embed=embed)
        await ctx.message.delete()
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
		
@bot.command(aliases=['жалоба'])
async def report(ctx, *, report=None):
     global report_channel
     if report is None:
        embed=discord.Embed(title=f"Укажите текст жалобы!", color=0xFF0000)
        await ctx.send(embed=embed)
     else:
        embed = discord.Embed(title="💥 Новая жалоба", description=f"**💡: {report}**", color=0x0000FF)
        embed.set_footer(text=f'✉️ Отправил: {ctx.author}')
        msg = await report_channel.send(embed=embed)
        await ctx.message.delete()
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
		
@bot.command(aliases=['отзыв'])
async def review(ctx, *, review=None):
     global review_channel
     if review is None:
        embed=discord.Embed(title=f"Укажите текст отзыва!", color=0xFF0000)
        await ctx.send(embed=embed)
     else:
        embed = discord.Embed(title="💥 Новый отзыв!", description=f"**💡: {review}**", color=0x0000FF)
        embed.set_footer(text=f'✉️ Отправил: {ctx.author}')
        msg = await review_channel.send(embed=embed)
        await ctx.message.delete()
		
@bot.command()
async def popit(ctx, popitt: int):
    text_map = ''
    for y in range(popitt):
        for x in range(popitt):
            text_map+= "||"+ random.choice(["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚪"]) +"|| "
        text_map+= "\n"
    
    popit = discord.Embed(title=f"Поиграй со мной ведь я попыыыыыыт", description=text_map, color=ctx.author.color)
    await ctx.send(embed = popit)
		
@bot.command(aliases=['очистить'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = None):
    if amount is None:
        await ctx.channel.purge(limit = amount)
        embed2 = discord.Embed(colour = 0xff9900, title = f'Удалены все сообщения')
        await ctx.send(embed=embed2, delete_after = 5)
    else:
        await ctx.channel.purge(limit = amount)
        embed = discord.Embed(colour = 0xff9900, title = f'Удалено {amount} сообщений')
        await ctx.send(embed = embed, delete_after = 5)

@bot.command(aliases=['сказать'])
async def say(ctx, *, content):
    await ctx.send(content)
    await ctx.message.delete() 
	
def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

@bot.command()
@commands.has_any_role(990006467694301185)
async def giveaway(ctx):
    await ctx.send("Начнем с этой раздачи! Ответьте на эти вопросы в течение 30 секунд!")

    questions = ["На каком канале он должен быть размещен?", "Какова должна быть продолжительность розыгрыша призов? (s|m|h|d)", "Какой приз в розыгрыше?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('Вы не ответили вовремя, пожалуйста, в следующий раз поторопитесь!')
            return
        else: 
            answers.append(msg.content)

    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"Вы неправильно упомянули канал. Делайте это так {ctx.channel.mention} в следующий раз.")
        return

    channel = bot.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"Вы не ответили правильным блоком. В следующий раз используйте (s|m|h|d)!")
        return
    elif time == -2:
        await ctx.send(f"Время должно быть целым числом. Пожалуйста, введите в следующий раз целое число.")
        return
 
    prize = answers[2]
    await ctx.send(f"Ивент будет через {channel.mention} и будет длиться {answers[1]} секунды!")
    embed = discord.Embed(title = "Ивент!", description = f"{prize}", color = ctx.author.color)
    embed.add_field(name = "Создал:", value = ctx.author.mention)
    embed.set_footer(text = f"Заканчивается {answers[1]} ")
    my_msg = await channel.send(embed = embed)
    await my_msg.add_reaction("🎉")
    await asyncio.sleep(time)
    new_msg = await channel.fetch_message(my_msg.id)
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Поздравляю! {winner.mention} выиграл приз: {prize}!")

@bot.command()
@commands.has_any_role(990006467694301185)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("Введенный идентификатор был неверным, убедитесь, что вы ввели правильный идентификатор сообщения с раздачей.")
        return   
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner = random.choice(users)

    await channel.send(f"Поздравляем нового победителя: {winner.mention} розыгрыша!")

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        msgErrorEmbed = discord.Embed(title="Ошибка!", description="Напишите текст!", colour=0xFF0000)
        await ctx.send(embed=msgErrorEmbed)
    else:
        raise(error)
		
@bot.command(aliases=['сообщение', 'msg', 'send'])
async def message(ctx, member: discord.Member, *, content):
	await member.send(f'**Вам пришло сообщение!**\n```bash\n{content}\n```\n**От:** `{ctx.author}`')
	await ctx.send(embed=discord.Embed(description="Успешно!", color=0x00FF00), delete_after = 5)
	await ctx.message.delete()
	
@message.error
async def message_error(ctx, error):
	if isinstance(error, commands.MemberNotFound):
		mesageerrorEmbed=discord.Embed(title="Ошибка!", description="Пользователь не найден!", colour=0xFF0000)
		await ctx.send(embed=mesageerrorEmbed)
	elif isinstance(error, commands.MissingRequiredArgument):
		messagetextErrorEmbed = discord.Embed(title="Ошибка!", description="Напишите текст!", colour=0xFF0000)
		await ctx.send(embed=messagetextErrorEmbed)
	else:
		raise(error)
		
@bot.command()
async def warn(ctx, member: discord.Member, *, about: str):
		channel = bot.get_channel(935828431038464000)
		if member:
			embed = discord.Embed(color = ctx.author.color, description = f'Участник **{member.mention}** получил предупреждение от **{ctx.message.author.name}** по причине:\n**```\n{about}\n```**')
			await channel.send(embed = embed)
			await ctx.message.delete()
		else:
			embed = discord.Embed(color = ctx.author.color, description = 'Ошибка в аргументах команды\nили участник не найден.', title = 'Ошибка')
			await ctx.send(embed = embed)
		
@bot.command(aliases=['помощь'])
async def help(ctx, arg=''):
	if arg == 'adm':
		embed = discord.Embed(
			title = 'Административные команды',
			description = f'`{prefix}mute <упом, время, причина>` - замутить участника сервера\n`{prefix}unmute <упом> ` - размутить участника сервера\n`{prefix}ban <упом, время, причина>` - забанить участника сервера\n`{prefix}unban <упом>` - Разбанить участника сервера \n`{prefix}warn <упом, причина> ` - Выдать предупреждение участнику\n`{prefix}clear <кол-во>` - очистить определённое количество сообщиний\n`{prefix}kick <упом, причина> ` - кикнуть участника сервера\n`{prefix}giveaway ` - Создать ивент\n`{prefix}nick <упом, текст> ` - Изменить никнейм участнику сервера',
			colour = discord.Colour.from_rgb(237, 47, 47)
		)

		await ctx.send(embed=embed)
		return
	elif arg == 'fun':
		embed = discord.Embed(
			title = 'Развлекательные команды',
			description = f'`{prefix}say <текст>` - Написать сообщиние от имени бота\n`{prefix}fakenitro` - Фейк нитро\n`{prefix}msg <упом, текст>` - Написать сообщиние от имени бота в ЛС\n`{prefix}hug <упом>` - Обнять пользователя\n`{prefix}popit <число от 1 до 26>` - Поиграть в Поп Ит ',
			colour = discord.Colour.from_rgb(237, 47, 47)
		)

		await ctx.send(embed=embed)
		return
	elif arg == 'profile':
		embed = discord.Embed(
            title = 'Профильные команды',
            description = f'`{prefix}avatar <упом>` - Посмотреть аватар пользователя\n`{prefix}useri` - Посмотреть информацию о участнике - ',
            colour = discord.Colour.from_rgb(237, 47, 47)
		)

		await ctx.send(embed=embed)
		return
		
	elif arg == 'server':
		embed = discord.Embed(
			title = 'Серверные команды',
			description = f'`{prefix}serverinfo` - Посмотреть информацию о сервере\n`{prefix}112 <текст>` Вызвать администрацию\n`{prefix}idea <текст>` Написать свою идею в канал <#946392129863815248>\n`{prefix}report <текст>` Написать далобу на Участника/Администрацию в канал <#978758368594382848>\n`{prefix}review <текст>` Написать отзыв о покупке в канал <#956127530216218664>\n`{prefix}ping` - Узнать пинг бота',
			colour = discord.Colour.from_rgb(237, 47, 47)
		)

		await ctx.send(embed=embed)
		return



	embed = discord.Embed(
		title = 'Список команд',
		description = f'`{prefix}help adm` - помощь по разделу "Административные команды"\n`{prefix}help fun` - помощь по разделу "Развлекательные команды"\n`{prefix}help profile` - помощь по разделу "Профильные команды"\n`{prefix}help server` - помощь по разделу "Серверные команды"\n',
		colour = discord.Colour.from_rgb(237, 47, 47)
	)

	await ctx.send(embed=embed)
    
bot.run(token)