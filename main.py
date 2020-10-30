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
consonants = ["pr", "br", "sc", "ng", "ch", "ck", "gh", "ph", "rh", "sh", "ti", "th", "wh", "zh", "ci", "wr", "qu", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
@client.event
async def on_message(message):

    helpmessage = discord.Embed(title="Commands", description="au - commands for au winnas, has extra arguemnts \nmorelike [word] - responds with '[word]? more like [word but edited]' \npdp - gives a random pdp song", color=0x7e01e4)
    helpmessage.set_footer(text="comands with extra arguments can be used to get more info out of with !help [command]")
    auhelpmessage = discord.Embed(title="AU commands", description="random - gives a random AU winna with image and name (not coded yet) \nlist - lists all au winnas \nsubmit - submit an au winna to the mods (not added yet)", color=0x7e01e4)

    auwinnas = ["<:Chickenwinna:759085236679868526> - chickenwinna prime, the basic chickenwinna", "<:ThiefChickenwinna:757436624152821770> - Thiefwinna", "<:WarWinna:759283034645594112> - WarWinna", "<:ThatWinna:757436113743773818> - ThatWinna", "<:StinkyWinna:760016992505036820> - StinkyWinna, he smells", "<:PogWinna:759044866444361788> - POGCHAMP", "<:Chickenwinna2020:757436053589196900> - Chickenwinna 2020", "<:ArrowWinna:759053771773968395> - KoichiWinna (arrow alt)", "<:ChickenwinnaBaldMartin:757436055766171649> - MartinWinna", "<:ChickenwinnaDistraction:757436043589976155> - DistractionWinna, what was i saying again?", "<:ChickenwinnaFnafCostume:757436050770493571> - FreddyWinna", "<:ChickenwinnaFubiBu:771180135487111219> - Fubibu Junor", "<:ChickenwinnaGame:757436050875613226> - Gamewinna, the gamer has become the game", "<:ChickenwinnaGhost:757436043761942568> - GhostWinna", "<:ChickenwinnaGolden:757436052502872124> - GoldenWinna", "<:ChickenwinnaSock:758036446006214780> - SockWinna", "<:ChickenwinnaSociety:757436044055674890> - JokerWinna", "<:ChickenwinnaSad:757436043816468490> - SadWinna", "<:ChickenwinnaPasta:757436048211968121> - NoodleWinna", "<:ChickenwinnaOriginal:757436043837308960> - OGWinna", "<:ChickenwinnaNoBody:757436052850999386> - Nobody", "<:ChickenwinnaMakeup:757436043900485732> - ~~hookerwinna~~", "<:ChickenwinnaKing:757436055220912169> - KingWinna", "<:ChickenwinnaHalloween:760929363511476234> - SpookyWinna", "<:Chickenwinnastupidnormiebrand:757436051177341026> - CorsairWinna", "<:ChickenwinnaWacky:771179967210848267> - WackyWinna", "<:ChickenwinnaWall:757436048451043338> - WallWinna", "<:Chikanweenuh:757436045653704796> - Chikanweenuh", "<:ChuckleWinna:762714207304548353> - ChuckleWinna", "<:ChungusWinna:760929010107940945> - chunguswinna, the cw from the ideal timeline", "<:Frenchwinna:758389011248185375> - FrenchWinna", "<:Noobwinna:760017383980662814> - Noobwinna"]
    aulist = discord.Embed(title="au winnas", description=f"{auwinnas[0]}\n{auwinnas[1]}\n{auwinnas[2]}\n{auwinnas[3]}\n{auwinnas[4]}\n{auwinnas[5]}\n{auwinnas[6]}\n{auwinnas[7]}\n{auwinnas[8]}\n{auwinnas[9]}\n{auwinnas[10]}\n{auwinnas[11]}\n{auwinnas[12]}\n{auwinnas[13]}\n{auwinnas[14]}\n{auwinnas[15]}\n{auwinnas[16]}\n{auwinnas[17]}\n{auwinnas[18]}\n{auwinnas[19]}\n{auwinnas[20]}\n{auwinnas[21]}\n{auwinnas[22]}\n{auwinnas[23]}\n{auwinnas[24]}\n{auwinnas[25]}\n{auwinnas[26]}\n{auwinnas[27]}\n{auwinnas[28]}\n{auwinnas[29]}\n{auwinnas[30]}\n{auwinnas[31]}", color=0x7e01e4)
    pdpsongs = ["https://youtu.be/GA6QunYgb-Q", "https://youtu.be/5tWoJndJA0E", "https://youtu.be/Qrax7n2QOwE", "https://youtu.be/KRXy2JkV3HU", "https://youtu.be/iKpSSA7jr3w", "https://youtu.be/WThe2NmwRfo", "https://youtu.be/E1Q-zYzp670", "https://youtu.be/n-MV8TCtCxk", "https://youtu.be/jmN6j67ZGjc", "https://youtu.be/B7VSMkS3VZ4", "https://youtu.be/2ZVD8enTzDM", "https://youtu.be/Sh5IwGyv7o8", "https://youtu.be/4U5uslyCbf8", "https://youtu.be/nN2scIaKbww", "https://youtu.be/dQw4w9WgXcQ"]

    args = message.content.lower
    args = message.content.replace(prefix,"")
    argslist = args.split(" ")

    if message.content.startswith(prefix):
        if (argslist[0] == "au"):
            if (argslist[1] == "list"):
                await message.channel.send(embed=aulist)
            elif (argslist[1] == "random"):
                await message.channel.send(auwinnas[random.randrange(len(auwinnas))])
            elif (argslist[1] == "submit"):
                await message.channel.send("nope")
            elif (argslist[1] == "help"):
                await message.channel.send(embed=auhelpmessage)
            else:
                await message.channel.send("unknown command, here are the commands for help", embed=auhelpmessage)
        elif (argslist[0] == "morelike"):
            morelike = message.content[10:].lower()
            #bully vresod
            if "vresod" in morelike:
                morelike = morelike.replace("vresod", "big dumb stupid idiot head nerd")
                await message.channel.send(f"{message.content[10:].lower()}? more like {morelike}")
                return
            # fart
            if (random.randrange(0, 2) == 1):
                morelike = morelike.replace("fort","fart")
                morelike = morelike.replace("fert","fart")
                morelike = morelike.replace("firt","fart")
                morelike = morelike.replace("furt","fart")
            # gay and lame
            if (random.randrange(0, 2) == 1):
                morelike = morelike.replace("ga","gay")
                for x in consonants:
                    morelike = morelike.replace(f"{x}ay","gay")
            else:
                for x in consonants:
                    morelike = morelike.replace(f"{x}ame","lame")
            # no
            for x in consonants:
                morelike = morelike.replace(f"{x}o ","no")
            # i to o and double o
            if (random.randrange(0, 2) == 1):
                morelike = morelike.replace("i","o")
            else:
                morelike = morelike.replace("o", "oo")
            # ae to æ
            for x in consonants:
                morelike = morelike.replace(f"a{x}e",f"æ{x}")
            morelike = morelike.replace(f"ae",f"æ")
            # a to e
            morelike = morelike.replace("a", "e")
            for x in consonants:
                morelike = morelike.replace(f"{x}ee",f"pee")
            if morelike == message.content[10:].lower():
                await message.channel.send(f"{morelike} is perfect, it cannot be changed")
            else:
                await message.channel.send(f"{message.content[10:].lower()}? more like {morelike}")
        elif (argslist[0] == "pdp"):
            await message.channel.send(f"your randomly selected puppy dog pals song is {pdpsongs[random.randrange(len(pdpsongs))]}")
        elif (argslist[0] == "help"):
            await message.channel.send(embed=helpmessage)
        else:
            await message.channel.send("unknown command, here are the commands for help", embed=helpmessage)

client.run(token)