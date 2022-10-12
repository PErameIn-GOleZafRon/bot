
	'''@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def meme(self, ctx):
		embed = discord.Embed(title="", description="", color=ctx.author.color)
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/memes/hot.json') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				await ctx.send(embed=embed)'''

	'''@commands.command()
	#@commands.cooldown(1, 5, commands.BucketType.guild)
	async def owl(self, ctx):
		embed = discord.Embed(title="", description="", color=ctx.author.color)
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/Owls/new.json') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				await ctx.send(embed=embed)'''


	'''@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def catowl(self, ctx):
		embed = discord.Embed(title="", description="", color=ctx.author.color)
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://www.reddit.com/r/OwlsWithCatHeads/new.json') as r:
				res = await r.json()
				embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
				await ctx.send(embed=embed)'''











	'''@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help_mod(self, ctx):
		embed = discord.Embed(title="Модерация", description="", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wweh888ARLaWUUm_wRXFMiYNqdBl3Vxhn3NVrQd9pHk/%3Fsize%3D1024/https/cdn.discordapp.com/icons/937331927743094794/e0793a07166e181c8457da251f3a7e1c.png")
		embed.add_field(name=f"{bot.PREFIX}ping", value="Показ задержки бота", inline=True)
		embed.add_field(name=f"{bot.PREFIX}clear", value=f"Синтаксис: {bot.PREFIX}clear (количество сообщений). Удаляет определенное количество сообщений в канале!", inline=False)
		embed.add_field(name=f"{bot.PREFIX}mute", value=f"Синтаксис: {bot.PREFIX}mute (участник) (время) (буква времянного промяжутка (s, m, h, d)) (причина). Временный мут участника!", inline=False)
		embed.add_field(name=f"{bot.PREFIX}infinitymute", value=f"Синтаксис: {bot.PREFIX}infinitymute (участник) (причина). Перманентный мут участника!", inline=False)
		embed.add_field(name=f"{bot.PREFIX}unmute", value=f"Синтаксис: {bot.PREFIX}unmute (участник). Снятие мута с участника!", inline=False)
		embed.add_field(name=f"{bot.PREFIX}kick", value=f"Синтаксис: {bot.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		embed.add_field(name=f"{bot.PREFIX}ban", value=f"Синтаксис: {bot.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		embed.add_field(name=f"{bot.PREFIX}unban", value=f"Синтаксис: {bot.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help_fan(self, ctx):
		embed = discord.Embed(title="Фан", description="", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wweh888ARLaWUUm_wRXFMiYNqdBl3Vxhn3NVrQd9pHk/%3Fsize%3D1024/https/cdn.discordapp.com/icons/937331927743094794/e0793a07166e181c8457da251f3a7e1c.png")
		embed.add_field(name=f"{bot.PREFIX}owl", value="Случайное фото совы", inline=False)
		embed.add_field(name=f"{bot.PREFIX}catowl", value="Случайное фото совы с головой кота", inline=False)
		embed.add_field(name=f"{bot.PREFIX}meme", value="Отправляет случайный мем", inline=False)
		embed.add_field(name=f"{bot.PREFIX}avatar", value=f"Синтаксис: {bot.PREFIX}avatar (участник). Отправляет аватар участника!", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}unmute", value=f"Синтаксис: {bot.PREFIX}unmute (участник). Снятие мута с участника!", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}kick", value=f"Синтаксис: {bot.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}ban", value=f"Синтаксис: {bot.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		#mbed.add_field(name=f"{bot.PREFIX}unban", value=f"Синтаксис: {bot.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help(self, ctx):
		embed = discord.Embed(title="Помощь", description="", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wweh888ARLaWUUm_wRXFMiYNqdBl3Vxhn3NVrQd9pHk/%3Fsize%3D1024/https/cdn.discordapp.com/icons/937331927743094794/e0793a07166e181c8457da251f3a7e1c.png")
		embed.add_field(name="Модерация ({bot.PREFIX}help_mod)", value="{bot.PREFIX}ping, {bot.PREFIX}clear, {bot.PREFIX}mute, {bot.PREFIX}infinitymute, {bot.PREFIX}unmute, {bot.PREFIX}kick, {bot.PREFIX}ban, w.unban", inline=False)
		embed.add_field(name="Фан (w.help_fan)", value="w.owl, w.catowl, w.meme", inline=False)
		embed.add_field(name="Ролеплей (w.help_rp)", value="w.kiss, w.kill, w.feed, w.cry, w.bite", inline=False)
		embed.add_field(name="Остальное (w.help_other)", value="w.info", inline=False)
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help_rp(self, ctx):
		embed = discord.Embed(title="Ролеплей", description="", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wweh888ARLaWUUm_wRXFMiYNqdBl3Vxhn3NVrQd9pHk/%3Fsize%3D1024/https/cdn.discordapp.com/icons/937331927743094794/e0793a07166e181c8457da251f3a7e1c.png")
		embed.add_field(name=f"{bot.PREFIX}kiss", value=f"Синтаксис: {bot.PREFIX}kiss (участник). Поцеловать участника", inline=False)
		embed.add_field(name=f"{bot.PREFIX}kill", value=f"Синтаксис: {bot.PREFIX}kill (участник). Убить участника", inline=False)
		embed.add_field(name=f"{bot.PREFIX}feed", value=f"Синтаксис: {bot.PREFIX}feed (участник). Покормить участника", inline=False)
		embed.add_field(name=f"{bot.PREFIX}cry", value=f"Начать плакать", inline=False)
		embed.add_field(name=f"{bot.PREFIX}bite", value=f"Синтаксис: {bot.PREFIX}bite (участник). Укусить участника", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}kick", value=f"Синтаксис: {bot.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}ban", value=f"Синтаксис: {bot.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		#mbed.add_field(name=f"{bot.PREFIX}unban", value=f"Синтаксис: {bot.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		await ctx.reply(embed=embed)

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help_other(self, ctx):
		embed = discord.Embed(title="Остальное", description="", timestamp=datetime.datetime.utcnow(), colour=discord.Colour.red())
		embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/wweh888ARLaWUUm_wRXFMiYNqdBl3Vxhn3NVrQd9pHk/%3Fsize%3D1024/https/cdn.discordapp.com/icons/937331927743094794/e0793a07166e181c8457da251f3a7e1c.png")
		embed.add_field(name=f"{bot.PREFIX}info", value=f"Синтаксис: {bot.PREFIX}info (участник). Просмотр информации об участнике", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}kill", value=f"Синтаксис: {bot.PREFIX}kill (участник). Убить участника", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}feed", value=f"Синтаксис: {bot.PREFIX}feed (участник). Покормить участника", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}cry", value=f"Начать плакать", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}bite", value=f"Синтаксис: {bot.PREFIX}bite (участник). Укусить участника", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}kick", value=f"Синтаксис: {bot.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
		#embed.add_field(name=f"{bot.PREFIX}ban", value=f"Синтаксис: {bot.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
		#mbed.add_field(name=f"{bot.PREFIX}unban", value=f"Синтаксис: {bot.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
		await ctx.reply(embed=embed)'''


'''@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def help(self, ctx, Chapter = None):

		if Chapter == None:
			Chapter = "all"

		if Chapter == "all":
			embed = discord.Embed(title=f"Помощь", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
			embed.add_field(name=f":shield: Модерация >>> {b.PREFIX}help Модерация", value=f"`{b.PREFIX}ping`, `{b.PREFIX}clear`, `{b.PREFIX}mute`, `{b.PREFIX}infinitymute`, `{b.PREFIX}unmute`, `{b.PREFIX}kick`, `{b.PREFIX}ban`, `{b.PREFIX}unban`", inline=False)
			embed.add_field(name=f":diamond_shape_with_a_dot_inside: Фан >>> w.help Фан", value=f"`{b.PREFIX}owl`, `{b.PREFIX}catowl`, `{b.PREFIX}meme`", inline=False)
			embed.add_field(name=f":infinity: Ролеплей >>> {b.PREFIX}help Ролеплей", value=f"`{b.PREFIX}kiss`, `{b.PREFIX}kill`, `{b.PREFIX}feed`, `{b.PREFIX}cry`, `{b.PREFIX}bite`", inline=False)
			embed.add_field(name=f":beginner: Остальное >>> {b.PREFIX}help Остальное", value=f"`{b.PREFIX}info`, `{b.PREFIX}help`, `{b.PREFIX}report`, `{b.PREFIX}bug`", inline=False)
			embed.add_field(name=f":ghost: Глобальный чат >>> {b.PREFIX}help Глобал", value=f"`Для информации пропишите команду помощи по глобальному чату`", inline=False)
			embed.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")
			await ctx.reply(embed=embed)

		elif Chapter == "Модерация":
			embed = discord.Embed(title=f":shield: Модерация >>> {b.PREFIX}help Модерация", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
			embed.add_field(name=f"{b.PREFIX}ping", value="Показ задержки бота", inline=True)
			embed.add_field(name=f"{b.PREFIX}clear", value=f"Синтаксис: {b.PREFIX}clear (количество сообщений). Удаляет определенное количество сообщений в канале!", inline=False)
			embed.add_field(name=f"{b.PREFIX}mute", value=f"Синтаксис: {b.PREFIX}mute (участник) (время) (буква времянного промяжутка (s, m, h, d)) (причина). Временный мут участника!", inline=False)
			embed.add_field(name=f"{b.PREFIX}infinitymute", value=f"Синтаксис: {b.PREFIX}infinitymute (участник) (причина). Перманентный мут участника!", inline=False)
			embed.add_field(name=f"{b.PREFIX}unmute", value=f"Синтаксис: {b.PREFIX}unmute (участник). Снятие мута с участника!", inline=False)
			embed.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
			embed.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
			embed.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
			embed.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")
			await ctx.reply(embed=embed)

		elif Chapter == "Фан":
			embed = discord.Embed(title=f":diamond_shape_with_a_dot_inside: Фан >>> {b.PREFIX}help Фан", description="", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
			embed.add_field(name=f"{b.PREFIX}owl", value="Случайное фото совы", inline=False)
			embed.add_field(name=f"{b.PREFIX}catowl", value="Случайное фото совы с головой кота", inline=False)
			embed.add_field(name=f"{b.PREFIX}meme", value="Отправляет случайный мем", inline=False)
			#embed.add_field(name=f"{b.PREFIX}unmute", value=f"Синтаксис: {b.PREFIX}unmute (участник). Снятие мута с участника!", inline=False)
			#embed.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
			#embed.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
			#mbed.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
			embed.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")
			await ctx.reply(embed=embed)

		elif Chapter == "Ролеплей":
			embed = discord.Embed(title=f":infinity: Ролеплей >>> {b.PREFIX}help Ролеплей", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
			embed.add_field(name=f"{b.PREFIX}kiss", value=f"Синтаксис: {b.PREFIX}kiss (участник). Поцеловать участника", inline=False)
			embed.add_field(name=f"{b.PREFIX}kill", value=f"Синтаксис: {b.PREFIX}kill (участник). Убить участника", inline=False)
			embed.add_field(name=f"{b.PREFIX}feed", value=f"Синтаксис: {b.PREFIX}feed (участник). Покормить участника", inline=False)
			embed.add_field(name=f"{b.PREFIX}cry", value=f"Начать плакать", inline=False)
			embed.add_field(name=f"{b.PREFIX}bite", value=f"Синтаксис: {b.PREFIX}bite (участник). Укусить участника", inline=False)
			#embed.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
			#embed.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
			#mbed.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
			embed.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")
			await ctx.reply(embed=embed)

		elif Chapter == "Остальное":
			embed = discord.Embed(title=f":beginner: Остальное >>> {b.PREFIX}help Остальное", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
			embed.add_field(name=f"{b.PREFIX}info", value=f"Синтаксис: {b.PREFIX}info (участник). Просмотр информации об участнике", inline=False)
			embed.add_field(name=f"{b.PREFIX}help", value=f"Показ меню помощи по командам", inline=False)
			embed.add_field(name=f"{b.PREFIX}serverinfo", value=f"Посмотреть информацию о сервере", inline=False)
			embed.add_field(name=f"{b.PREFIX}avatar", value=f"Синтаксис: {b.PREFIX}avatar (участник). Отправляет аватар участника", inline=False)
			embed.add_field(name=f"{b.PREFIX}report", value=f"Синтаксис: {b.PREFIX}report (текст жалобы с id, именем пользователя и самой жалобой). Написание жалобы на участника", inline=False)
			embed.add_field(name=f"{b.PREFIX}bug", value=f"Синтаксис: {b.PREFIX}bug (подробное описание ошибки бота). Нашли ошибку в боте? Помогите нам исправить её, сообщив о её существовании", inline=False)
			#embed.add_field(name=f"{b.PREFIX}bite", value=f"Синтаксис: {b.PREFIX}bite (участник). Укусить участника", inline=False)
			#embed.add_field(name=f"{b.PREFIX}kick", value=f"Синтаксис: {b.PREFIX}kick (участник) (причина). Выгнать участника с сервера!)", inline=False)
			#embed.add_field(name=f"{b.PREFIX}ban", value=f"Синтаксис: {b.PREFIX}ban (участник) (причина). Перманентный бан участника!", inline=False)
			#mbed.add_field(name=f"{b.PREFIX}unban", value=f"Синтаксис: {b.PREFIX}unban (участник). Снятие бана у участника!", inline=False)
			embed.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")
			await ctx.reply(embed=embed)

		elif Chapter == "Глобал":
			embed = discord.Embed(title=f":ghost: Глобальный чат >>> {b.PREFIX}help Глобал", description=f"", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/984792797649465394/51d935be541e8937d2d662f2cfa947bc.webp?size=1024")
			embed.add_field(name=f"Описание", value=f"Глобальный чат позволяет общаться с людьми с других серверов, где есть канал глобального чата и присутствует данный бот", inline=False)
			embed.add_field(name=f"Использование", value=f"Для включения данной функции вам требуется создать канал с названием '`global-chat`'\nПосле создания канала можно начанать общаться, просто отправляя туда обычные сообщения", inline=False)
			embed.add_field(name=f"Правила общения в глобальном чате", value=f"**1. Не рекламировать сервера!**\n**2. Не отправлять скам-ссылки, или ссылки которые нарушают правила Discord!**\n**3. Не флудить/спамить!**\n**4. Не кидать NSFW (Not Save For Work (18+)) изображения!**\n**5. Не отправлять в данный чат никаких команд!**", inline=False)
			embed.add_field(name=f"Примечания", value=f"Менять название канала нельзя, в противном случае чат перестанет работать\nЗа нарушение правил глобального чата вам может быть выдан бан глобального чата\nЕсли вы заметили нарушение правил глобального чата, напишите `{b.PREFIX}report` с описанием нарушения, id и полным ником с тегом пользователя, совершивсего нарушение", inline=False)
			embed.set_author(name=f"Запросил: {ctx.author} ", icon_url=f"{ctx.author.avatar_url}")
			await ctx.reply(embed=embed)



		else:
			embed = discord.Embed(title="Error", description="Извините, но данной категории помощи не существует!", timestamp=datetime.datetime.utcnow(), color=ctx.author.color)
			await ctx.reply(embed=embed)'''



'''@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, данной команды не существует.**', color=0x0c0c0c))

    if isinstance(error, commands.BotMissingPermissions ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, мне не хватает прав, для выполнения этой комнды, обратитесь к техническому администратору.**', color=0x0c0c0c))

    if isinstance(error, commands.DisabledCommand ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, данная команда отключена.**', color=0x0c0c0c))

    if isinstance(error, commands.CommandOnCooldown ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, полегче, не так быстро.**', color=0x0c0c0c))

    if isinstance(error, commands.UserInputError ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, ошибка ввода доп, данных команды\nПроверьте правильность ввода данных и попробуйте снова.**', color=0x0c0c0c))

    if isinstance(error, commands.NoPrivateMessage ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, данная команда не может быть использована в лс.**', color=0x0c0c0c))

    if isinstance(error, commands.CheckFailure ):
        await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, у вас нет прав на использование данной команды.**', color=0x0c0c0c))'''


'''bot = interactions.Client(token=TOKEN)'''


'''@bot.command(aliases=['8ball'])
async def ball(ctx, *, message) :

    ball = ['Да',
        'Возможно да',
        'Нет',
        'Возможно нет']
        
    embed = discord.Embed(title="Вопрос!", description=f"**💡: {message}**\nЗадал {ctx.author}\nОтвет на этот вопрос: {random.choice(ball)}", color=ctx.author.color)
    await ctx.send(embed=embed)'''


'''@bot.command()
async def vv(ctx):
    await ctx.message.delete()
    await ctx.send(
        embed = discord.Embed(title=f"Верефикация", description=f"Для верефикации нажмите на кнопку!", timestamp=datetime.datetime.utcnow() ,color=ctx.author.color),
        components = [
            Button(label = "verifications", custom_id = "verifications", style=ButtonStyle.green)
        ]
    )'''

'''@commands.command()
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
	    await ctx.reply(embed=embed)'''