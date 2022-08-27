#last updated 29/10/2020 branch main
import discord
from discord.ext import commands
import asyncio
from discord.utils import get
import logging
import random
from datetime import datetime, timezone, timedelta, date
token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
BOT_PREFIX=">"
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)


current = False
help = """**Here are my commands master.** <:MotokaBlush:621601566889345028>

1. Did you finish the laundry yet, Motoka?
2. Will you cook for me, Motoka?
3. Motoka?
4. Motoka!
5. Motoka is cute
6. Good morning, Motoka!
7. Good night, Motoka
8. Kazuha is here
9. Laundry
10. Stupid bots
11. Do you like being a maid?
12. I love you, Motoka
13. Give the daily quote, Motoka
14. Motoka of the pool, what is your wisdom?
15. <:YahiroHappy:616719487928107013>
16. <:MotokaEhehe:607814360806588427>
17. :cocktail:
18. Motoka, kill **@user**
19. Motoka, pat **@user**"""

daily = ["I want to become happy happy soon.",
"In life, if there are negatives, there are positives.",
"Every dog has its day.",
"Trying too hard is just as bad as not trying.",
"Sangaria when your country goes BOOM, I hope you try pretty hard too.",
"I want to cry more, oh please let me cry more. Says the cuckoo bird.",
"Everything is wonderful.",
"Burn with jealousy, and get real wet.",
"First Time Ever in the Extra Part! A Cliffhanger Ending.",
"Oh No! We also got less porn!",
"Sorry! No porn again!",
"Haruka-kun...I really really reeeealy love you!",
]

motoka = 800821327648391168
akira = 889829898934439996
sora = 768265134027440128
bots = [motoka, akira, sora]

greetings = [" Welcome", " Please don't ignore me...", " Ara Ara <:MotokaAraAra:690380320993968138>",
    " Eh?! What are you doing here?! <:MotokaSurprised:621452996139679744>",
    " Hajimemashite. Nogisaka Motoka desu.", " <:MotokaHeadPat:724844821319254046>",
    " Hope you brought something to drink <:MotokaSip:768373514084155393>",
    " <:MotokaFight:768369578556129310>", " <a:YES:695193105179345016>"]

@bot.event
async def on_member_join(member):
    """Runs whenever a new member joins the server"""
    channel = bot.get_channel(595525657971392562)
    last = await channel.fetch_message(channel.last_message_id)
    last = await channel.fetch_message(channel.last_message_id)
    if last.author.id == sora:
        await channel.send(member.mention + random.choice(greetings))

@bot.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 663752882725584927 or message_id == 663753733766643732 or message_id == 1005208886011244584:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if message_id == 663752882725584927:  # message id for color roles
            emoji = payload.emoji.name  # name of the emoji the user reacts to
            if emoji == 'DarkRed':
                role = discord.utils.get(guild.roles, name="Dark Red")
            elif emoji == 'DarkBlue':
                role = discord.utils.get(guild.roles, name="Dark Blue")

            elif emoji == 'BrightPink':
                role = discord.utils.get(guild.roles, name="Bright Pink")
            elif emoji == 'LightGreen':
                role = discord.utils.get(guild.roles, name="Light Green")
            elif emoji == 'LightBlue':
                role = discord.utils.get(guild.roles, name="Light Blue")

            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

        elif message_id == 663753733766643732:  # message if for fan roles
            emoji = payload.emoji.name  # name of the emoji the user reacts to

            if emoji == "SoraHappy":
                role = discord.utils.get(guild.roles, name="Sora fan")
            elif emoji == "AkiraWink2":
                role = discord.utils.get(guild.roles, name="Akira fan")
            elif emoji == "MotokaTease":
                role = discord.utils.get(guild.roles, name="Motoka fan")
            elif emoji == "KozueHappy":
                role = discord.utils.get(guild.roles, name="Kozue fan")
            elif emoji == "KazuhaHappy":
                role = discord.utils.get(guild.roles, name="Kazuha fan")
            elif emoji == "NaoSmile":
                role = discord.utils.get(guild.roles, name="Nao fan")
            elif emoji == "YahiroHappy":
                role = discord.utils.get(guild.roles, name="Yahiro fan")
            elif emoji == "HarukaHuh":
                role = discord.utils.get(guild.roles, name="Haruka fan")
            elif emoji == "RyouheiEhehe":
                role = discord.utils.get(guild.roles, name="Ryouhei fan")

        elif message_id == 1005208886011244584:  # message if for emote role things
            emoji = payload.emoji.name  # name of the emoji the user reacts to

            if emoji == "HarukaLUL":
                role = discord.utils.get(guild.roles, name="Haruka Laugh")
            elif emoji == "HarukaHuh":
                role = discord.utils.get(guild.roles, name="Haruka Huh")
            elif emoji == "SoraHappy":
                role = discord.utils.get(guild.roles, name="Sora Happy")
            elif emoji == "SoraSleepy2":
                role = discord.utils.get(guild.roles, name="Sora Sleepy")
            elif emoji == "SoraLove":
                role = discord.utils.get(guild.roles, name="Sora Love")
            elif emoji == "SoraEvilGrin":
                role = discord.utils.get(guild.roles, name="Sora Evil Grin")
            elif emoji == "SoraEheheh":
                role = discord.utils.get(guild.roles, name="Sora Ehehe")
            elif emoji == "AkiraSmile2":
                role = discord.utils.get(guild.roles, name="Akira Smile")
            elif emoji == "AkiraUwU":
                role = discord.utils.get(guild.roles, name="Akira UwU")
            elif emoji == "AkiraWink2":
                role = discord.utils.get(guild.roles, name="Akira Wink")
            elif emoji == "MotokaAraAra":
                role = discord.utils.get(guild.roles, name="Motoka Ara Ara")
            elif emoji == "MotokaEhehe":
                role = discord.utils.get(guild.roles, name="Motoka Ehehe")
            elif emoji == "KazuhaLaugh":
                role = discord.utils.get(guild.roles, name="Kazuha Laugh")
            elif emoji == "NaoYeyy":
                role = discord.utils.get(guild.roles, name="Nao Yeyy")
            elif emoji == "KozueBlush":
                role = discord.utils.get(guild.roles, name="Kozue Blush")
            elif emoji == "YahiroPing":
                role = discord.utils.get(guild.roles, name="Yahiro Ping")
            elif emoji == "RyouheiEhehe":
                role = discord.utils.get(guild.roles, name="Ryouhei Laugh")
            elif emoji == "Butler":
                role = discord.utils.get(guild.roles, name="Butler")
            elif emoji == "CatShishou3":
                role = discord.utils.get(guild.roles, name="Shishou")
            elif emoji == "Bunny":
                role = discord.utils.get(guild.roles, name="Bunny")

        if role is not None:
            member = payload.member
            if member:
                await member.add_roles(role)
                print("role given")
            else:
                print("member not found")
        else:
            print("role not found")


"""async def on_raw_reaction_add(payload): # adds roles on raact
    message_id = payload.message_id
    if message_id == 663752882725584927 or message_id == 663753733766643732:

        guild_id = payload.guild_id
        guild = discord.utils.find( lambda g : g.id == guild_id, bot.guilds)
        if message_id ==663752882725584927: # message id for color roles
            emoji = payload.emoji.name # name of the emoji the user reacts to
            role = discord.utils.get(guild.roles, name= emote_reacts.get(emoji))

        elif message_id == 663753733766643732: # message if for fan roles
            emoji = payload.emoji.name # name of the emoji the user reacts to
            role = discord.utils.get(guild.roles, name=emote_reacts.get(emoji))

        if role is not None:
            #member = discord.utils.find( lambda m : m.id == payload.user_id, guild.members)
            member = payload.member
            if member:
                await member.add_roles(role)
                print("role given")
            else:
                print("member not found")
        else:
            print("role not found")"""


@bot.event
async def on_raw_reaction_remove(payload): # Remove roles on when a user removes a react
    message_id = payload.message_id
    if message_id == 663752882725584927 or message_id == 663753733766643732 or message_id == 1005208886011244584:

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        if message_id == 663752882725584927:  # message id for color roles
            emoji = payload.emoji.name  # name of the emoji the user reacts to
            if emoji == 'DarkRed':
                role = discord.utils.get(guild.roles, name="Dark Red")
            elif emoji == 'DarkBlue':
                role = discord.utils.get(guild.roles, name="Dark Blue")

            elif emoji == 'BrightPink':
                role = discord.utils.get(guild.roles, name="Bright Pink")
            elif emoji == 'LightGreen':
                role = discord.utils.get(guild.roles, name="Light Green")
            elif emoji == 'LightBlue':
                role = discord.utils.get(guild.roles, name="Light Blue")

            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

        elif message_id == 663753733766643732:  # message if for fan roles
            emoji = payload.emoji.name  # name of the emoji the user reacts to

            if emoji == "SoraHappy":
                role = discord.utils.get(guild.roles, name="Sora fan")
            elif emoji == "AkiraWink2":
                role = discord.utils.get(guild.roles, name="Akira fan")
            elif emoji == "MotokaTease":
                role = discord.utils.get(guild.roles, name="Motoka fan")
            elif emoji == "KozueHappy":
                role = discord.utils.get(guild.roles, name="Kozue fan")
            elif emoji == "KazuhaHappy":
                role = discord.utils.get(guild.roles, name="Kazuha fan")
            elif emoji == "NaoSmile":
                role = discord.utils.get(guild.roles, name="Nao fan")
            elif emoji == "YahiroHappy":
                role = discord.utils.get(guild.roles, name="Yahiro fan")
            elif emoji == "HarukaHuh":
                role = discord.utils.get(guild.roles, name="Haruka fan")
            elif emoji == "RyouheiEhehe":
                role = discord.utils.get(guild.roles, name="Ryouhei fan")


        elif message_id == 1005208886011244584:  # message if for emote role things
            emoji = payload.emoji.name  # name of the emoji the user reacts to

            if emoji == "HarukaLUL":
                role = discord.utils.get(guild.roles, name="Haruka Laugh")
            elif emoji == "HarukaHuh":
                role = discord.utils.get(guild.roles, name="Haruka Huh")
            elif emoji == "SoraHappy":
                role = discord.utils.get(guild.roles, name="Sora Happy")
            elif emoji == "SoraSleepy2":
                role = discord.utils.get(guild.roles, name="Sora Sleepy")
            elif emoji == "SoraLove":
                role = discord.utils.get(guild.roles, name="Sora Love")
            elif emoji == "SoraEvilGrin":
                role = discord.utils.get(guild.roles, name="Sora Evil Grin")
            elif emoji == "SoraEheheh":
                role = discord.utils.get(guild.roles, name="Sora Ehehe")
            elif emoji == "AkiraSmile2":
                role = discord.utils.get(guild.roles, name="Akira Smile")
            elif emoji == "AkiraUwU":
                role = discord.utils.get(guild.roles, name="Akira UwU")
            elif emoji == "AkiraWink2":
                role = discord.utils.get(guild.roles, name="Akira Wink")
            elif emoji == "MotokaAraAra":
                role = discord.utils.get(guild.roles, name="Motoka Ara Ara")
            elif emoji == "MotokaEhehe":
                role = discord.utils.get(guild.roles, name="Motoka Ehehe")
            elif emoji == "KazuhaLaugh":
                role = discord.utils.get(guild.roles, name="Kazuha Laugh")
            elif emoji == "NaoYeyy":
                role = discord.utils.get(guild.roles, name="Nao Yeyy")
            elif emoji == "KozueBlush":
                role = discord.utils.get(guild.roles, name="Kozue Blush")
            elif emoji == "YahiroPing":
                role = discord.utils.get(guild.roles, name="Yahiro Ping")
            elif emoji == "RyouheiEhehe":
                role = discord.utils.get(guild.roles, name="Ryouhei Laugh")
            elif emoji == "Butler":
                role = discord.utils.get(guild.roles, name="Butler")
            elif emoji == "CatShishou3":
                role = discord.utils.get(guild.roles, name="Shishou")
            elif emoji == "Bunny":
                role = discord.utils.get(guild.roles, name="Bunny")

        if role is not None:
            member = guild.get_member(payload.user_id)
            if member:
                await member.remove_roles(role)
                print("role removed")
            else:
                print("member not found")
        else:
            print("could not remove role ")


    """if message_id == 663752882725584927 or message_id ==663753733766643732:
        guild_id = payload.guild_id
        guild = discord.utils.find( lambda g : g.id == guild_id, bot.guilds)
        
        emoji = payload.emoji.name # name of the emoji the user reacts to
        role = discord.utils.get(guild.roles, name=emote_reacts.get(emoji))


       

        member = guild.get_member(payload.user_id)
        
        print(member)
        if role is not None:

            if member:
                await member.remove_roles(role)
                print("role removed")
            else:
                print("member not found")
        else:
            print("could not remove role ")"""
@bot.event
async def on_message(message):
    global current
    if message.author == bot.user:
        return

    if message.content.lower() == "did you finish the laundry yet, motoka?":
        await message.channel.send("<:MotokaAnnoyed:621451371052400651>")

    if message.content.lower() == "will you cook for me, motoka?":
        await message.channel.send("If you ask me nicely, master~ <:MotokaTease:621452497399054336>")

    if message.content.lower() == "motoka?":
        await message.channel.send("Yes, Master? <:MotokaHappy:616738739259179063>")

    if message.content.lower() == "motoka!":
        await message.channel.send("Haaaaiiiiii <:MotokaSmile:617092202119561226>")

    if message.content.lower() == "motoka is cute":
        react = "<:MotokaBlush:621601566889345028>"
        await message.add_reaction(react)

    if message.content.lower() == "good morning, motoka!":
        await message.channel.send("Good morning! Did you sleep well?")

    if message.content.lower() == "good night, motoka":
        await message.channel.send("Oyasumi. <:MotokaWink:621610020597137418>")

    if message.content.lower() == "kazuha is here":
        await message.channel.send("Ojou-samaa?!?! <:MotokaSurprised:621452996139679744>")

    if message.content.lower() == "laundry":
        await message.channel.send("<:MotokaSurprised:621452996139679744>")

    if message.content.lower() == "stupid bots":
        react = "<:MotokaCry:607814347380621323>"
        await message.add_reaction(react)

    if message.content.lower() == "do you like being a maid?":
        await message.channel.send("<:MotokaShrug:656268770850897920>")

    if message.content.lower() == "i love you, motoka":
        await message.channel.send("Really?! <:MotokaSurprised:621452996139679744>")

    if message.content.lower() == "give the daily quote, motoka" or message.content.lower() == "motoka of the pool, what is your wisdom?":
        if not current:
            current = datetime.now(timezone(timedelta(hours=1))).date()
            x = random.randint(0, 11)
            response = daily[x]
            await message.channel.send(response)
        else:
            day = datetime.now(timezone(timedelta(hours=1))).date()
            if day == current:
                await message.channel.send("Huh? But I already did a quote today.<:MotokaSurprised:621452996139679744>")
            else:
                x = random.randint(0, 11)
                response = daily[x]
                await message.channel.send(response)
                current = day


    if message.content == "<:YahiroHappy:616719487928107013>":
        await message.channel.send("Osake!! <:MotokaSmile:617092202119561226>")

    if message.content == "🍸":
        await message.channel.send("<:MotokaEhehe:607814360806588427>")

    if message.content.lower().startswith("motoka, kill"):
        meslist = message.content.split(" ")
        if len(meslist) == 3 and "@" in meslist[2]:
            mention = "<@!" + str(message.mentions[0].id) + ">"
            x = random.randint(1,7)
            if x == 1:
                response = mention + " <:MotokaFight:768369578556129310>"
            elif x == 2:
                response = mention + "Hai, Goshūjin-Sama. :knife:"
            elif x == 3:
                response = "Kinda busy at the moment. <:MotokaSip:768373514084155393>"
            elif x == 4:
                response = mention + "Naughty Children need to be punished! <:MotokaFight:768369578556129310>"
            elif x == 5:
                response = "Wouldn’t that get me fired? <:MotokaEhehe:607814360806588427>"
            elif x == 6:
                response = "<:MotokaSurprised:621452996139679744>"
            elif x == 7:
                response = mention + "Sure. Why not? <:MotokaShrug:656268770850897920> <:Dagger:853058515248873473>"
            await message.channel.send(response)

    if message.content.lower().startswith("motoka, pat"):
        meslist = message.content.split(" ")
        if len(meslist) == 3 and "@" in meslist[2]:
            mention = "<@!" + str(message.mentions[0].id) + ">"
            x = random.randint(1, 2)
            if x == 1:
                response = mention + " <:MotokaHeadPat:724844821319254046>"
            elif x == 2:
                response = "<:MotokaTease:621452497399054336>"
            await message.channel.send(response)

    if message.content.lower() == "motoka help":
        await bot.get_user(message.author.id).send(help)

    if message.content == "<:MotokaEhehe:607814360806588427>":
        react = "<:MotokaEhehe:607814360806588427>"
        await message.add_reaction(react)
    botdev = discord.utils.get(message.channel.guild.roles, name="Bot Dev")
    if message.content.lower() == "motoka, reset" and botdev in message.author.roles:
        await message.channel.send("Resetting")
        exit()








@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game(name="Motoka\'s route"))

    print('------')

bot.run(token)