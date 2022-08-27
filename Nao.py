import os
import random
import discord
from discord.ext import commands

# from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

meid = 407747014806208523

TOKEN = ('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
GUILD = ('Yosuga no Sora')

bot = commands.Bot(command_prefix='!')

client = discord.Client(intents=intents)
help = """**Here is a list of my commands!** <:NaoYeyy:609375678579867658>

1. Hi or Hello Nao
2. Good Morning or GM Nao
3. Good night or GN Nao
4. @Nao
5. Nao do you love Haru?
6. Splash splash
7. Will you go out with me Nao?
8. I love you Nao
9. Stupid Bots
10. Nao kill @user
11. <a:SoraNaoFight:642985262565294090>
12. <a:Sora:642665322985291776>
13: <:NaoYeyy:609375678579867658>
14: <:HarukaSleepy:852672066163179532>
15: <:SoraHate:617072191225462785>"""

#g = client.get_guild(348796287606456321)
for guild in client.guilds:
    try:
        stick = g.fetch_sticker(1005758615656878160)
    except:
        pass

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    await client.change_presence(activity=discord.Game(name="Nao's route"))

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )



@client.event
async def on_message(message):
    try:
        admin = discord.utils.get(message.channel.guild.roles, name="Admin")
        botdev = discord.utils.get(message.channel.guild.roles, name="Bot Dev")
        mod = discord.utils.get(message.channel.guild.roles, name="Mods")
    except:
        pass

    m = message.content.lower()
    c = message.channel

    if message.author == client.user:
        return

    if m in ["hello nao", "hi nao"]:
        await c.send("Hi! <:NaoSmile:598913197168132117>")
    if m == "i love you nao":
        await c.send("<:NaoBlush:852672067693576202>")
    if m == "stupid bots":
        await message.add_reaction("<:NaoFlustered:852672068574117908>")
    if m in ["good morning nao", "gm nao"]:
        await c.send("Want me to make you breakfast? <:NaoSmile:598913197168132117>")
    if m in ["good night nao", "gn nao"]:
        await c.send("Good Night, have a good sleep. <:NaoSmile:598913197168132117>")
    if message.mentions:
        if len(message.content.split(" ")) == 1:
            if message.mentions[0].id == 1005747090338623508:
                await c.send("<:NaoYeyy:609375678579867658>")
    if m == "<a:SoraNaoFight:642985262565294090>".lower():
        await message.add_reaction("<:NaoLUL:609342186684940288>")
    if m == "splash splash":
        await c.send("CHAPA CHAPA")
    if m == "<:NaoYeyy:609375678579867658>".lower():
        await message.add_reaction("<:NaoYeyy:609375678579867658>")
    if m == "<a:Sora:642665322985291776>".lower():
        await c.send("Sora-chan!")
    if m == "nao do you love haru?":
        await c.send("...Yes I do <:NaoBlush:852672067693576202>")
    if m.startswith("nao kill ") and message.mentions:
        r = ["Killing is bad <:NaoFlustered:852672068574117908>", "No!", message.mentions[0].mention + "<:NaoYeyy:609375678579867658>:knife:"]
        await c.send(random.choice(r))
    if m == "<:HarukaSleepy:852672066163179532>".lower():
        await message.add_reaction("<:NaoLUL:609342186684940288>")
    if m == "<:SoraHate:617072191225462785>".lower():
        await message.add_reaction("<:NaoFlustered:852672068574117908>")
    if m == "will you go out with me nao?":
        await c.send("I think I would rather date Ryouhei. <:NaoLUL:609342186684940288>")
    if m == "nao help":
        await client.get_user(message.author.id).send(help)
    if message.mentions:
        if m == ("sora kill " + message.mentions[0].mention).lower():
            stick = await message.guild.fetch_sticker(1005758615656878160)
            await c.send(stick)
    if message.content.lower() == "nao, reset" and message.author.id == 407747014806208523:
        await message.channel.send("Resetting")
        exit()
    if m == "give the cult some love" and message.author.id == 407747014806208523:
        try:
            cult = await message.guild.get_channel(1000956025278570596)
        except:
            pass
        await cult.send("I love you guys!")


client.run(TOKEN)