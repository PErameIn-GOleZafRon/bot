from http import client
import discord
from discord.ext import commands
import json
import os


class Exp(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(ctx):
		print("exp cog on")

	'''@commands.Cog.listener()
	async def on_message(self, message):
		break'''

def setup(bot):
	bot.add_cog(Exp(bot))