#made by glorious bitran, please do not copypaterino

import discord
from discord import Game
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from weather import Weather, Unit
import asyncio
import chalk
import os
import random
import json
	
bot = commands.Bot(command_prefix="!")
emb = discord.Embed()
weatherw = Weather(unit=Unit.CELSIUS)
lookupw = weatherw.lookup(796597)
conditionw = lookupw.condition
startup_extensions = ["Music"]

class Main_Commands():
	def __init__(self, bot):
	 self.bot = bot

#bitran's glorious Autism Points system

def user_add_xp(user_id: int, xp: int):
	if os.path.isfile("users.json"):
		try:
			with open("users.json", "r") as fp:
				users = json.load(fp)
			users[user_id]["xp"] += xp
			with open("users.json", "w") as fp:
				json.dump(users, fp, sort_keys=True, indent=4)
		except KeyError:
			with open("users.json", "r") as fp:
				users = json.load(fp)
			users[user_id] = {}
			users[user_id]["xp"] = xp
			with open("users.json", "w") as fp:
				json.dump(users, fp, sort_keys=True, indent=4)
	else:
		users = {user_id: {}}
		users[user_id]["xp"] = xp
		with open("users.json", "w") as fp:
			json.dump(users, fp, sort_keys=True, indent=4)
			
def get_xp(user_id: int):
	if os.path.isfile("users.json"):
		with open("users.json", "r") as fp:
			users = json.load(fp)
			return users[user_id]["xp"]
	else:
		return 0
			
#Events

@bot.event
async def on_ready():
	await bot.change_presence(game=Game(name="with Western Spy"))
	print ("BLIN THIS BOT WORKS!")
	print ("OPA BOT NAME: " + bot.user.name)
	print ("OPA BOT ID: " + bot.user.id)
	print ("BLIN DIRECTORY IS: " + os.getcwd())
	print ("--------------------------------------")
	print ("bot made by: bitran")
	
@bot.event
async def on_message(message):
	await bot.process_commands(message)
	if "anime" in message.content.lower():
		await bot.send_message(message.channel, "WEEB ALERT! " + message.author.mention + " is a fucking weeb! and got autism points!")
		user_add_xp(message.author.id, 3)

#Commands

@bot.command(pass_context=True)
async def bottest(ctx):
	await bot.say("i fucking work blin")
	
@bot.command(pass_context=True)
async def hug(ctx, target: discord.Member):
	await bot.send_file(ctx.message.channel, "d99.png", content="{} is a faggot with {}".format(ctx.message.author.mention, target.mention))
	
@bot.command(pass_context=True)
async def meme(ctx):
	memes = ["m1.png", "m2.png", "m3.jpg", "m4.png", "m5.png", "m6.png", "m7.png", "m8.png", "m9.png", "m10.jpg", "m13.jpg", "m11.png", "m12.png"]
	await bot.send_file(ctx.message.channel, random.choice(memes), content="here you go blin")
	
@bot.command(pass_context=True)
async def advice(ctx):
	advice = ["Never leave a gopnik near vodka alone, you may find your bottle empty.", "If you're sick, ask babushka to make you chicken polevka.", "Homemade Kvass is the Best Kvass."]
	await bot.say(random.choice(advice))
	
@bot.command(pass_context=True)
async def kiss(ctx, target: discord.Member):
	await bot.send_file(ctx.message.channel, "stop.jpg", content="{} and {} no assaulting each other this is not a weeb fucking server".format(ctx.message.author.mention, target.mention))

@bot.command(pass_context=True)
async def isvilemafaggot(ctx):
	await bot.say("yes blin he is")
	
@bot.command(pass_context=True)
async def weather(ctx, misto):
	weather = Weather(unit=Unit.CELSIUS)
	location = weather.lookup_by_location(misto)
	condition = location.condition
	await bot.say("its currently: " + condition.text)
	await bot.say("and the tempature is: " + condition.temp + "°C")
	await bot.say("this is in: " + misto + ", blin")
	
@bot.command(pass_context = True)
async def info(ctx):
    user_xp = get_xp(ctx.message.author.id)
    await bot.say("ur full name blin: *{}*".format(ctx.message.author))
    await bot.say("ur ID: *{}*".format(ctx.message.author.id))
    await bot.say("ur best role: *{}*".format(ctx.message.author.top_role))
    await bot.say("ur join date blin: *{}*".format(ctx.message.author.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")))
    await bot.say("you have **{}** autism points!".format(user_xp))
	
@bot.command(pass_context = True)
async def targetinfo(ctx, target: discord.Member):
    target_xp = get_xp(target.id)
    await bot.say("their full name blin: *{}*".format(target))
    await bot.say("their ID: *{}*".format(target.id))
    await bot.say("their best role: *{}*".format(target.top_role))
    await bot.say("their join date blin: *{}*".format(target.joined_at.strftime("%A, %B %d %Y @ %H:%M:%S %p")))
    await bot.say("they have **{}** autism points!".format(target_xp))

#Autism Points Commands

@bot.command(pass_context=True)
async def what_are_autism_points(ctx):
	target_xp = get_xp(ctx.message.author.id)
	await bot.say("Autism points are a currency used to determine how autistic a person is. You can check your autism points with !points, !give or !take points from others, and award people points with !autist (name). You have **{}** autism points.".format(target_xp))
	
@bot.command(pass_context=True)
async def amiretarded(ctx):
	await bot.say("you have earned an autism point, {}".format(ctx.message.author.mention))
	user_add_xp(ctx.message.author.id, 1)

@bot.command(pass_context=True)
async def give(ctx, target: discord.Member):
	target_xp = get_xp(ctx.message.author.id)
	
	if target_xp > 10:
		await bot.say("{} gave a ton of their shitty points to {} ".format(ctx.message.author.mention, target.mention))
		user_add_xp(ctx.message.author.id, -4)
		user_add_xp(target.id, 4)
	else:
		await bot.say("{} gave an autism point to {} ".format(ctx.message.author.mention, target.mention))
		user_add_xp(ctx.message.author.id, -1)
		user_add_xp(target.id, 1)	

@bot.command(pass_context=True)
async def take(ctx, target: discord.Member):
	target_xp = get_xp(target.id)
	
	if target_xp > 10:
		await bot.say("{} took a lot of autism points from {} ".format(ctx.message.author.mention, target.mention))
		user_add_xp(ctx.message.author.id, 4)
		user_add_xp(target.id, -4)
	else:
		await bot.say("{} took an autism point from {} ".format(ctx.message.author.mention, target.mention))
		user_add_xp(ctx.message.author.id, 1)
		user_add_xp(target.id, -1)	

@bot.command(pass_context=True)
async def points(ctx):
	user_xp = get_xp(ctx.message.author.id)
	await bot.say("{}, you have {} autism points.".format(ctx.message.author.mention, user_xp))
	
@bot.command(pass_context=True)
async def targetpoints(ctx, target: discord.Member):
    target_xp = get_xp(target.id)
    await bot.say("{} has {} autism points.".format(target.mention, target_xp))

@bot.command(pass_context=True)
async def autist(ctx, target: discord.Member):
	if target == ctx.message.author:
		await bot.say("you cannot declare yourself autistic, use !amiretarded instead blin!")
	else:
		await bot.say("{} declared {} an autist, awarding them 3 autism points.".format(ctx.message.author.mention, target.mention))
		user_add_xp(target.id, 3)
		
@bot.command(pass_context=True)
async def omegaautist(ctx, target: discord.Member):
	if target == ctx.message.author:
		await bot.say("{} declared themselves an omegaautist, awarding them 10 JUSTIFIED autism points.".format(ctx.message.author.mention, target.mention))
		user_add_xp(target.id, 10)
	else:
		await bot.say("only you can declare yourself to be the apex autist, because your mom.")
		
@bot.command(pass_context=True)
async def save_server(ctx):
	await bot.say("Saving everyone on this discord server, this is required for commands like !info to work!")
	await bot.say("**THIS COMMAND SHOULD BE RUN ONLY ONCE OR WHEN NEW PEOPLE JOIN THE SERVER AND DONT HAVE POINTS YET!**")
	for server_member in ctx.message.server.members:
		user_add_xp(server_member.id, 0)
		await bot.say("{} was given 0 autism points.".format(server_member))

#Bullshit

if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			exc = "{}: {}".format(type(e).__name__, e)
			print("blin extensions fucked {}\n{}".format(extension, exc))
			

bot.run(os.getenv("TOKEN"))
