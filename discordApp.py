import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = "%")

@Bot.event
async def on_ready():
	print("ready")

@Bot.event
async def on_raw_reaction_add(react):
	print(react)
	if(react.channel_id == 682247064620630129):
		print("1n6ty\n")
		if(str(react.emoji) == "🧠"):
			print("brain")
			roleAdd = discord.utils.get(react.member.guild.roles, name = "Cyber")
			print("role")
			await react.member.add_roles(roleAdd)

		if(str(react.emoji) == "🤺"):
			print("run")
			roleAdd = discord.utils.get(react.member.guild.roles, name = "Sports")
			print("role")
			await react.member.add_roles(roleAdd)

		if(str(react.emoji) == "😋"):
			print("run")
			roleAdd = discord.utils.get(react.member.guild.roles, name = "Stream")
			print("role")
			await react.member.add_roles(roleAdd)

import discord

from discord.ext import commands
from discord.ext.commands import Bot

import os

Bot = commands.Bot(command_prefix = "%")

@Bot.event
async def on_ready():
	print("readyy")

@Bot.event
async def on_raw_reaction_add(react):
	print(react)
	if(react.channel_id == 682247064620630129):
		print("1n6ty\n")
		if(str(react.emoji) == "🧠"):
			print("brain")
			roleAdd = discord.utils.get(react.member.guild.roles, name = "Cyber")
			print("role")
			await react.member.add_roles(roleAdd)

		if(str(react.emoji) == "🤺"):
			print("run")
			roleAdd = discord.utils.get(react.member.guild.roles, name = "Sports")
			print("role")
			await react.member.add_roles(roleAdd)

		if(str(react.emoji) == "😋"):
			print("run")
			roleAdd = discord.utils.get(react.member.guild.roles, name = "Stream")
			print("role")
			await react.member.add_roles(roleAdd)

@Bot.event
async def on_raw_reaction_remove(react):
	print(react)
	guild = Bot.get_guild(react.guild_id)
	channel = discord.utils.get(guild.channels, name = "promise")
	print("1n6ty\n")
	if(str(react.emoji) == "🧠"):
		print("brain")
		roleAdd = discord.utils.get(guild.roles, name = "Cyber")
		print("role")
		await discord.utils.get(guild.members, id = react.user_id).remove_roles(roleAdd)

	if(str(react.emoji) == "🤺"):
		print("run")
		roleAdd = discord.utils.get(guild.roles, name = "Sports")
		print("role")
		await discord.utils.get(guild.members, id = react.user_id).remove_roles(roleAdd)

	if(str(react.emoji) == "😋"):
		print("run")
		roleAdd = discord.utils.get(guild.roles, name = "Stream")
		print("role")
		await discord.utils.get(guild.members, id = react.user_id).remove_roles(roleAdd)

Bot.run("NjgxOTE3NzE5OTgxMDY0Mjg3.Xlav4g.IP7pRAIGVHiyKd2WwwDbphOjNLc")
token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
