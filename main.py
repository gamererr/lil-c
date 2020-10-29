#!/usr/bin/env python3

import random
import asyncio
import discord
from discord import Member, Embed

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

intents = discord.Intents.all()
client = discord.Client(intents=intents)

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file()
		filelist.insert(len(filelist),file)
	return filelist

@client.event
async def on_ready():
	print("hello world!")

prefix = "!"

@client.event
async def on_message(message):

    helpmessage = discord.Embed(title="Commands", description="au - commands for au winnas, has extra arguemnts \nmorelike [word] - responds with '[word]? more like [word but edited]' \npdp - gives a random pdp song", color=0x7e01e4)
    helpmessage.set_footer(text="comands with extra arguments can be used to get more info out of with !help [command]")
    auhelpmessage = discord.Embed(title="AU commands", description="random - gives a random AU winna with image and name (not coded yet) \nlist - lists all au winnas \nsubmit - submit an au winna to the mods (not added yet)", color=0x7e01e4)

    pdpsongs = ["https://youtu.be/GA6QunYgb-Q", "https://youtu.be/5tWoJndJA0E", "https://youtu.be/Qrax7n2QOwE", "https://youtu.be/KRXy2JkV3HU", "https://youtu.be/iKpSSA7jr3w", "https://youtu.be/WThe2NmwRfo", "https://youtu.be/E1Q-zYzp670", "https://youtu.be/n-MV8TCtCxk", "https://youtu.be/jmN6j67ZGjc", "https://youtu.be/B7VSMkS3VZ4", "https://youtu.be/2ZVD8enTzDM", "https://youtu.be/Sh5IwGyv7o8", "https://youtu.be/4U5uslyCbf8", "https://youtu.be/nN2scIaKbww", "https://youtu.be/dQw4w9WgXcQ"]

    args = message.content.lower
    args = message.content.replace(prefix,"")
    argslist = args.split(" ")

    if message.content.startswith(prefix):
        if (argslist[0] == "au"):
            if (argslist[1] == "list"):
                await message.channel.send("nope")
            elif (argslist[1] == "random"):
                await message.channel.send("nope")
            elif (argslist[1] == "submit"):
                await message.channel.send("nope")
            elif (argslist[1] == "help"):
                await message.channel.send(embed=auhelpmessage)
            else:
                await message.channel.send("unknown command, here are the commands for help", embed=auhelpmessage)
        elif (argslist[0] == "morelike"):
            await message.channel.send("nope")
        elif (argslist[0] == "pdp"):
            await message.channel.send(f"your randomly selected puppy dog pals song is {pdpsongs[random.randrange(len(pdpsongs))]}")
        elif (argslist[0] == "help"):
            await message.channel.send(embed=helpmessage)
        else:
            await message.channel.send("unknown command, here are the commands for help", embed=helpmessage)

client.run(token)