import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix = "%")

@Bot.event
async def on_ready():
	print("ready")

@Bot.event
async def on_reaction_add(reaction, user):
	print(reaction, user)
	if(reaction.message.author.name == "1n6ty"):
		print("1n6ty\n")
		if(str(reaction) == "🧠"):
			print("brain")
			roleAdd = discord.utils.get(user.guild.roles, name = "Cyber")
			print("role")
			await user.add_roles(roleAdd)

		if(str(reaction) == "🤺"):
			print("run")
			roleAdd = discord.utils.get(user.guild.roles, name = "Sports")
			print("role")
			await user.add_roles(roleAdd)

		if(str(reaction) == "😋"):
			print("run")
			roleAdd = discord.utils.get(user.guild.roles, name = "Stream")
			print("role")
			await user.add_roles(roleAdd)

@Bot.event
async def on_reaction_remove(reaction, user):
	print(reaction, user)
	if(reaction.message.author.name == "1n6ty"):
		print("1n6ty\n")
		if(str(reaction) == "🧠"):
			print("brain")
			roleRem = discord.utils.get(user.guild.roles, name = "Cyber")
			print("role")
			await user.remove_roles(roleRem)

		if(str(reaction) == "🤺"):
			print("run")
			roleAdd = discord.utils.get(user.guild.roles, name = "Sports")
			print("role")
			await user.remove_roles(roleAdd)

		if(str(reaction) == "😋"):
			print("run")
			roleAdd = discord.utils.get(user.guild.roles, name = "Stream")
			print("role")
			await user.remove_roles(roleAdd)

Bot.run(open('Config.txt', 'r').readline())