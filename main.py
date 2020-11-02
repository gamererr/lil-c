#!/usr/bin/env python3

import random
import asyncio
import discord
from discord.ext import commands
from embeds import *

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

intents = discord.Intents.all()
prefix = "!"
client = commands.Bot(command_prefix=prefix,intents=intents)

consonants = ["pr", "br", "sc", "ng", "ch", "ck", "gh", "ph", "rh", "sh", "ti", "th", "wh", "zh", "ci", "wr", "qu", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
client.remove_command("help")
async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file()
		filelist.insert(len(filelist),file)
	return filelist

@client.event
async def on_ready():
	print("hello world!")

@client.command()
async def au(ctx,action = None):
	if (action == "list"):
		await ctx.send(embed=aulist)
	elif (action == "random"):
		await ctx.send(auwinnas[random.randrange(len(auwinnas))])
	elif (action == "submit"):
		await ctx.send("nope")
	elif (action == "help"):
		await ctx.send(embed=auhelpmessage)
	else:
		await ctx.send("unknown command, here are the commands for help", embed=auhelpmessage)

@client.command()
async def morelike(ctx, *text):
	ctext = " ".join(text)
	octext = ctext
	# bully vresod
	if "vresod" in ctext:
		ctext = ctext.replace("vresod", "big dumb stupid idiot head nerd")
		await ctx.send(
			f"{octext}? more like {ctext}"
		)
		return
	# fart
	if random.randrange(0, 2) == 1:
		ctext = ctext.replace("fort", "fart")
		ctext = ctext.replace("fert", "fart")
		ctext = ctext.replace("firt", "fart")
		ctext = ctext.replace("furt", "fart")
	# gay and lame
	if random.randrange(0, 2) == 1:
		ctext = ctext.replace("ga", "gay")
		for x in consonants:
			ctext = ctext.replace(f"{x}ay", "gay")
	else:
		for x in consonants:
			ctext = ctext.replace(f"{x}ame", "lame")
	# no
	for x in consonants:
		ctext = ctext.replace(f"{x}o ", "no")
	# i to o and double o
	if random.randrange(0, 2) == 1:
		ctext = ctext.replace("i", "o")
	else:
		ctext = ctext.replace("o", "oo")
	# ae to æ
	for x in consonants:
		ctext = ctext.replace(f"a{x}e", f"æ{x}")
	ctext = ctext.replace(f"ae", f"æ")
	# a to e
	ctext = ctext.replace("a", "e")
	for x in consonants:
		ctext = ctext.replace(f"{x}ee", f"pee")
	if ctext == octext:
		await ctx.send(f"{octext} is perfect, it cannot be changed")
	else:
		await ctx.send(f"{octext}? more like {ctext}")

@client.command()
async def pdp(ctx):
	await ctx.send(f"your randomly selected puppy dog pals song is {pdpsongs[random.randrange(len(pdpsongs))]}")
@client.command()
async def help(ctx):
	await ctx.send("unknown command, here are the commands for help", embed=helpmessage)
client.run(token)
