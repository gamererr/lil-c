#!/usr/bin/env python3

import random
import asyncio
import discord
import requests
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

async def morelikeend(morelike, original, message):
    if morelike.lower() == original.lower():
        await message.channel.send(f"{original} is perfect, it cannot be changed")
    else:
        await message.channel.send(f"{original}? more like {morelike}")

@client.event
async def on_ready():
	print("hello world!")

prefix = "!"

# lists
auwinnas = ["<:Chickenwinna:759085236679868526> - chickenwinna prime, the basic chickenwinna", "<:ThiefChickenwinna:757436624152821770> - Thiefwinna", "<:WarWinna:759283034645594112> - WarWinna", "<:ThatWinna:757436113743773818> - ThatWinna", "<:StinkyWinna:760016992505036820> - StinkyWinna, he smells", "<:PogWinna:759044866444361788> - POGCHAMP", "<:Chickenwinna2020:757436053589196900> - Chickenwinna 2020", "<:ArrowWinna:759053771773968395> - KoichiWinna (arrow alt)", "<:ChickenwinnaBaldMartin:757436055766171649> - MartinWinna", "<:ChickenwinnaDistraction:757436043589976155> - DistractionWinna, what was i saying again?", "<:ChickenwinnaFnafCostume:757436050770493571> - FreddyWinna", "<:ChickenwinnaFubiBu:771180135487111219> - Fubibu Junor", "<:ChickenwinnaGame:757436050875613226> - Gamewinna, the gamer has become the game", "<:ChickenwinnaGhost:757436043761942568> - GhostWinna", "<:ChickenwinnaGolden:757436052502872124> - GoldenWinna", "<:ChickenwinnaSock:758036446006214780> - SockWinna", "<:ChickenwinnaSociety:757436044055674890> - JokerWinna", "<:ChickenwinnaSad:757436043816468490> - SadWinna", "<:ChickenwinnaPasta:757436048211968121> - NoodleWinna", "<:ChickenwinnaOriginal:757436043837308960> - OGWinna", "<:ChickenwinnaNoBody:757436052850999386> - Nobody", "<:ChickenwinnaMakeup:757436043900485732> - ~~hookerwinna~~", "<:ChickenwinnaKing:757436055220912169> - KingWinna", "<:ChickenwinnaHalloween:760929363511476234> - SpookyWinna", "<:Chickenwinnastupidnormiebrand:757436051177341026> - CorsairWinna", "<:ChickenwinnaWacky:771179967210848267> - WackyWinna", "<:ChickenwinnaWall:757436048451043338> - WallWinna", "<:Chikanweenuh:757436045653704796> - Chikanweenuh", "<:ChuckleWinna:762714207304548353> - ChuckleWinna", "<:ChungusWinna:760929010107940945> - chunguswinna, the cw from the ideal timeline", "<:Frenchwinna:758389011248185375> - FrenchWinna", "<:Noobwinna:760017383980662814> - Noobwinna"]
pdpsongs = ["https://youtu.be/GA6QunYgb-Q", "https://youtu.be/5tWoJndJA0E", "https://youtu.be/Qrax7n2QOwE", "https://youtu.be/KRXy2JkV3HU", "https://youtu.be/iKpSSA7jr3w", "https://youtu.be/WThe2NmwRfo", "https://youtu.be/E1Q-zYzp670", "https://youtu.be/n-MV8TCtCxk", "https://youtu.be/jmN6j67ZGjc", "https://youtu.be/B7VSMkS3VZ4", "https://youtu.be/2ZVD8enTzDM", "https://youtu.be/Sh5IwGyv7o8", "https://youtu.be/4U5uslyCbf8", "https://youtu.be/nN2scIaKbww", "https://youtu.be/dQw4w9WgXcQ"]
perfectwords = ["big chungus", "chickenwinna", "ur mom"]
consonants = ["pr", "br", "sc", "ng", "ch", "ck", "gh", "ph", "rh", "sh", "ti", "th", "wh", "zh", "ci", "wr", "qu", "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

# embeds
helpmessage = discord.Embed(title="Commands", description="au - commands for au winnas, has extra arguemnts \nmorelike [word] - responds with '[word]? more like [word but edited]' \npdp - gives a random pdp song", color=0x7e01e4)
helpmessage.set_footer(text="comands with extra arguments can be used to get more info out of with !help [command]")
auhelpmessage = discord.Embed(title="AU commands", description="random - gives a random AU winna with image and name (not coded yet) \nlist - lists all au winnas \nsubmit - submit an au winna to the mods (not added yet)", color=0x7e01e4)
aulist = discord.Embed(title="au winnas", description=f"{auwinnas[0]}\n{auwinnas[1]}\n{auwinnas[2]}\n{auwinnas[3]}\n{auwinnas[4]}\n{auwinnas[5]}\n{auwinnas[6]}\n{auwinnas[7]}\n{auwinnas[8]}\n{auwinnas[9]}\n{auwinnas[10]}\n{auwinnas[11]}\n{auwinnas[12]}\n{auwinnas[13]}\n{auwinnas[14]}\n{auwinnas[15]}\n{auwinnas[16]}\n{auwinnas[17]}\n{auwinnas[18]}\n{auwinnas[19]}\n{auwinnas[20]}\n{auwinnas[21]}\n{auwinnas[22]}\n{auwinnas[23]}\n{auwinnas[24]}\n{auwinnas[25]}\n{auwinnas[26]}\n{auwinnas[27]}\n{auwinnas[28]}\n{auwinnas[29]}\n{auwinnas[30]}\n{auwinnas[31]}", color=0x00C400)
aulistnoemoji = discord.Embed(title="au winnas that dont have emojis", description="there are none yet, check back later")

@client.event
async def on_message(message):
    args = message.content.lower
    args = message.content.replace(prefix,"")
    argslist = args.split(" ")

    modchat = discord.utils.get(message.guild.channels, id=757449377819263028)

    # add reaction buttons for !au submit
    if ("submited an au chickenwinna, " in message.content) and (message.author == client.user) and (message.channel == modchat):
        await message.add_reaction("✅")
        await message.add_reaction("☑️")
        await message.add_reaction("❌")
        await message.add_reaction("❓")

    if message.content.startswith(prefix):
        if message.author == client.user:
            return
        elif (argslist[0] == "au"): # au commands
            if (argslist[1] == "list"): # list all of the officially reconized au winnas
                if (argslist[2] == "yes" or argslist[2] == "y"):
                    await message.channel.send(embed=aulist)
                elif (argslist[2] == "no" or argslist[2] == "n"):
                    await message.channel.send(embed=aulistnoemoji)
                else:
                    await message.channel.send("fun fact: you can do !au list <yes/no> to choose whether or not you want the list of aus with or without the emojis", embed=aulist)
            elif (argslist[1] == "random"): # send a random au winna
                await message.channel.send(auwinnas[random.randrange(len(auwinnas))])
            elif (argslist[1] == "submit"): # submiting an au chickenwinna
                try:
                    ausubmitname = argslist[2]
                except IndexError:
                    await message.channel.send("you need an au name")
                try:
                    ausubmitemoji = message.attachments[0]
                except IndexError:
                    await message.channel.send("you need an image")
                r = requests.get(ausubmitemoji.url, allow_redirects=True)
                open('newemoji.png', 'wb').write(r.content)
                open('newemojiname', 'wt').write(ausubmitname)
                files = await attachments_to_files(message.attachments,True)
                await modchat.send(f"{message.author.mention} submited an au chickenwinna, *{ausubmitname}*", files=files)
            elif (argslist[1] == "help"): # the au command set's very own help message command
                auhelpmessage.color = 0x00C400
                await message.channel.send(embed=auhelpmessage)
            else:
                auhelpmessage.color = 0xFF0000
                await message.channel.send("unknown command, here are the commands for help", embed=auhelpmessage)
        elif (argslist[0] == "morelike"): # the command that changes random letters with others
            morelike = message.content[10:].lower()
            #bully vresod
            if "vresod" in morelike:
                morelike = morelike.replace("vresod", "big dumb stupid idiot head nerd")
                await morelikeend(morelike=morelike, original=morelike, message=message)
                return
            for word in perfectwords:
                if morelike == word:
                    morelike = message.content[10:]
                    await morelikeend(morelike, original=morelike)
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
            # double o
            morelike = morelike.replace("o", "oo")
            # i to o
            morelike = morelike.replace("i","o")
            # ae to æ
            for x in consonants:
                morelike = morelike.replace(f"a{x}e",f"æ{x}")
            morelike = morelike.replace(f"ae",f"æ")
            # a to e
            morelike = morelike.replace("a", "e")
            for x in consonants:
                morelike = morelike.replace(f"{x}ee",f"pee")
            await morelikeend(morelike, original=message.content[10:].lower(), message=message)
        elif (argslist[0] == "pdp"): # command that sends a song from the show Puppy Dog Pals
            if not (len(argslist) == 1): # for specifically requesting a song
                try:
                    x = int(argslist[1]) - 1
                    if x == -1:
                        await message.channel.send("that number is too high or low!")
                        return
                except ValueError:
                    await message.channel.send("that is not a number!")
                try:
                    await message.channel.send(f"you requested this puppy dog pals song {pdpsongs[x]}")
                except IndexError:
                    await message.channel.send("that number is too high or low!")
            else: # for a random song
                await message.channel.send(f"your randomly selected puppy dog pals song is {pdpsongs[random.randrange(len(pdpsongs))]}")
        elif (argslist[0] == "help"): # the help message, duh
            helpmessage.color = 0x00C400
            await message.channel.send(embed=helpmessage)
        else: # for when an unknown command is put in
            helpmessage.color = 0xFF0000
            await message.channel.send("unknown command, here are the commands for help", embed=helpmessage)

@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    modchat = discord.utils.get(message.guild.channels, id=757449377819263028)
    general = discord.utils.get(message.guild.channels, id=757433959117488193)
    if user == client.user:
        return
    if not ("submited an au chickenwinna, " in message.content) and (message.author == client.user) and (message.channel == modchat):
        return

    newemojiname = open('newemojiname', 'rt').read()
    newemoji = open('newemoji.png', 'rb').read()

    if reaction.emoji == "✅":
        try:
            await message.guild.create_custom_emoji(name=newemojiname,image=newemoji)
            await general.send(f"{message.mentions[0].mention} your au submission for {newemojiname} has been acccepted")
        except discord.errors.HTTPException:
            await general.send(f"{message.mentions[0].mention} your au submission for {newemojiname} has been acccepted but could not be made into an emoji due to an error (emoji cap, invalid character, etc)")
        await message.clear_reaction("✅")
        await message.clear_reaction("☑️")
        await message.clear_reaction("❌")
        await message.clear_reaction("❓")
    elif reaction.emoji == "☑️":
        await general.send(f"{message.mentions[0].mention} your au submission for {newemojiname} has been acccepted but wont be an emoji")
        await message.clear_reaction("✅")
        await message.clear_reaction("☑️")
        await message.clear_reaction("❌")
        await message.clear_reaction("❓")
    elif reaction.emoji == "❌":
        await general.send(f"{message.mentions[0].mention} your au submission for {newemojiname} has been denied. ask {user} why that is if you have questions")
        await message.clear_reaction("✅")
        await message.clear_reaction("☑️")
        await message.clear_reaction("❌")
        await message.clear_reaction("❓")
    elif reaction.emoji == "❓":
        await message.channel.send(f"{user.name}, here is what the emoji inputs do: \n✅ accepts and makes the submission an emoji \n☑️ accepts but does not make submission and emoji \n❌ denies the submission\n❓ you are reading it now idiot")
    else:
        return

client.run(token)