import discord
import os
import traceback
from discord.ext import commands
import asyncio
import datetime
import youtube_dl
from discord_components import DiscordComponents, Button, ButtonStyle

TOKEN = "OTg0NzkyNzk3NjQ5NDY1Mzk0.G-WR2y.-8-VZT8Bs6dWKn5FJlFEhW5K6W2GzmV5_ZXkTQ"
PREFIX = "w."
intents = discord.Intents.all()
bot = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)

class evetns(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(ctx):
		print("evetns cog on")
		DiscordComponents(bot)


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
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
			await ctx.send(embed = discord.Embed(title=f"Error!", description = f'** {ctx.author.name}, у вас нет прав на использование данной команды.**', color=0x0c0c0c))
		'''print("бнаружена ошибка в команде бота")'''
		

	@commands.command()
	async def test(self, ctx):
		msg = await ctx.send(
			embed = discord.Embed(title = 'Вы точно хотите перевевсти деньги?', timestamp = ctx.message.created_at),
			components = [
			Button(style = ButtonStyle.green, label = 'Да'),
			Button(style = ButtonStyle.red, label = 'Нет')
			])
		responce = await bot.wait_for('button_click', check = lambda message: message.author == ctx.author)
		if responce.component.label == 'Да':
			await responce.respond(content = 'Деньги успешно переведены!')
		else:
			await responce.respond(content = 'Вы отменили перевод.')


def setup(bot):
	bot.add_cog(evetns(bot))